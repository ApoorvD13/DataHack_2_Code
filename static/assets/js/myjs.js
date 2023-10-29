dashboardLink = document.getElementById("dashboard-link");
violationsLink = document.getElementById("violations-link");
factoryLink = document.getElementById("factory-link");
evidenceLink = document.getElementById("evidence-link");

activeLink =
  window.location.pathname === "/"
    ? dashboardLink
    : window.location.pathname.startsWith("/violation")
    ? violationsLink
    : window.location.pathname.startsWith("/factory")
    ? factoryLink
    : evidenceLink;

dashboardLink.addEventListener("click", () => {
  activeLink.classList.remove("active");
  dashboardLink.classList.add("active");
  activeLink = dashboardLink;
});

violationsLink.addEventListener("click", () => {
  activeLink.classList.remove("active");
  violationsLink.classList.add("active");
  activeLink = violationsLink;
});

factoryLink.addEventListener("click", () => {
  activeLink.classList.remove("active");
  factoryLink.classList.add("active");
  activeLink = factoryLink;
});

evidenceLink.addEventListener("click", () => {
  activeLink.classList.remove("active");
  evidenceLink.classList.add("active");
  activeLink = evidenceLink;
});

activeLink.classList.add("active");
