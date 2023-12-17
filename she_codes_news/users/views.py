from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from news.models import NewsStory  
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserProfile, CustomUser
from django.core.exceptions import PermissionDenied

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to the login page upon successful account creation
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        # This method is called when the form is valid after submission
        response = super().form_valid(form)
        
        # Create a user profile associated with the newly created user
        UserProfile.objects.create(user=self.object)
        
        return response
    
@login_required 
def AccountView(request):
    # Retrieves or creates a user profile for the currently logged-in user
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Retrieves news stories authored by the current user
    user_stories = NewsStory.objects.filter(author=request.user)
    
    # Render the user account page with the user profile and associated news stories
    return render(request, 'users/account.html', {'user_profile': user_profile, 'user_stories': user_stories})

class UpdateProfileView(UpdateView):
    model = CustomUser
    template_name = "users/update_profile.html"
    fields = ['username', 'email', 'bio']  # Fields that can be updated in the profile
    success_url = reverse_lazy('users:account')  # Redirect to the account view after successful update

class DeleteProfileView(DeleteView):
    model = CustomUser
    template_name = "users/delete_profile.html"
    success_url = reverse_lazy('news:index')  # Redirect to the news index after successful profile deletion

def login_redirect(request):
    return redirect (reverse_lazy('users:account', kwargs={'pk': request.user.id}))