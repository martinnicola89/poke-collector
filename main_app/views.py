from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pokemon


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def poke_index(request):
    party = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'party': party})


def poke_detail(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon})


def poke_new(request):
    return render(request, 'pokemon/new.html')


def poke_create(request):
    pokemon = Pokemon.objects.create(
        name=request.POST['name'],
        poke_type=request.POST['poke_type'],
        strongest_attack=request.POST['strongest_attack'],
        date_caught=request.POST['date_caught'],
        image=request.POST['image'],
        team=request.POST['team'],
    )
    return redirect(f'/party/{pokemon.id}')


def poke_delete(request, poke_id):
    Pokemon.objects.filter(id=poke_id).delete()
    return redirect(f'/party')


def poke_edit(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    return render(request, 'pokemon/edit.html', {'pokemon': pokemon})


def poke_update(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    pokemon.name = request.POST['name']
    pokemon.poke_type = request.POST['poke_type']
    pokemon.strongest_attack = request.POST['strongest_attack']
    pokemon.date_caught = request.POST['date_caught']
    pokemon.image = request.POST['image']
    if request.POST['team'] == "Yes":
        pokemon.team = True
    else:
        pokemon.team = False
    # pokemon.team = request.POST['team']
    pokemon.save()
    return redirect(f'/party/{pokemon.id}')


def team(request):
    team = Pokemon.objects.filter(team=True)
    return render(request, 'pokemon/team.html', {'team': team})
