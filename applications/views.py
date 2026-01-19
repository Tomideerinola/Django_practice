from django.shortcuts import render
from .models import JobApplication

# Create your views here.
def job_list(request):
    jobs = JobApplication.objects.all()  # get all jobs from the database
    return render(request, 'applications/job_list.html', {'jobs': jobs})

