from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('welcome/', views.welcome),
    path('welcome/<str:username>/', views.welcome_user),
    path('hello_user/', views.hello_user),
]
