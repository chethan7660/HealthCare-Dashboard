from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Patient, Doctor

# Customizing the admin site header and title
admin.site.site_header = "ADMIN"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to the Admin Dashboard"

# Patient Admin
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'disease', 'date_admitted')
    search_fields = ('name', 'disease')  # Adding search functionality
    list_filter = ('disease', 'date_admitted')  # Filters for easy navigation

# Doctor Admin
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'contact')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)

# Debugging logout issue: Admin logs session activities
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'expire_date')
