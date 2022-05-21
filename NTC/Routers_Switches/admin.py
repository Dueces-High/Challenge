from django.contrib import admin
from .models import Router
from .models import Interface

admin.site.register(Router)
admin.site.register(Interface)

# Register your models here.
