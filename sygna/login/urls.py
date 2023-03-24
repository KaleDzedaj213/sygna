from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_form, name='show_form'),
    path('passwordReset/', views.show_resetForm, name='show_resetForm')
]
