from django.urls import path

from common.views import HomePageView, SearchResultsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home page'),
    path('search/', SearchResultsView.as_view(), name='search results'),
]
