
from django.contrib import admin

from .models import Logiciel, CaptureEcran


class CaptureEcranInline(admin.TabularInline):

    model = CaptureEcran
    extra = 1

    fields = (
        "image",
        "legende",
        "ordre",
        "publie",
    )

    ordering = ("ordre",)


@admin.register(Logiciel)
class LogicielAdmin(admin.ModelAdmin):

    list_display = (
        "nom",
        "categorie",
        "version",
        "ordre",
        "publie",
        "date_modification",
    )

    list_filter = (
        "publie",
        "categorie",
    )

    search_fields = (
        "nom",
        "description",
        "categorie",
    )

    prepopulated_fields = {
        "slug": ("nom",),
    }

    list_editable = (
        "ordre",
        "publie",
    )

    ordering = ("ordre", "nom")

    fields = (
        "nom",
        "slug",
        "categorie",
        "icone",
        "accroche",
        "description",
        "fonctionnalites",
        "fichier_installation",
        "version",
        "date_publication",
        "notes_version",
        "ordre",
        "publie",
        "date_creation",
        "date_modification",
    )

    readonly_fields = (
        "date_creation",
        "date_modification",
    )

    inlines = [
        CaptureEcranInline,
    ]
