from django.contrib import admin

# Register your models here.
from .models import Menu
from .models import MenuCategory

admin.site.register(Menu)
admin.site.register(MenuCategory)
