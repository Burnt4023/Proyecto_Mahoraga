from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.my_view, name='index'),
]