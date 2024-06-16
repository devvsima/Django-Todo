from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('create/', views.create_todo, name='create'),
    path('done/', views.done_todo, name='done'),
    path('current/', views.current_todo, name='current'),
    path('all/', views.all_todo, name='all'),
    
    path('edit/<int:task_id>', views.edit_todo, name='edit'),
    
    path('delete/<int:task_id>', views.delete_todo, name='delete'),
    path('mark-as-done/<int:task_id>', views.mark_as_done, name='mark_as_done'),
    path('mark-as-current/<int:task_id>', views.mark_as_current, name='mark_as_current'),
]
