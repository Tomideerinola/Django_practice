from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications'



    def ready(self):
        # Import signals here so Django knows about them
        import applications.signals  # noqa