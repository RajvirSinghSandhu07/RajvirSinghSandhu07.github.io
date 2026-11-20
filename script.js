/**
 * ==========================================================================
 * RAJVIR SINGH SANDHU - PORTFOLIO SCRIPTS
 * ==========================================================================
 * Features:
 * - Dynamic scrollspy for active navigation links
 * - Frosted navbar background on scroll
 * - Responsive mobile navigation menu toggle
 * - Project category filtering with smooth display
 * - Raycast/Linear-style interactive cursor spotlight on cards
 * - One-click Copy Email with animated toast notifications
 * - Contact form handler (mailto pre-fill + clipboard backup)
 * - Intersection Observer for smooth section entrance reveals
 * - Current year auto-update
 * ==========================================================================
 */

document.addEventListener('DOMContentLoaded', () => {

  /* --------------------------------------------------------------------------
     1. Current Year Auto-Update
     -------------------------------------------------------------------------- */
  const yearElement = document.getElementById('currentYear');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  /* --------------------------------------------------------------------------
     2. Navbar Scrolled State & Mobile Menu Toggle
     -------------------------------------------------------------------------- */
  const navbar = document.getElementById('navbar');
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  // Sticky navbar shadow on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  // Mobile menu open / close
  if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      mobileMenuBtn.setAttribute('aria-expanded', isOpen);
    });

    // Close menu when clicking any nav item
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* --------------------------------------------------------------------------
     3. Scrollspy: Highlight Active Nav Link
     -------------------------------------------------------------------------- */
  const sections = document.querySelectorAll('section[id]');
  
  function updateActiveNavLink() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');
      const targetNavLink = document.querySelector(`.nav-menu a[href*="${sectionId}"]`);

      if (targetNavLink) {
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          targetNavLink.classList.add('active');
        } else {
          targetNavLink.classList.remove('active');
        }
      }
    });
  }

  window.addEventListener('scroll', updateActiveNavLink, { passive: true });

  /* --------------------------------------------------------------------------
     4. Intersection Observer: Reveal Elements on Scroll
     -------------------------------------------------------------------------- */
  const revealElements = document.querySelectorAll('.reveal-on-scroll');

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback if observer not supported
    revealElements.forEach(el => el.classList.add('revealed'));
  }

  /* --------------------------------------------------------------------------
     5. Project Filtering (All, Hackathons, Web, Prototypes)
     -------------------------------------------------------------------------- */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Set active state on button
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filterValue === 'all' || category === filterValue) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 20);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 250);
        }
      });
    });
  });

  /* --------------------------------------------------------------------------
     6. Raycast / Linear Card Spotlight Hover Effect
     -------------------------------------------------------------------------- */
  const cards = document.querySelectorAll('.project-card, .skill-category-card, .timeline-card, .about-highlight-card, .pinned-repo-card, .contact-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });

  /* --------------------------------------------------------------------------
     7. Toast Notification Utility
     -------------------------------------------------------------------------- */
  const toast = document.getElementById('toastNotification');
  const toastMsg = document.getElementById('toastMessage');
  let toastTimeout;

  function showToast(message, duration = 3000) {
    if (!toast) return;
    if (toastMsg) toastMsg.textContent = message;

    clearTimeout(toastTimeout);
    toast.classList.add('show');

    toastTimeout = setTimeout(() => {
      toast.classList.remove('show');
    }, duration);
  }

  /* --------------------------------------------------------------------------
     8. Copy Email to Clipboard
     -------------------------------------------------------------------------- */
  const copyEmailBtn = document.getElementById('copyEmailBtn');
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', () => {
      const emailToCopy = copyEmailBtn.getAttribute('data-copy') || 'rajvirssandhu007@gmail.com';
      
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(emailToCopy).then(() => {
          showToast(`Copied ${emailToCopy} to clipboard!`);
        }).catch(() => {
          fallbackCopyText(emailToCopy);
        });
      } else {
        fallbackCopyText(emailToCopy);
      }
    });
  }

  function fallbackCopyText(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
      showToast(`Copied ${text} to clipboard!`);
    } catch (err) {
      showToast('Could not copy automatically. Please copy manually.');
    }
    document.body.removeChild(textArea);
  }

  /* --------------------------------------------------------------------------
     9. Functional Contact Form (Mailto Generator + Clipboard Safety)
     -------------------------------------------------------------------------- */
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('senderName')?.value.trim();
      const email = document.getElementById('senderEmail')?.value.trim();
      const subject = document.getElementById('senderSubject')?.value.trim();
      const message = document.getElementById('senderMessage')?.value.trim();

      if (!name || !email || !message) {
        showToast('Please fill out all required fields.');
        return;
      }

      // Configure your destination email here (or edit placeholder)
      const recipientEmail = 'rajvirssandhu007@gmail.com';
      const emailSubject = encodeURIComponent(`[Portfolio Inquiry] ${subject || 'New Message from ' + name}`);
      const emailBody = encodeURIComponent(
        `Hi Rajvir,\n\n${message}\n\n---\nFrom: ${name}\nEmail: ${email}`
      );

      const mailtoLink = `mailto:${recipientEmail}?subject=${emailSubject}&body=${emailBody}`;

      // Open email client
      window.location.href = mailtoLink;

      showToast('Opening your default email client...');
    });
  }

  /* --------------------------------------------------------------------------
     10. Subtle Developer Guide in Browser Console
     -------------------------------------------------------------------------- */
  console.log(
    '%c Rajvir Singh Sandhu - Developer Portfolio %c Ready for personalization ',
    'background: #4f46e5; color: #ffffff; padding: 4px 8px; border-radius: 4px; font-weight: bold;',
    'background: #18181b; color: #38bdf8; padding: 4px 8px; border-radius: 4px;'
  );
  console.log('To customize:\n1. Update GitHub & LinkedIn URLs in index.html\n2. Replace placeholder email in index.html & script.js\n3. Add your PDF resume to assets/resume.pdf\n4. Add real screenshots to assets/images/ when available.');

});
