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
    users = User.objects.all()
    clients = Client.objects.all()
    displayItems = []
    displayCustomers = []

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
        if form.is_valid():
            pattern = form.cleaned_data['email']
            for user in users:
                if pattern in user.email:
                    displayItems.append(f"{user.email}, {user.permission}")
        if form2.is_valid():
            user = User.objects.create(
                id=random.randint(0, 2147483646),
                name=form2.cleaned_data["name"],
                lastname=form2.cleaned_data["last_name"],
                email=form2.cleaned_data['email'],
                default_password=form2.cleaned_data['password'],
                permission=form2.cleaned_data['permission'])
        if form3.is_valid():
            selected_value = form3.cleaned_data['select_Field']
            record = User.objects.get(email=selected_value)
        if form4.is_valid():
            selected_value = form4.cleaned_data['select_Field']
            if selected_value in users:
                User.objects.filter(email=selected_value).delete()

        # obsługa formularzy klientów
        if cform.is_valid():
            pattern = cform.cleaned_data['name']
            for client in clients:
                strName=str(client.company_name)
                if pattern in strName:
                    displayCustomers.append(f"{client.company_name}, {client.nip}")
        if cform2.is_valid():
            client = Client.objects.create(
                nip=cform2.cleaned_data['nip'],
                company_name=cform2.cleaned_data['name'],
                billing_method=cform2.cleaned_data['payment'])
        if cform3.is_valid():
            selected_value = cform3.cleaned_data['select_Field']
            record = Client.objects.filter(name=selected_value).first()
            if record:
                record.delete()
        if cform4.is_valid():
            selected_value = cform4.cleaned_data['select_Field']
            if selected_value in clients:
                Client.objects.filter(name=selected_value).delete()



        form = SearchForm()
        form2 = CreateForm()
        form3 = UpdateForm()
        form4 = DeleteForm()
        cform = SearchClientForm()
        cform2 = CreateClientForm()
        cform3 = UpdateClientForm()
        cform4 = DeleteClientForm()



    if not displayItems:
        message = "No results found."
    else:
        message = None

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
