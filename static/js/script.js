document.addEventListener("DOMContentLoaded", function() {
    // Récupérer le chemin de l'URL actuelle
    var currentUrl = window.location.href;

    // Définir les noms des pages actives pour chaque lien de navigation
    var active_pages = {
        "client": "client",
        "object": "object",
        "insurance": "contracts"
        // Ajoutez d'autres pages si nécessaire
    };

    // Parcourir les noms de pages actives et vérifier si l'URL contient l'un d'eux
    for (var page in active_pages) {
        if (currentUrl.includes(active_pages[page])) {
            var activeNavItem = document.querySelector(`.nav li a[href*="${active_pages[page]}"]`);
            if (activeNavItem) {
                activeNavItem.parentElement.classList.add("active");
            }
            break; // Sortir de la boucle dès qu'une correspondance est trouvée
        }
    }
});

