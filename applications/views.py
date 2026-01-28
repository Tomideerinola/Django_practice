from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from .forms import JobApplicationForm, BookForm
from django.contrib import messages

# Create your views here.
@login_required
def job_list(request):
    jobs = JobApplication.objects.all()  # get all jobs from the database
    return render(request, 'applications/job_list.html', {'jobs': jobs})


def home(request):
    return render(request, 'applications/home.html')


@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, "applications/list.html", {"applications": applications})



def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
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


def job_detail(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    return render(request, 'applications/job_detail.html', {'job': job})


def create_book_view(request):
    # 1. Did the user click 'Submit'? (POST request)
    if request.method == 'POST':
        form = BookForm(request.POST) # Fill the form with the user's data
        if form.is_valid():           # Django's built-in security & logic check
            form.save()               # Saves directly to the Database!
            return redirect('success') 
            
    # 2. User is just visiting the page (GET request)
    else:
        form = BookForm()             # Provide a blank form
        
    return render(request, 'applications/create_book.html', {'form': form})

def success(request):
    return render(request, 'applications/success.html')
