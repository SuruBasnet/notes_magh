from django.contrib import admin
from .models import Note, NoteType
# Register your models here.
admin.site.register(Note)

admin.site.register(NoteType)