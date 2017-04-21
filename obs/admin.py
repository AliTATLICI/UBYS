from django.contrib import admin
from .models import *

admin.site.register(Program)
admin.site.register(Ogrenci)

class Blog(admin.ModelAdmin):
    list_display = ('created', 'title', 'code', 'linenos', 'language','style')
    search_fields = ('created', 'title', 'code', 'language','style')
admin.site.register(Snippet,Blog)
