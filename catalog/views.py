from django.shortcuts import render

# Create your views here. Создает Ваше отображение здесь

from .models import Book, Author, BookInstance, Genre, Rifle, Gallery

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    num_genres=Genre.objects.filter()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_visits':num_visits}, # num_visits appended
    )

from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

def testing(request):
    return render(
        request,
        'catalog/testing.html')

class RifleListView(generic.ListView):
    model = Rifle


class RifleDetailView(generic.DetailView):
    model = Rifle

def gallery_detail_page(request):
    obj = Gallery.objects.get(id=1)
    template_name = 'catalog/gallery_detail.html'
    context = {"object": obj}
    return render (request, template_name, context)

def weapons(request):
    return render(request, 'catalog/all_weapons.html')

def prestige(request):
    obj = Gallery.objects.get(id=2)
    template_name = 'catalog/prestige_detail.html'
    context = {"object": obj}
    return render (request, template_name, context)
