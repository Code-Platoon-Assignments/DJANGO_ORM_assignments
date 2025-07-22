from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Owner,Cat,Bird,Dog,Exotic_Animal])