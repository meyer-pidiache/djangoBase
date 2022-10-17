const home = document.getElementById("home-i");
const path = window.location.pathname;

if (path == "/home/") {
  home.classList.add("active");
} else {
  home.classList.remove("active");
}


(() => {
  "use strict";
  const tooltipTriggerList = Array.from(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.forEach((tooltipTriggerEl) => {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
})();
