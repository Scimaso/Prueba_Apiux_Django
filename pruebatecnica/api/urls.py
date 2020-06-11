from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path('autor/<int:autor_id>/', views.autor_detail, name ="autor_detail"),
]
