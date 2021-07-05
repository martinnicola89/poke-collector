from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('party/', views.poke_index, name='index'),
    path('party/<int:poke_id>', views.poke_detail, name='detail'),
]
