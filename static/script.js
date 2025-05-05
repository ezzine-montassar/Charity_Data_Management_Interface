function showSection(sectionId) {
    // Cacher le menu
    document.getElementById("menu").style.display = "none";

    // Cacher toutes les sections et retirer les anciennes classes de couleur
    let sections = document.querySelectorAll(".content");
    sections.forEach(section => {
        section.style.display = "none";
        section.classList.remove("bg-affichage", "bg-ajout", "bg-suppression", "bg-modification");
    });

    // Afficher la section sélectionnée
    const section = document.getElementById(sectionId);
    section.style.display = "block";

    // Ajouter la classe de couleur correspondante
    section.classList.add("bg-" + sectionId);

}

function showMenu() {
    // Afficher le menu
    document.getElementById("menu").style.display = "grid";

    // Cacher toutes les sections
    let sections = document.querySelectorAll(".content");
    sections.forEach(section => section.style.display = "none");
}


function showFormAjout() {
    const type = document.getElementById("Ajout-type").value;
    const majeurFormAjout = document.getElementById("majeurFormAjout");
    const enfantFormAjout = document.getElementById("enfantFormAjout");

    if (type === "majeur") {
        majeurFormAjout.style.display = "block";
        enfantFormAjout.style.display = "none";
    } else if (type === "enfant") {
        majeurFormAjout.style.display = "none";
        enfantFormAjout.style.display = "block";
    }
}


function showFormModification() {
    const type = document.getElementById("modification-type").value;
    const majeurFormModification = document.getElementById("majeurFormModification");
    const enfantFormModification = document.getElementById("enfantFormModification");

    if (type === "majeur") {
        majeurFormModification.style.display = "block";
        enfantFormModification.style.display = "none";
    } else if (type === "enfant") {
        majeurFormModification.style.display = "none";
        enfantFormModification.style.display = "block";
    }
}





function confirmerModification() {
    return confirm("Êtes-vous sûr de vouloir modifier ces données ?");
}

function closePopup() {
    document.getElementById("alert-popup").style.display = "none";
}