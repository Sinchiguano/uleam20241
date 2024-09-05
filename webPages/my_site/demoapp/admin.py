from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Menu
from .models import Customer
from .models import Vehicle

admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Vehicle)