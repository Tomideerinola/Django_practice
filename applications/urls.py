# applications/urls.py
from django.urls import path
from . import views
from .views import JobListView, JobCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/add/', views.add_job, name='add_job'),
    path('job/<int:pk>/edit/', views.edit_job, name='edit_job'),
    path('job/<int:pk>/delete/', views.delete_job, name='delete_job'),
    path('job/<int:pk>/view/', views.job_detail, name='job_detail'),
    path('books/', views.create_book_view, name='create_book_view'),
    path('thank-you/', views.success, name='success'),
    path('my/applications/', views.my_applications, name='my_applications'),
    path('jobs/<int:pk>/mark-employed/', views.mark_employed, name='mark_employed'),  # our test URL
    path('jobcbv/', JobListView.as_view(), name='job_list'),
    path('job/addcbv/', JobCreateView.as_view(), name='job_add_cbv'),

]