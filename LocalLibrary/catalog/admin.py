from django.contrib import admin
from .models import Author, Genre, Book, Bookinstance, Language


# Define the admin class
class BooksInstanceInline(admin.TabularInline):
    model = Bookinstance
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

@admin.register(Bookinstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(Bookinstance)
admin.site.register(Language)
