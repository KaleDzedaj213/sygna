from django.shortcuts import render
from .forms import SearchForm, CreateForm, UpdateForm, DeleteForm, SearchClientForm, DeleteClientForm, UpdateClientForm, CreateClientForm
from .models import Client
from login.models import User
import random

def show_adminpanel(request):
    form = SearchForm()
    form2 = CreateForm()
    form3 = UpdateForm()
    form4 = DeleteForm()
    cform = SearchClientForm()
    cform2 = CreateClientForm()
    cform3 = UpdateClientForm()
    cform4 = DeleteClientForm()
    displayItems = []
    displayCustomers = []
    message = ""

    if request.method == 'POST':
        form = SearchForm(request.POST)
        form2 = CreateForm(request.POST)
        form3 = UpdateForm(request.POST)
        form4 = DeleteForm(request.POST)
        cform = SearchClientForm(request.POST)
        cform2 = CreateClientForm(request.POST)
        cform3 = UpdateClientForm(request.POST)
        cform4 = DeleteClientForm(request.POST)

        # obsługa formularzy użytkowników
        if "user_search_submit" in request.POST and form.is_valid():
            i = 0
            users = User.objects.filter(
                email__startswith=form.cleaned_data["email"]).filter(
                    name__startswith=form.cleaned_data["name"]).filter(
                        lastname__startswith=form.cleaned_data["last_name"])
            for user in users:
                displayItems.append(f"{user.id}, {user.name}, {user.lastname}, {user.email}, {user.default_password}, {user.permission}")
                i += 1
            message = f"Znalezionych użytkowników: {i}"
        if "user_create_submit" in request.POST and form2.is_valid():
            if (User.objects.filter(email=form2.cleaned_data['email']).exists()):
                message = f"Email {form2.cleaned_data['email']} jest już zajęty"
            else:
                user = User.objects.create(
                    #id=random.randint(0, 2147483646),
                    name=form2.cleaned_data["name"],
                    lastname=form2.cleaned_data["last_name"],
                    email=form2.cleaned_data['email'],
                    password=form2.cleaned_data['password'],
                    default_password=form2.cleaned_data['password'],
                    permission=form2.cleaned_data['permission'])
                message = "Dodano użytkownika"
        if "user_update_submit" in request.POST and form3.is_valid():
            user = form3.cleaned_data['select_Field']
            if form3.cleaned_data["name"] != "": user.name = form3.cleaned_data["name"]
            if form3.cleaned_data["last_name"] != "": user.lastname = form3.cleaned_data["last_name"]
            if form3.cleaned_data["email"] != "": user.email = form3.cleaned_data["email"]
            if form3.cleaned_data["password"] != "": user.password = form3.cleaned_data["password"]
            if form3.cleaned_data["default_password"] != "": user.default_password = form3.cleaned_data["default_password"]
            if form3.cleaned_data["permission"] != "": user.permission = form3.cleaned_data["permission"]
            user.save()
            message = "Zaktualizowano użytkownika"
        if "user_delete_submit" in request.POST and form4.is_valid():
            form4.cleaned_data['select_Field'].delete()
            message = "Usunięto użytkownika"

        # obsługa formularzy klientów
        if "client_search_submit" in request.POST and cform.is_valid():
            i = 0
            clients = Client.objects.filter(
                nip__startswith=cform.cleaned_data['nip']).filter(
                    company_name__startswith=cform.cleaned_data["name"])
            for client in clients:
                displayCustomers.append(f"{client.id}, {client.company_name}, {client.nip}, {client.billing_method}")
                i += 1
            message = f"Znalezionych klientów: {i}"
        if "client_create_submit" in request.POST and cform2.is_valid():
            client = Client.objects.create(
                #id=random.randint(0, 2147483646),
                nip=cform2.cleaned_data['nip'],
                company_name=cform2.cleaned_data['name'],
                billing_method=cform2.cleaned_data['payment'])
            message = "Dodano klienta"
        if "client_update_submit" in request.POST and cform3.is_valid():
            client = cform3.cleaned_data['select_Field']
            if cform3.cleaned_data["nip"] != "": client.nip = cform3.cleaned_data["nip"]
            if cform3.cleaned_data["name"] != "": client.company_name = cform3.cleaned_data["name"]
            if cform3.cleaned_data["payment"] != "": client.billing_method = cform3.cleaned_data["payment"]
            client.save()
            message = "Zakutalizowano klienta"
        if "client_delete_submit" in request.POST and cform4.is_valid():
            cform4.cleaned_data['select_Field'].delete()
            message = "Usunięto klienta"

        form = SearchForm()
        form2 = CreateForm()
        form3 = UpdateForm()
        form4 = DeleteForm()
        cform = SearchClientForm()
        cform2 = CreateClientForm()
        cform3 = UpdateClientForm()
        cform4 = DeleteClientForm()

    context = {
        "form": form,
		"form2": form2,
		"form3": form3,
        "form4": form4,
        "cform": cform,
        "cform2": cform2,
        "cform3": cform3,
        "cform4": cform4,
        "object": displayItems,
        "object2": displayCustomers,
        "message": message,
    }

    return render(request, "template3.html", context)