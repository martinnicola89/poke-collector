from django.contrib import admin

from .models import Pokemon, Item, Attack

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Item)
admin.site.register(Attack)
