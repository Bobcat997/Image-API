from django.contrib import admin

from .models import Basic, Premium, Enterprise, Image

myModels = [Basic, Premium, Enterprise, Image]
admin.site.register(myModels)