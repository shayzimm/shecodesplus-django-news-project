from django.urls import path
from .views import AccountView, CreateAccountView, UpdateProfileView, DeleteProfileView

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('account/', AccountView, name='account'),
    path('editprofile/<int:pk>', UpdateProfileView.as_view(), name='update_profile'),
    path('editprofile/<int:pk>/deleteprofile', DeleteProfileView.as_view(), name='delete_profile'),
]