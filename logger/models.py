from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Repository(models.Model):
    BUILD_STATUS_CHOICES = [
        ('success', 'Success'),
        ('failure', 'Failure'),
        ('error', 'Error'),
        ('pending', 'Pending'),
    ]

    DEPLOYMENT_STATUS_CHOICES = [
        ('success', 'Success'),
        ('failure', 'Failure'),
        ('in_progress', 'In Progress'),
        ('queued', 'Queued'),
        ('paused', 'Paused'),
    ]

    name = models.CharField(max_length=255, unique=True)
    build_status = models.CharField(max_length=50, choices=BUILD_STATUS_CHOICES)
    deployment_status = models.CharField(max_length=50, choices=DEPLOYMENT_STATUS_CHOICES)
    version_number = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
