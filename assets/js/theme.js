// Apply the saved or system theme before rendering to avoid a colour flash.
const readTheme = () => {
  try {
    return localStorage.getItem("theme");
  } catch (_) {
    return null;
  }
};

const updateThemeControl = () => {
  const button = document.getElementById("light-toggle");
  if (!button) return;
  const dark = document.documentElement.getAttribute("data-theme") === "dark";
  const label = dark ? "Switch to light mode" : "Switch to dark mode";
  button.title = label;
  button.setAttribute("aria-label", label);
};

const setTheme = (theme) => {
  document.documentElement.setAttribute("data-theme", theme);
  try {
    localStorage.setItem("theme", theme);
  } catch (_) {
    // Theme switching still works when browser storage is unavailable.
  }
  updateThemeControl();
};

const savedTheme = readTheme();
const systemTheme = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
  ? "dark" : "light";
setTheme(savedTheme === "dark" || savedTheme === "light" ? savedTheme : systemTheme);
