from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', TodoList.as_view(), name='todos'),
    path('todo/<str:pk>/', TodoDetail.as_view(), name='todo'),
    path('todo-create/', TodoCreate.as_view(), name='todo-create'),
    path('todo-edit/<str:pk>/', TodoUpdate.as_view(), name='todo-update'),
    path('todo-delete/<str:pk>/', TodoDelete.as_view(), name='todo-delete')
]
