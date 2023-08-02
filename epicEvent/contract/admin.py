from django.contrib import admin
from .models import Event, Contract, Customer

# Register your models here.
admin.site.register([Customer, Contract, Event])
