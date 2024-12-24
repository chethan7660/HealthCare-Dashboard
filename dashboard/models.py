from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=255)
    date_admitted = models.DateField()
   
    photo = models.ImageField(upload_to='patient_photos/', blank=True, null=True)  # Added photo field
    doctors = models.ManyToManyField('Doctor', related_name='patients', blank=True)  # Many-to-many relationship with Doctor
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    experience = models.IntegerField(default=0)  # New experience field
    photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)  # Added photo field
    

    def __str__(self):
        return self.name
