from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item, Attack
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def poke_index(request):
    # party = Pokemon.objects.all()
    party = Pokemon.objects.filter(user=request.user)
    return render(request, 'pokemon/index.html', {'party': party})


@login_required
def poke_detail(request, poke_id):
    pokemon = Pokemon.objects.get(user=request.user, id=poke_id)
    # attacks = Attack.objects.all()
    attacks = Attack.objects.filter(user=request.user)
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon, 'attacks': attacks})


@login_required
def poke_new(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'pokemon/new.html', {'items': items})


@login_required
def poke_create(request):
    pokemon = Pokemon.objects.create(
        name=request.POST['name'],
        poke_type=request.POST['poke_type'],
        date_caught=request.POST['date_caught'],
        image=request.POST['image'],
        team=request.POST['team'],
        item=Item.objects.get(user=request.user, name=request.POST['item']),
        user=request.user,
    )
    return redirect(f'/party/{pokemon.id}')


@login_required
def poke_delete(request, poke_id):
    Pokemon.objects.filter(id=poke_id).delete()
    return redirect(f'/party')


@login_required
def poke_edit(request, poke_id):
    pokemon = Pokemon.objects.get(user=request.user, id=poke_id)
    # items = Item.objects.all()
    items = Item.objects.filter(user=request.user)
    return render(request, 'pokemon/edit.html', {'pokemon': pokemon, 'items': items})


@login_required
def poke_update(request, poke_id):
    pokemon = Pokemon.objects.get(id=poke_id)
    pokemon.name = request.POST['name']
    pokemon.poke_type = request.POST['poke_type']
    pokemon.date_caught = request.POST['date_caught']
    pokemon.image = request.POST['image']
    pokemon.item = Item.objects.get(
        user=request.user, name=request.POST['item'])
    pokemon.team = request.POST['team']
    pokemon.save()
    return redirect(f'/party/{pokemon.id}')


@login_required
def team(request):
    team = Pokemon.objects.filter(user=request.user, team=True)
    return render(request, 'pokemon/team.html', {'team': team})


@login_required
def item_index(request):
    # items = Item.objects.all()
    items = Item.objects.filter(user=request.user)
    return render(request, 'item/index.html', {'items': items})


@login_required
def item_create(request):
    Item.objects.create(
        name=request.POST['name'],
        boost=request.POST['boost'],
        user=request.user,
    )
    return redirect('/item')


@login_required
def assoc_attack(request, poke_id, attack_id):
    # Note that you can pass a toy's id instead of the whole object
    Pokemon.objects.get(user=request.user, id=poke_id).attacks.add(attack_id)
    return redirect('detail', poke_id=poke_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class AttackList(LoginRequiredMixin, ListView):
    model = Attack

    def get_queryset(self):
        return Attack.objects.filter(user=self.request.user)


class AttackDetail(LoginRequiredMixin, DetailView):
    model = Attack

    def get_queryset(self):
        return Attack.objects.filter(user=self.request.user)


class AttackCreate(LoginRequiredMixin, CreateView):
    model = Attack
    # fields = '__all__'
    fields = ['name', 'type']
    # This inherited method is called when a
    # valid cat form is being submitted

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class AttackUpdate(LoginRequiredMixin, UpdateView):
    model = Attack
    fields = ['name', 'type']


class AttackDelete(LoginRequiredMixin, DeleteView):
    model = Attack
    success_url = '/attacks/'
