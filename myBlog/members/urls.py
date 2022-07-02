from django.urls import path
from .views import UserRegistrationView, UserLoginView, EditUserSettingsView, CreateUserProfileView, EditUserProfileView, PassChangeView, ShowProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="Register"),
    path('login/', UserLoginView.as_view(), name="Login"),
    path('<int:pk>/profile', ShowProfileView.as_view(), name="UserProfile"),
    path('<int:pk>/edit_profile/', EditUserProfileView.as_view(), name="EditProfile"),
    path('create_profile/', CreateUserProfileView.as_view(), name="CreateProfile"),
    path('edit_settings/', EditUserSettingsView.as_view(), name="EditSettings"),
    path('password/', PassChangeView.as_view(template_name='registration/change_password.html')),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
]
