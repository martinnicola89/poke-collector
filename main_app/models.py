from django.db import models


class Pokemon():  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, poke_type, strongest_attack, date_caught, image):
        self.name = name
        self.poke_type = poke_type
        self.strongest_attack = strongest_attack
        self.date_caught = date_caught
        self.image = image


party = [
    Pokemon('Alolan Raichu', 'Electric/Psychic', 'Psychic', '12/25/2018',
            'https://cdn.staticneo.com/w/pokemon/5/58/Alolan_Raichu.png'),
    Pokemon('Hitmonchan', 'Fighting', 'Mega Punch', '11/22/2018',
            'https://cdn2.bulbagarden.net/upload/a/a3/107Hitmonchan.png'),
    Pokemon('Starmie', 'Water/Psychic', 'Surf', '11/25/2018',
            'https://cdn2.bulbagarden.net/upload/c/cd/121Starmie.png'),
    Pokemon('Venusaur', 'Grass/Poison', 'Leech Seed', '12/1/2018',
            'https://cdn2.bulbagarden.net/upload/thumb/a/ae/003Venusaur.png/1200px-003Venusaur.png'),
    Pokemon('Poliwrath', 'Water/Fighting', 'Superpower', '12/1/2018',
            'https://cdn2.bulbagarden.net/upload/2/2d/062Poliwrath.png'),
    Pokemon('Magmar', 'Fire', 'Fire Punch', '11/25/2018',
            'https://cdn2.bulbagarden.net/upload/thumb/8/8c/126Magmar.png/1200px-126Magmar.png')
]
