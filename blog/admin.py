
from django.contrib import admin
from .models import Eventos, Hotel, Room, customer

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Eventos)
admin.site.register(Room)
admin.site.register(customer)
