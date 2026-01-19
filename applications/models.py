from django.db import models

# Create your models here.
class JobApplication(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.role}"