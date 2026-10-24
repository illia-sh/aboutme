(() => {
  const nav = document.querySelector('.nav-inner');
  const toggle = document.querySelector('.menu-toggle');
  const links = document.getElementById('nav-links');
  if (nav && toggle && links) {
    const setOpen = (open, restoreFocus = false) => {
      toggle.setAttribute('aria-expanded', String(open));
      links.classList.toggle('is-open', open);
      if (restoreFocus) toggle.focus();
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    links.addEventListener('click', event => {
      if (event.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') setOpen(false, true);
    });
    document.addEventListener('click', event => {
      if (!nav.contains(event.target)) setOpen(false);
    });
    // Navigation stays visible if JavaScript is unavailable or fails to load.
    toggle.hidden = false;
    nav.classList.add('nav-enhanced');
    nav.closest('.site-header').classList.add('nav-enhanced-header');
  }
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
