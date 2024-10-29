from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import RegisterView, ProfileView, activate

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', activate, name='verify_email'),
]