from django.db import models
from django.urls import reverse


class Attack(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attacks_detail', kwargs={'pk': self.id})


class Item(models.Model):
    name = models.CharField(max_length=100, default='X-Attack')
    boost = models.IntegerField(default=2)

    # def __str__(self):
    #     return f"{self.name} (+{self.boost})"


class Pokemon(models.Model):
    name = models.CharField(max_length=100)  # maps to sql var char
    poke_type = models.CharField(max_length=100)  # maps to sql var char
    date_caught = models.CharField(max_length=100)
    image = models.TextField(max_length=1000)
    team = models.BooleanField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    attacks = models.ManyToManyField(Attack)

    # If I print something from the database, it'll display the string below

    # def __str__(self):
    #     return f"The {self.poke_type} type, {self.name}, caught on {self.date_caught} has an item, {self.item}"
