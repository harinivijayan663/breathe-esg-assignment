from django.db import models

class UploadedData(models.Model):
    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name