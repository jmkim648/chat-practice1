from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView


signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="user/form.html",
    success_url="/user/login/",
)

login = LoginView.as_view(
    template_name="user/form.html",
)

logout = LogoutView.as_view(next_page="/user/login/")
