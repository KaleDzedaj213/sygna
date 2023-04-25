from django.shortcuts import render
from adminpanel.models import Client

def show_form(request):
    clients=Client.objects.all()
    context = {"clients": clients}
    return render(request, "template4.html", context)
