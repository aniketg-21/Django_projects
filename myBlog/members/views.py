from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import SignUpForm, EditSettingsForm, UserProfileForm, PassChangeForm
from django.contrib.auth import authenticate, login
from blog.models import Profile, Post

# Create your views here.
class UserLoginView(View):
    template_name = 'registration/login_modal.html'

    def post(self, request):
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged in.")
                return redirect('BlogHome')
            else:
                messages.error(request, "Invalid credentials! Please enter correct username or password.")
                return redirect('BlogHome')

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        user_posts = Post.objects.filter(author=user_profile.user.id)
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        context["user_profile"] = user_profile
        context["user_posts"] = user_posts
        return context

class UserRegistrationView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('Login')
    success_message = '%(username)s have been registered successfully. You may Login now.'

class EditUserSettingsView(SuccessMessageMixin, UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('BlogHome')
    success_message = '%(username)s - your settings has been updated successfully.'

    def get_object(self):
        return self.request.user

class EditUserProfileView(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'registration/edit_profile.html'
    success_message = 'Your Profile has been updated successfully.'

class CreateUserProfileView(SuccessMessageMixin, CreateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'registration/create_profile.html'
    success_message = 'Your Profile has been created successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PassChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PassChangeForm
    success_url = reverse_lazy('BlogHome')
    success_message = 'Your password has been changed successfully.'
