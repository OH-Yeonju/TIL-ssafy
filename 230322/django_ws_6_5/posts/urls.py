from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('posts/', views.index, name='index'),
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.post, name='post'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/update', views.update, name='update'),
]
