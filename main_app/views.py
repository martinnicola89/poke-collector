from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item, Attack


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def poke_index(request):
    party = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'party': party})


def poke_detail(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    attacks = Attack.objects.all()
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon, 'attacks': attacks})


def poke_new(request):
    items = Item.objects.all()
    return render(request, 'pokemon/new.html', {'items': items})


def poke_create(request):
    pokemon = Pokemon.objects.create(
        name=request.POST['name'],
        poke_type=request.POST['poke_type'],
        date_caught=request.POST['date_caught'],
        image=request.POST['image'],
        team=request.POST['team'],
        item=Item.objects.get(name=request.POST['item']),
    )
    return redirect(f'/party/{pokemon.id}')


def poke_delete(request, poke_id):
    Pokemon.objects.filter(id=poke_id).delete()
    return redirect(f'/party')


def poke_edit(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    items = Item.objects.all()
    return render(request, 'pokemon/edit.html', {'pokemon': pokemon, 'items': items})


def poke_update(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    pokemon.name = request.POST['name']
    pokemon.poke_type = request.POST['poke_type']
    pokemon.date_caught = request.POST['date_caught']
    pokemon.image = request.POST['image']
    pokemon.item = Item.objects.get(name=request.POST['item'])
    pokemon.team = request.POST['team']
    pokemon.save()
    return redirect(f'/party/{pokemon.id}')


def team(request):
    team = Pokemon.objects.filter(team=True)
    return render(request, 'pokemon/team.html', {'team': team})


def item_index(request):
    items = Item.objects.all()
    return render(request, 'item/index.html', {'items': items})


def item_create(request):
    Item.objects.create(
        name=request.POST['name'],
        boost=request.POST['boost'],
    )
    return redirect('/item')


def assoc_attack(request, poke_id, attack_id):
    # Note that you can pass a toy's id instead of the whole object
    Pokemon.objects.get(id=poke_id).attacks.add(attack_id)
    return redirect('detail', poke_id=poke_id)


class AttackList(ListView):
    model = Attack


class AttackDetail(DetailView):
    model = Attack


class AttackCreate(CreateView):
    model = Attack
    fields = '__all__'


class AttackUpdate(UpdateView):
    model = Attack
    fields = ['name', 'type']


class AttackDelete(DeleteView):
    model = Attack
    success_url = '/attacks/'
