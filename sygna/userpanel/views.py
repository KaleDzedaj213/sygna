from django.shortcuts import render
<<<<<<< HEAD
from adminpanel.models import Client

def show_form(request):
    clients=Client.objects.all()
    context = {"clients": clients}
    return render(request, "template4.html", context)
=======

# Create your views here.
>>>>>>> 283ffdb85b50d13598a9a7b511fd083e76c38cd5
