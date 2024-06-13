from django.contrib import admin

# Register your models here.
from store.models import Categorymod,Productmod
admin.site.register(Categorymod)
admin.site.register(Productmod)