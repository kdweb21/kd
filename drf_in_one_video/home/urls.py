
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, ),    
    path('post-todo', views.post_todo, name="todo" ),    
]
