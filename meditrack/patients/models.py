from django.db import models
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.specialization})"
    

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient.name} with Dr. {self.doctor.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"


