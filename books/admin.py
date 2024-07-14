from django.contrib import admin

from .models import Books, Authors, Publishers


# Register your models here.


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'autor', 'publisher', 'genre', 'owner', 'image', 'is_borrow', 'return_date', 'year_of_publication')
    list_filter = ('genre',)
    fieldsets = (
        (None, {
            'fields': (
                'title', 'autor', 'publisher', 'genre', 'owner', 'image', 'is_borrow', 'return_date',
                'year_of_publication')
        }),
    )


@admin.register(Authors)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)


@admin.register(Publishers)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ("publisher_name__startswith",)
