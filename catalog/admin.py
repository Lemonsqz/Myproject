from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
#Зарегистрируйте модели путем вставки следующего текста в нижнюю часть этого файла.
#Этот код просто импортирует модели и затем вызывает  admin.site.register для регистрации каждой из них.
from .models import Author, Genre, Book, BookInstance, Rifle, Gallery

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

#admin.site.register(Author)

@admin.register(Gallery)
class GalleryAdmin(SummernoteModelAdmin):
    summernote_fields = ('gname', 'img_g')
    list_display = ('gname',)

@admin.register(Rifle)
class RifleAdmin(SummernoteModelAdmin):
    summer_note_fields = ('rif_summary', 'rif_name')
    list_display = ('rname',)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)

#Register the admin class with the associated model
#admin.site.register(Book)
#admin.site.register(BookInstance)
#Register the Admin classes for Book using the decorator
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)#@тоже самое что и admin.site.register
class BookAdmin(SummernoteModelAdmin):
    summer_note_fields = ('summary', 'title')
    list_display = ('bname','author', 'display_genre')
    inlines = [BookInstanceInline]



#Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back','id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('New bookinstance', {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
