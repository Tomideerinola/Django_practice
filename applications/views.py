from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm
from django.contrib import messages

# Create your views here.
def job_list(request):
    jobs = JobApplication.objects.all()  # get all jobs from the database
    return render(request, 'applications/job_list.html', {'jobs': jobs})


def home(request):
    return render(request, 'applications/home.html')


def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()

    return render(request, 'applications/add_job.html', {'form': form})



# --- EDIT JOB ---
def edit_job(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully!")
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'applications/edit_job.html', {'form': form, 'job': job})

# --- DELETE JOB ---
def delete_job(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job deleted successfully!")
        return redirect('job_list')
    return render(request, 'applications/delete_job.html', {'job': job})
