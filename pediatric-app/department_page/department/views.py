from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import *
from .models import *
from .utils import DataMixin


class GeneralHome(DataMixin, ListView):
    model = General
    template_name = 'department/index.html'
    context_object_name = 'general'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GeneralHome, self).get_context_data(**kwargs)
        context['posts'] = News.objects.all()
        c_def = self.get_user_context(title='Кафедра педиатрии')
        return dict(list(context.items()) + list(c_def.items()))


class NewsHome(DataMixin, ListView):
    model = News
    template_name = 'department/index.html'
    context_object_name = 'posts'


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'department/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class TableHome(LoginRequiredMixin, DataMixin, ListView):
    model = General
    template_name = 'department/timetables.html'
    context_object_name = 'timetable'
    login_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Расписание')
        return dict(list(context.items()) + list(c_def.items()))


class SignupUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'department/signupuser.html'
    success_url = reverse_lazy('loginuser')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'department/loginuser.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
