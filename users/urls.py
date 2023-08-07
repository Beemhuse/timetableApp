# from dj_rest_auth.views import LoginView
from django.urls import path
from users.views import SignUpView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', SignUpView.as_view()),

]
