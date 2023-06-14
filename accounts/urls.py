from django.urls import path
from accounts.views import LoginView, SignUpView

app_name = 'accounts'
urlpatterns = [

    # Example: /accounts/signIn/
    path('signIn/', LoginView.as_view(), name='login'),

    # Example: /accounts/signUp/
    path('signUp/', SignUpView.as_view(), name='signUp'),

]