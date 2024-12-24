
from django.contrib import admin
from django.urls import path
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('patients/', views.patient_page, name='patient_page'),
    path('doctors/', views.doctor_page, name='doctor_page'),
    path('', views.login_view, name='login'),
    path('export-csv/', views.export_to_csv, name='export_csv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
