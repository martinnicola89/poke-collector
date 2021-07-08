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
    path('item/', views.item_index),
    path('item/new', views.item_create),
    path('attacks/', views.AttackList.as_view(), name='attacks_index'),
    path('attacks/<int:pk>/', views.AttackDetail.as_view(), name='attacks_detail'),
    path('attacks/create/', views.AttackCreate.as_view(), name='attacks_create'),
    path('attacks/<int:pk>/update/',
         views.AttackUpdate.as_view(), name='attacks_update'),
    path('attacks/<int:pk>/delete/',
         views.AttackDelete.as_view(), name='attacks_delete'),
    path('party/<int:poke_id>/assoc_attack/<int:attack_id>/',
         views.assoc_attack, name='assoc_attack'),
]
