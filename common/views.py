from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from books.models import Books

UserModel = get_user_model()


class HomePageView(ListView):
    template_name = 'home-page.html'
    model = Books


class SearchResultsView(ListView):
    model = Books
    template_name = "home-page.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Books.objects.filter(Q(title__icontains=query))
        try:
            object_list[0]
        except IndexError:
            return render(None, 'book-does-not-exists.html')
        return object_list
