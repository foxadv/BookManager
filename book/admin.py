from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Book,BookAdmin)
