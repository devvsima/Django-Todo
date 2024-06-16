from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('create/', views.create_todo, name='create'),
    path('delete/', views.delete_todo, name='delete'),
    path('currenttodos/', views.currenttodos, name='currenttodos'),
    path('done/', views.done_todo, name='done'),
    path('all/', views.all_todo, name='all'),
]
