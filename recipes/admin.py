from django.contrib import admin
from .models import Recipe, Category


# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)