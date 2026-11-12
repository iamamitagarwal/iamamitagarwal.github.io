"""Check a built portfolio against its source records. No network required."""
import json
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse
from bs4 import BeautifulSoup

root = Path(sys.argv[1])
source = Path(__file__).resolve().parents[1]
errors = []
checked = 0
routes = []
for collection in ('publications', 'patents'):
    index = BeautifulSoup((root / collection / 'index.html').read_text(), 'html.parser')
    targets = {urlparse(a['href']).path for a in index.select('main a[href]') if urlparse(a['href']).path.startswith('/' + collection + '/') and urlparse(a['href']).path != '/' + collection + '/'}
    records = json.loads((root / 'publications.json').read_text())['publications'] if collection == 'publications' else list((source / '_patents').glob('*.md'))
    if len(targets) != len(records):
        errors.append(f'{collection}: {len(targets)} linked detail URLs, expected {len(records)}')
    routes.extend(targets)
for route in ('/', '/publications/', '/projects/', '/patents/', '/awards/', '/media/', '/talks/', '/workshops/', '/community/', '/cv/', '/research-topics/'):
    routes.append(route)
for html in root.rglob('*.html'):
    relative = html.relative_to(root).as_posix()
    routes.append('/' + relative[:-10] if relative.endswith('index.html') else '/' + relative)
for route in sorted(set(routes)):
    path = root / route.lstrip('/')
    if not route.endswith('.html'):
        path = path / 'index.html'
    if not path.exists():
        errors.append(f'Missing route: {route}')
        continue
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    checked += 1
    if len(soup.select('h1')) != 1:
        errors.append(f'{route}: expected one H1')
    if len(soup.select('link[rel=canonical]')) != 1:
        errors.append(f'{route}: expected one canonical')
    if route.startswith('/publications/') and route != '/publications/':
        if not soup.select('meta[name=citation_title]') or not soup.select('meta[name=citation_author]'):
            errors.append(f'{route}: missing citation title/authors')
        body = soup.select_one('.paper-body')
        first_block = body.find(recursive=False) if body else None
        if first_block is None or not first_block.get_text(' ', strip=True).startswith('Abstract.'):
            errors.append(f'{route}: author-written abstract must precede editorial overview')
    for script in soup.select('script[type="application/ld+json"]'):
        try:
            json.loads(script.string or script.get_text())
        except ValueError:
            errors.append(f'{route}: malformed JSON-LD')
    for tag in soup.select('a[href], img[src], link[rel=stylesheet], script[src]'):
        value = tag.get('href') or tag.get('src')
        if not value:
            errors.append(f'{route}: empty link or asset URL')
            continue
        url = urlparse(value)
        if url.scheme or url.netloc or not url.path.startswith('/'):
            continue
        target = root / unquote(url.path).lstrip('/')
        if url.path.endswith('/'):
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{route}: broken local target {value}')
        elif url.fragment and target.suffix == '.html':
            target_soup = soup if target == path else BeautifulSoup(target.read_text(), 'html.parser')
            if not target_soup.find(id=unquote(url.fragment)):
                errors.append(f'{route}: missing anchor {value}')
    for image in soup.select('img'):
        if not image.has_attr('alt'):
            errors.append(f'{route}: image missing alt')
print(json.dumps({'pages_checked': checked, 'errors': sorted(set(errors))}, indent=2))
sys.exit(bool(errors))
