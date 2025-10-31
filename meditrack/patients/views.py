from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment
from django.utils import timezone

def home(request):
    return render(request, 'patients/home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients.html', {'patients': patients})

def appointments(request):
    doctors = Doctor.objects.filter(available=True)
    patients = Patient.objects.all()
    appointments = Appointment.objects.select_related('patient', 'doctor')

    if request.method == "POST":
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=timezone.now(),
            confirmed=True
        )
        return redirect('appointments')

    return render(request, 'patients/appointments.html', {
        'doctors': doctors,
        'patients': patients,
        'appointments': appointments
    })
