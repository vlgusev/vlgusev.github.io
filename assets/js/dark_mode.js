document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("light-toggle");
  if (!button) return;
  updateThemeControl();
  button.addEventListener("click", () => {
    const dark = document.documentElement.getAttribute("data-theme") === "dark";
    setTheme(dark ? "light" : "dark");
  });
});
