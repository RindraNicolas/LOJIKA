
from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("vinideo/", views.vinideo, name="vinideo"),
    path("efambolena/", views.efambolena, name="efambolena"),
    path("genealogie/", views.genealogie, name="genealogie"),
]
