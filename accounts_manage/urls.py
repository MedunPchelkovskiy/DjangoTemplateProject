from django.urls import path


from accounts_manage.views import SignUpView, SignInView, SignOutView, ProfileDetailsView, ProfileEditView, ProfileDeleteView


urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile-edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
    path('profile-delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),

]

from .signals import *
