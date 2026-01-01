from django.db import models

class Application(models.Model):
    PROGRAM_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('AI', 'Artificial Intelligence'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    program = models.CharField(max_length=2, choices=PROGRAM_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
