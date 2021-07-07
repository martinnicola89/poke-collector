from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('party/', views.poke_index, name='index'),
    path('party/<int:poke_id>', views.poke_detail, name='detail'),
    path('party/new', views.poke_new),
    path('pokemon_submit/', views.poke_create),
    path('party/<int:poke_id>/delete', views.poke_delete),
    path('party/<int:poke_id>/edit', views.poke_edit),
    path('party/<int:poke_id>/poke_submit_update_form', views.poke_update),
    path('team/', views.team, name='team'),
]
