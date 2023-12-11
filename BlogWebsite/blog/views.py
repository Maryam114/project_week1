from django.shortcuts import render

# Create your views here.
#--------------------------------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Usernew,Post,Category,Comment
def blogs(request):
    blogs = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'blogs': blogs,
    }
    return HttpResponse(template.render(context, request))

def blogdetails(request,ID_Post):
    blogs = Post.objects.get(ID_Post=ID_Post)
    template = loader.get_template('blogdetails.html')
    context = {
        'blogs': blogs,
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    categories = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))


def comments(request):
    comments = Comment.objects.all()
    template = loader.get_template('comments.html')
    context = {
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

def users(request):
    users = Usernew.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())



