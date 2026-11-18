
from django.db import models


class Logiciel(models.Model):

    nom = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nom du logiciel",
    )

    slug = models.SlugField(
        max_length=160,
        unique=True,
        verbose_name="Identifiant URL",
    )

    categorie = models.CharField(
        max_length=100,
        verbose_name="Catégorie",
    )

    description = models.TextField(
        verbose_name="Description",
    )

    icone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Icône",
    )

    accroche = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Phrase d'accroche",
    )

    fonctionnalites = models.TextField(
        blank=True,
        default="",
        verbose_name="Fonctionnalités",
        help_text="Une fonctionnalité par ligne.",
    )

    # INFORMATIONS DE TÉLÉCHARGEMENT

    fichier_installation = models.FileField(
        upload_to="installations/",
        blank=True,
        null=True,
        verbose_name="Fichier d'installation",
    )

    version = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Version",
    )

    date_publication = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date de publication",
    )

    notes_version = models.TextField(
        blank=True,
        verbose_name="Notes de version",
    )

    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage",
    )

    publie = models.BooleanField(
        default=True,
        verbose_name="Publié",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création",
    )

    date_modification = models.DateTimeField(
        auto_now=True,
        verbose_name="Dernière modification",
    )

    class Meta:
        verbose_name = "Logiciel"
        verbose_name_plural = "Logiciels"
        ordering = ["ordre", "nom"]

    def __str__(self):
        return self.nom


class CaptureEcran(models.Model):

    logiciel = models.ForeignKey(
        Logiciel,
        on_delete=models.CASCADE,
        related_name="captures",
        verbose_name="Logiciel",
    )

    image = models.ImageField(
        upload_to="captures/",
        verbose_name="Capture d'écran",
    )

    legende = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Légende",
    )

    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage",
    )

    publie = models.BooleanField(
        default=True,
        verbose_name="Publié",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'ajout",
    )

    class Meta:
        verbose_name = "Capture d'écran"
        verbose_name_plural = "Captures d'écran"
        ordering = ["ordre", "id"]

    def __str__(self):
        return f"Capture - {self.logiciel.nom}"
