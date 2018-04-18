from django.contrib import admin

# Register your models here.
from .models import Todo, Status

admin.site.register(Todo)
admin.site.register(Status)
