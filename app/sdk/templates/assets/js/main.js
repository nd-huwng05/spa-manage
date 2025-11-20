(function() {
  "use strict";

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToggle() {
    document.body.classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }

  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToggle);
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navLink => {
    navLink.addEventListener('click', () => {
      if (document.body.classList.contains('mobile-nav-active')) {
        mobileNavToggle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(toggleBtn => {
    toggleBtn.addEventListener('click', function(e) {
      e.preventDefault();
      const parentLi = this.parentNode;
      parentLi.classList.toggle('active');
      const submenu = parentLi.querySelector('ul');
      if (submenu) submenu.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Navmenu Scrollspy - highlight current section
   */
  const navLinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    const scrollPosition = window.scrollY + 200;

    navLinks.forEach(link => {
      if (!link.hash) return;
      const section = document.querySelector(link.hash);
      if (!section) return;

      if (scrollPosition >= section.offsetTop && scrollPosition <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

})();