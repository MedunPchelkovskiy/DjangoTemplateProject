from django.urls import path


from accounts_manage.views import SignUpView, SignInView, SignOutView, ProfileDetailsView, ProfileEditView, UserDeleteView


urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),       #TODO: fix 405 error on this link
    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('add-profile-details/<int:pk>/', ProfileEditView.as_view(), name='add profile details'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='user delete'),

]

from .signals import *
