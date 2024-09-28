#from django.views import View
# this is  import django view
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from CGM48FANS.models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('signin')  # Redirect เมื่อสำเร็จ
    template_name = 'signup/SignUp_form.html'

    def form_valid(self, form):
        context = self.get_context_data()
        member_form = context['member_form']
        if form.is_valid() and member_form.is_valid():
            user = form.save() #save data
            profile = member_form.save(commit=False)
            profile.user = user #place fk in profile
            profile.save() #save to database with all data
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class UserLoginView(LoginView):
    redirect_authenticated_user = True #redicret to LOGIN_REDIRECT_URLin setting
    template_name = 'signin/SignIn_form.html'
    success_url = reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('signin')
        