from django import forms

from forum.models import Topics, Posts

DISCUSSIONS_CHOICES = (
    ("Books", "BOOKS"),
    ("Authors", "AUTHORS"),
    ("Publishers", "PUBLISHERS"),
    ("Other", "OTHER"),
    ("All Topics", "ALL TOPICS"),
)


class CreateTopicForm(forms.ModelForm):
    initial_post = forms.CharField(max_length=255)

    class Meta:
        model = Topics

        fields = ['topic_name', 'category']

        labels = {
            'topic_name': 'Topic Name:',
            'category': 'Category:',
        }

        widgets = {
            'topic_name': forms.TextInput(attrs={'placeholder': 'Fill Topic Name'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
        }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'text_of_post'
        ]

        labels = {
            'text_of_post': 'Add_post:'
        }

        widgets = {
            'text_of_post': forms.TextInput(attrs={'placeholder': 'Add post'})
        }
