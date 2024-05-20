from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from forum.forms import SearchDiscussionForm, CreateTopicForm
from forum.models import Topics


class ForumHomePageView(LoginRequiredMixin, ListView):
    model = Topics
    template_name = 'forum.html'

    def get_context_data(self, **kwargs):
        context = super(ForumHomePageView, self).get_context_data(**kwargs)
        context['filter_form'] = SearchDiscussionForm()
        return context


def add_topic(request):
    if request.mehod == 'GET':
        context = {'form': CreateTopicForm()}
        return render(request, 'topic-create.html', context)

    topic_name = request.POST['topic_name']
    topic_autor = request.user
    category = request.POST['category']

    new_topic = Topics(
        topic_name=topic_name,
        topic_autor=topic_autor,
        category=category,
        post_count=1
    )

    new_topic.save()
    return redirect('forum')
