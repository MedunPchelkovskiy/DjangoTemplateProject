from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import CreateTopicForm, CreatePostForm, SearchDiscussionForm
from .models import Topics, Posts

UserModel = get_user_model()


class ForumHomePageView(LoginRequiredMixin, ListView):
    model = Topics
    template_name = 'forum.html'

    # queryset = Topics.objects.all().annotate(posts_count=Count('posts'))

    def get_context_data(self, **kwargs):
        context = super(ForumHomePageView, self).get_context_data(**kwargs)
        context['filter_form'] = SearchDiscussionForm()
        return context


def add_topic(request):
    if request.method == 'GET':
        context = {'form': CreateTopicForm()}
        return render(request, 'topic-create.html', context)

    topic_name = request.POST['topic_name']
    topic_author = request.user
    category = request.POST['category']

    new_topic = Topics(
        topic_name=topic_name,
        topic_author=topic_author,
        category=category,
        posts_count=1
    )

    new_topic.save()

    new_post = Posts(
        text_of_post=request.POST['initial_post'],
        post_to_topic=new_topic,
        post_author=request.user

    )

    new_post.save()

    return redirect('forum')


def topic_posts(request, pk):
    topic = Topics.objects.get(pk=pk)
    posts = Posts.objects.filter(post_to_topic=pk).all()
    # topic.comments_count = Posts.objects.filter(post_to_topic=pk).count()

    if request.method == 'GET':
        context = {
            'topic': topic,
            'posts': posts,
            'form': CreatePostForm()
        }

        return render(request, 'topic-posts.html', context=context)
    else:
        post_form = CreatePostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.post_to_topic = topic
            post.post_author = request.user
            topic.posts_count += 1
            post.save()
            topic.save()

        return redirect('posts topic', pk=pk)


def filter_topics(request):
    object_list = Topics.objects.all()
    if request.method == 'POST':
        filter_form = SearchDiscussionForm(request.POST)
        if filter_form.is_valid():
            searched_category = filter_form.cleaned_data['discussion_search_field']
            if searched_category == 'All Topics':
                object_list = object_list
            else:
                object_list = Topics.objects.filter(category=searched_category)
            try:
                object_list[0]
            except IndexError:
                return render(request, 'topic-does-not-exists.html', context={'filter_form': SearchDiscussionForm()})
    context = {
        'object_list': object_list,
        'filter_form': SearchDiscussionForm(),

    }

    return render(request, 'forum.html', context)
