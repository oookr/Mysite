from django.urls import path, include
# from . import views
from django.views.generic import ListView, DetailView
from news.models import Articles


urlpatterns = [
	path('',
		ListView.as_view(queryset = Articles.objects.filter(id = 2).order_by("-date")[:20], 
        template_name="news/posts.html")),
]
