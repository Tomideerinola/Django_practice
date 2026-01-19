# applications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list, name='job_list'),  # our first page
]