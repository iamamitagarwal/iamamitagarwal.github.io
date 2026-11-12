(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.primary-navigation');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    });
    nav.addEventListener('focusout', event => {
      if (!nav.contains(event.relatedTarget) && event.relatedTarget !== toggle) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open');
      }
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open'); toggle.focus();
      }
    });
  }
  const theme = document.querySelector('.theme-toggle');
  function labelTheme() {
    const dark = document.documentElement.classList.contains('theme-dark');
    if (theme) { theme.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`); }
  }
  labelTheme();
  if (theme) theme.addEventListener('click', () => {
    document.documentElement.classList.toggle('theme-dark');
    try { localStorage.setItem('portfolio-theme', document.documentElement.classList.contains('theme-dark') ? 'dark' : 'light'); } catch(e) {}
    labelTheme();
  });
})();
