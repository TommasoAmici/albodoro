from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("squadre/", views.squadre, name="squadre"),
    path("squadre/<int:pk>", views.team_detail, name="squadra"),
    path("user/<int:pk>", views.owner_detail, name="owner"),
    path("competizioni/", views.comps_all, name="competizioni"),
    path("competizioni/<int:pk>", views.comp_detail, name="competizione"),
    path("partita/<int:pk>", views.game_detail, name="partita"),
]
