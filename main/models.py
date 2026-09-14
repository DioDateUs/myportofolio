import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, help_text="Posisi / Role")
    organization = models.CharField(max_length=255, blank=True, null=True, help_text="Nama Organisasi / Perusahaan")
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    photo = models.URLField(blank=True, null=True, help_text="Masukkan link URL foto/logo di sini")
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None



