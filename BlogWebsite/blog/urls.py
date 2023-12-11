from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blog'),
    path('categories/', views.categories, name='categories'),
    path('comments/', views.comments, name='comments'),
    path('blogs/blogdetails/<int:ID_Post>',views.blogdetails, name='blogdetails'),



]
