from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todos')


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'


class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo/todo.html'


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('todos')


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('todos')


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todos')
