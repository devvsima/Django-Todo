from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('main.urls', namespace='main')),
    path('users/', include('users.urls', namespace='users')),
    path('todo/', include('todo.urls', namespace='todo')),

]

if DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)