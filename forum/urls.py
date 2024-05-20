from django.urls import path

from forum.views import ForumHomePageView, add_topic

urlpatterns = [
    path('', ForumHomePageView.as_view(), name='forum'),
    path('add/', add_topic, name='add topic'),

]
