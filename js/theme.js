/**
 * Abu Haider Maintenance - Theme Handler (Dark / Light Mode)
 */
document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
  const storedTheme = localStorage.getItem('abu_haider_theme') || 'dark';

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('abu_haider_theme', theme);
    
    themeToggleBtns.forEach(btn => {
      const icon = btn.querySelector('i');
      if (icon) {
        icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
      }
    });
  }

  setTheme(storedTheme);

  themeToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      setTheme(newTheme);
    });
  });
});
