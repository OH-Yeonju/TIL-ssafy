from django.urls import path
from . import views

urlpatterns = [
    path('certifications1/', views.certifications1),
    path('certifications2/', views.certifications2),
    path('certifications3/', views.certifications3),
]
