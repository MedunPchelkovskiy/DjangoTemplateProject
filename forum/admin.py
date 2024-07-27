
from django.contrib import admin

from .models import Topics, Posts


@admin.register(Topics)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ("publisher_name__startswith", )


@admin.register(Posts)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ("publisher_name__startswith", )