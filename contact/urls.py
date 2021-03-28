from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_us, name="contact_us"),
    path('contact-success/', views.contact_success, name="contact_success"),
]