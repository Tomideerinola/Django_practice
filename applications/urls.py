# applications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/add/', views.add_job, name='add_job'),
    path('job/<int:pk>/edit/', views.edit_job, name='edit_job'),
    path('job/<int:pk>/delete/', views.delete_job, name='delete_job'),
    
]