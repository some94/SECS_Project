from django.urls import path
from accounts.views import LoginView, LogoutView, PasswordChangeView, SignUpView

app_name = 'accounts'
urlpatterns = [

    # Example: /accounts/signIn/
    path('signIn/', LoginView.as_view(), name='login'),

    # Example: /accounts/logout/
    path('logout/', LogoutView.as_view(), name='logout'),

    # Example: /accounts/passwordChange
    path('passwordChange/', PasswordChangeView.as_view(), name='passwordChange'),

    # Example: /accounts/signUp/
    path('signUp/', SignUpView.as_view(), name='signUp'),
]