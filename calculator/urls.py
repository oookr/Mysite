from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('kca48/', views.kcah, name='kcah'),
]
