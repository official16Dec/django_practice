from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request) :
    return HttpResponse("Hello, World!")

def welcome(request) :
    return HttpResponse("Welcome to Django!")

def welcome_user(request, username) :
    return HttpResponse("Welcome, {username}!")

def hello_user(request, username) :
    return render(request, 'hello.html', {'username': username})

def show_my_cv(request) :
    return render(request, 'my_cv.html', {})
