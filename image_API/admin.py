from django.contrib import admin

from .models import Account, Plan, Image, Thumbnail

myModels = [Account, Plan, Image, Thumbnail]
admin.site.register(myModels)
