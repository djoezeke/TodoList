/* ===== TITLE CHANGE ===== */
document.addEventListener("visibilitychange", function () {
  if (document.visibilityState === "visible") {
    $("#favicon").attr("href", "assets/images/favicon.png");
  } else {
    document.title = "To-Do List | Task Organizer";
    $("#favicon").attr("href", "assets/images/favicon.png");
  }
});

/* ===== MODE CHANGE ===== */

// ===== DARK MODE TOGGLE =====
const themeToggleBtn = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");
const themeToggleText = document.getElementById("theme-toggle-text");
const htmlElement = document.getElementById("html");

function setTheme(theme) {
  htmlElement.setAttribute("data-bs-theme", theme);
  if (theme === "dark") {
    themeIcon.classList.remove("fa-moon");
    themeIcon.classList.add("fa-sun");
    themeToggleBtn.classList.add("btn-dark");
    themeToggleBtn.classList.remove("btn-outline-secondary");
    if (themeToggleText) themeToggleText.textContent = "Light Mode";
  } else {
    themeIcon.classList.remove("fa-sun");
    themeIcon.classList.add("fa-moon");
    themeToggleBtn.classList.remove("btn-dark");
    themeToggleBtn.classList.add("btn-outline-secondary");
    if (themeToggleText) themeToggleText.textContent = "Dark Mode";
  }
  // Animate icon
  themeIcon.classList.add("theme-icon-animate");
  setTimeout(() => themeIcon.classList.remove("theme-icon-animate"), 400);
}

// Load theme from localStorage
const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
  setTheme(savedTheme);
} else {
  // Default: match system
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  setTheme(prefersDark ? "dark" : "light");
}

themeToggleBtn.addEventListener("click", () => {
  const currentTheme = htmlElement.getAttribute("data-bs-theme");
  const newTheme = currentTheme === "dark" ? "light" : "dark";
  setTheme(newTheme);
  localStorage.setItem("theme", newTheme);
});

/* ===== HEADER REVEAL WHEN SCROLL DOWN TO 100px ===== */
const header = document.querySelector("[data-header]");

window.addEventListener("scroll", function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
});

/* ===== SCROLL REVEAL ANIMATION ===== */
const revealElements = document.querySelectorAll("[data-reveal]");
const revealDelayElements = document.querySelectorAll("[data-reveal-delay]");

const reveal = function () {
  for (let i = 0, len = revealElements.length; i < len; i++) {
    if (
      revealElements[i].getBoundingClientRect().top <
      window.innerHeight / 1.2
    ) {
      revealElements[i].classList.add("revealed");
    }
  }
};

for (let i = 0, len = revealDelayElements.length; i < len; i++) {
  revealDelayElements[i].style.transitionDelay =
    revealDelayElements[i].dataset.revealDelay;
}

window.addEventListener("scroll", reveal);
window.addEventListener("load", reveal);
