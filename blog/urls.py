from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Blog-home'),
    path('insert/', views.insertdata, name='Blog-insert'),    
]
