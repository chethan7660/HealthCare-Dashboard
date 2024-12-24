from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Patient, Doctor
from .forms import PatientForm, DoctorForm
import csv
from django.http import HttpResponse


def dashboard(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'dashboard.html', {'patients': patients, 'doctors': doctors})

def login_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        # Replace 'admin123' with your desired password
        if password == 'dashboard':
            request.session['is_authenticated'] = True
            return redirect('dashboard')  # Redirect to the dashboard if the password is correct
        elif password == 'doctors':
            request.session['is_authenticated'] = True
            return redirect('doctor_page')
        elif password == 'patients':
            request.session['is_authenticated'] = True
            return redirect('patient_page')
        else:
            messages.error(request, 'Invalid password. Please try again.')
    return render(request, 'login.html')

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PatientForm()
    return render(request, 'add_entry.html', {'form': form, 'type': 'Patient'})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DoctorForm()
    return render(request, 'add_entry.html', {'form': form, 'type': 'Doctor'})

def admin_dashboard(request):
    """View to display both patients and doctors for the admin."""
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'admin_dashboard.html', {'patients': patients, 'doctors': doctors})

def patient_page(request):
    """View to display only patients."""
    patients = Patient.objects.all()
    return render(request, 'patient_page.html', {'patients': patients})

def doctor_page(request):
    """View to display only doctors."""
    doctors = Doctor.objects.all()
    return render(request, 'doctor_page.html', {'doctors': doctors})

def export_to_csv(request):
    # Prepare the HttpResponse
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="healthcare_data.csv"'

    writer = csv.writer(response)
    # Write the header
    writer.writerow(['Entity', 'Name', 'Disease', 'Age', 'Date of Admission'])

    # Add patient data
    patients = Patient.objects.all()
    for patient in patients:
        writer.writerow(['Patient', patient.name, patient.disease, patient.age, patient.date_admitted])

    # Add doctor data
    doctors = Doctor.objects.all()
    for doctor in doctors:
        writer.writerow(['Doctor', doctor.name, doctor.specialization, doctor.experience, doctor.patients.count()])

    return response