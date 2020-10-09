from django.contrib import admin

# Register your models here.
from .models import bankreq
from .models import bank

admin.site.register(bankreq)
admin.site.register(bank)
