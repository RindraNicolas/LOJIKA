
from django.shortcuts import render, get_object_or_404

from .models import Logiciel


# ==========================================================
# PAGE D'ACCUEIL
# ==========================================================

def accueil(request):

    logiciels = Logiciel.objects.filter(
        publie=True
    ).order_by(
        "ordre",
        "nom",
    )

    return render(
        request,
        "catalogue/accueil.html",
        {
            "logiciels": logiciels,
        },
    )


# ==========================================================
# AFFICHAGE D'UN LOGICIEL
# ==========================================================

def afficher_logiciel(request, slug):

    # Récupération du logiciel publié
    logiciel_db = get_object_or_404(
        Logiciel,
        slug=slug,
        publie=True,
    )

    # Récupération des captures d'écran publiées
    captures = logiciel_db.captures.filter(
        publie=True
    ).order_by(
        "ordre",
        "id",
    )

    # Préparation des informations du logiciel
    logiciel = {
        "nom": logiciel_db.nom,
        "categorie": logiciel_db.categorie,
        "theme": logiciel_db.slug,
        "icone": logiciel_db.icone,
        "accroche": logiciel_db.accroche,
        "description": logiciel_db.description,

        # Fonctionnalités
        "points": [
            ligne.strip()
            for ligne in logiciel_db.fonctionnalites.splitlines()
            if ligne.strip()
        ],

        # Téléchargement
        "fichier_installation": logiciel_db.fichier_installation,
        "version": logiciel_db.version,
        "date_publication": logiciel_db.date_publication,
        "notes_version": logiciel_db.notes_version,
    }

    return render(
        request,
        "catalogue/logiciel_detail.html",
        {
            "logiciel": logiciel,
            "captures": captures,
        },
    )


# ==========================================================
# PAGES INDIVIDUELLES DES LOGICIELS
# ==========================================================

def vinideo(request):

    return afficher_logiciel(
        request,
        "vinideo",
    )


def efambolena(request):

    return afficher_logiciel(
        request,
        "efambolena",
    )


def genealogie(request):

    return afficher_logiciel(
        request,
        "genealogie",
    )
