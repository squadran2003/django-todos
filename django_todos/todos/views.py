from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import RedirectView, UpdateView, DeleteView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import *
from .models import *

# Create your views here.
class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    template_name = 'todos/add_todo.html'
    success_url = reverse_lazy('home')
    fields = ('name','description')

    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        Status.objects.create(user=self.request.user,
                              todo=instance)
        return super().form_valid(form)

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todos/edit_todo.html'
    success_url = reverse_lazy('home')
    fields = ('name','description')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('home')

class TodoStatusView(RedirectView):
    url = reverse_lazy('home')

    def get(self,request, *args, **kwargs):
        todo_id = self.kwargs.get('pk')
        Status.objects.filter(todo=todo_id).update(status='DONE')
        return super().get(request,*args, **kwargs)

class TodoCompletedView(ListView):
    model = Todo
    template_name = 'index.html'

    def get_queryset(self):
        return Todo.objects.filter(status__status='DONE')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('todos:login')

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class logoutView(RedirectView):
    url = reverse_lazy('home')

    def get(self,request, *args, **kwargs):
        logout(request)
        return super().get(request,*args, **kwargs)

    

