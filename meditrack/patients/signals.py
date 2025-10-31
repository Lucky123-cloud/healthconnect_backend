from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Appointment, Patient, Doctor


@receiver(post_save, sender=Appointment)
def notify_appointment(sender, instance, created, **kwargs):
    if created:
        print(f"Appointment booked for {instance.patient.name} with Dr. {instance.doctor.name} on {instance.date}. ")