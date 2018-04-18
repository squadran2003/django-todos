from django.shortcuts import render
from django.views.generic.list import ListView
from todos.models import Todo




class TodolistView(ListView):
    model = Todo
    template_name = 'index.html'
