from django.shortcuts import render
from django.http import HttpResponse

def show_form(request):
    return(HttpResponse("<h1>formularz</h1>"))
