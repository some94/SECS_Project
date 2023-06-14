from django.urls import path
from accounts.views import LoginView, SignUpView, SignUpDoneTV, PasswordUpdateView

app_name = 'accounts'
urlpatterns = [

    # Example: /accounts/signIn/
    path('signIn/', LoginView.as_view(), name='login'),

    # Example: /accounts/signUp/
    path('signUp/', SignUpView.as_view(), name='signUp'),

    # Example: /accounts/signUp/done
    path('signUp/done/', SignUpDoneTV.as_view(), name='signUp_done'),

    # Example: /accounts/passwordUpdate
    path('passwordUpdate/<int:user_email>/', PasswordUpdateView.as_view(), name='password_update'),
]