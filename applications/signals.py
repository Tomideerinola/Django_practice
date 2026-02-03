from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobApplication

@receiver(post_save, sender=JobApplication)
def notify_on_job_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New job added: {instance.company} - {instance.role}")