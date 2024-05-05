from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

# from books.models import Books
from accounts_manage.models import LibraryUser, UserProfile
from accounts_manage.forms import SignUpForm, SignInForm, ProfileEditForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home page')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        login(request, self.object)

        return response


class SignInView(LoginView):
    template_name = 'sign-in.html'
    form_class = SignInForm
    success_url = reverse_lazy('home page')


class SignOutView(LogoutView):
    template_name = 'sign-out.html'
    succes_url = reverse_lazy('home page')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    fields = '__all__'
    template_name = 'user-delete.html'
    success_url = reverse_lazy('home page')


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile-details.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'add-profile-details.html'
    # fields = '__all__'    # can't use if use fomr_class
    success_url = '/'
    form_class = ProfileEditForm

# def view_profile(request):
#     profile = LibraryUser.objects.first()
#     all_books = Books.objects.all()
#     context = {'profile': profile, 'all_books': all_books
#     }
#     return render(request, 'profile.html', context)


# def my_books(request, pk):
#     user = UserProfile.objects.get(user_id=pk)
#     all_books = Books.objects.get(owner=pk)

