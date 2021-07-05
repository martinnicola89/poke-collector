from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)  # maps to sql var char
    poke_type = models.CharField(max_length=100)  # maps to sql var char
    strongest_attack = models.CharField(max_length=100)
    date_caught = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    # If I print something from the database, it'll display the string below

    def __str__(self):
        return f"The {self.poke_type} type, {self.name}, caught on {self.date_caught}"


# class Pokemon():  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, poke_type, strongest_attack, date_caught, image):
#         self.name = name
#         self.poke_type = poke_type
#         self.strongest_attack = strongest_attack
#         self.date_caught = date_caught
#         self.image = image


# party = [
#     Pokemon('Alolan Raichu', 'Electric/Psychic', 'Psychic', '12/25/2018',
#             'https://cdn.staticneo.com/w/pokemon/5/58/Alolan_Raichu.png'),
#     Pokemon('Hitmonchan', 'Fighting', 'Mega Punch', '11/22/2018',
#             'https://cdn2.bulbagarden.net/upload/a/a3/107Hitmonchan.png'),
#     Pokemon('Starmie', 'Water/Psychic', 'Surf', '11/25/2018',
#             'https://cdn2.bulbagarden.net/upload/c/cd/121Starmie.png'),
#     Pokemon('Venusaur', 'Grass/Poison', 'Leech Seed', '12/1/2018',
#             'https://cdn2.bulbagarden.net/upload/thumb/a/ae/003Venusaur.png/1200px-003Venusaur.png'),
#     Pokemon('Poliwrath', 'Water/Fighting', 'Superpower', '12/1/2018',
#             'https://cdn2.bulbagarden.net/upload/2/2d/062Poliwrath.png'),
#     Pokemon('Magmar', 'Fire', 'Fire Punch', '11/25/2018',
#             'https://cdn2.bulbagarden.net/upload/thumb/8/8c/126Magmar.png/1200px-126Magmar.png')
# ]
