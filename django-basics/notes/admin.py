from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)
# Register your models here.

admin.site.register(models.Notes, NotesAdmin)