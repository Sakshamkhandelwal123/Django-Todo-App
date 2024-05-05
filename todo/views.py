from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Todo


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todos')


class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todos')
        return super(RegisterPage, self).get(*args, **kwargs)


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(user_id=self.request.user)
        context['count'] = context['todos'].filter(is_complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['todos'] = context['todos'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input

        return context


class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo/todo.html'


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'is_complete']
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('todos')


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todos')
