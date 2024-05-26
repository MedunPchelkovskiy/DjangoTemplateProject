from django.urls import path

from forum.views import ForumHomePageView, add_topic, filter_topics, topic_posts

urlpatterns = [
    path('', ForumHomePageView.as_view(), name='forum'),
    path('add/', add_topic, name='add topic'),
    path('posts/<int:pk>', topic_posts, name='posts topic'),
    # path('add-post/<int:pk>', add_post, name='add post'),
    path('filtered-topics/', filter_topics, name='filtered topics'),

]
