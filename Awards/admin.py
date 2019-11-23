from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Projects)
admin.site.register(Profile)