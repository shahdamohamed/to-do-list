from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES= [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    title=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    complete=models.BooleanField(default=False)
    priority=models.CharField(max_length=7, choices=PRIORITY_CHOICES, default='Meduim')
    finished_date=models.DateField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title