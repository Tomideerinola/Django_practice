from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    applied_date = models.DateField(auto_now_add=True)


    class Meta:
        permissions = [
            ("can_mark_employed", "Can mark job as employed"),
            ("can_approve_leave", "Can approve leave status"),
        ]

    def __str__(self):
        return f"{self.company} - {self.role}"
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()

    def __str__(self):
        return self.title