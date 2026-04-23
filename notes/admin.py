from django.contrib import admin  # <-- Cette ligne manquait !
from .models import Operation, Tag

admin.site.register(Operation)
admin.site.register(Tag)