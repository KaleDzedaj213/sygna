from django.shortcuts import render
<<<<<<< HEAD
from .forms import SearchForm, CreateForm, UpdateForm, DeleteForm, SearchClientForm, DeleteClientForm, UpdateClientForm, CreateClientForm
from .models import Client
=======
from .forms import SearchForm, CreateForm, UpdateForm
>>>>>>> 283ffdb85b50d13598a9a7b511fd083e76c38cd5
from login.models import User

def show_adminpanel(request):
    form = SearchForm()
    form2 = CreateForm()
    form3 = UpdateForm()
<<<<<<< HEAD
    form4 = DeleteForm()
    cform = SearchClientForm()
    cform2 = CreateClientForm()
    cform3 = UpdateClientForm()
    cform4 = DeleteClientForm()
    users = User.objects.all()
    clients = Client.objects.all()
    displayItems = []
    displayCustomers = []
=======
    users = User.objects.all()
    displayItems = []
>>>>>>> 283ffdb85b50d13598a9a7b511fd083e76c38cd5

    if request.method == 'POST':
        form = SearchForm(request.POST)
        form2 = CreateForm(request.POST)
<<<<<<< HEAD
        form3 = UpdateForm(request.POST)
        form4 = DeleteForm(request.POST)
        cform = SearchClientForm(request.POST)
        cform2 = CreateClientForm(request.POST)
        cform3 = UpdateClientForm(request.POST)
        cform4 = DeleteClientForm(request.POST)


        # obsługa formularzy użytkowników
=======

        if form3.is_valid():
            selected_values = form3.cleaned_data['select_Field']
        if form2.is_valid():
            user = User.objects.create(email=form2.cleaned_data['email'], password=form2.cleaned_data['password'], permission=form2.cleaned_data['permission'])
            form2 = CreateForm()
            form = SearchForm()
            form3 = UpdateForm()
>>>>>>> 283ffdb85b50d13598a9a7b511fd083e76c38cd5
        if form.is_valid():
            pattern = form.cleaned_data['email']
            for user in users:
                if pattern in user.email:
                    displayItems.append(f"{user.email}, {user.permission}")
<<<<<<< HEAD
        if form2.is_valid():
            user = User.objects.create(email=form2.cleaned_data['email'], password=form2.cleaned_data['password'], permission=form2.cleaned_data['permission'])
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
                strName=str(client.name)
                if pattern in strName:
                    displayCustomers.append(f"{client.name}, {client.nip}")
        if cform2.is_valid():
            client = Client.objects.create(nip=cform2.cleaned_data['nip'], name=cform2.cleaned_data['name'], payment=cform2.cleaned_data['payment'])
        if cform3.is_valid():
            selected_value = cform3.cleaned_data['select_Field']
            record = Client.objects.filter(name=selected_value).first()
            if record:
                record.delete()
        if cform4.is_valid():
            selected_value = cform4.cleaned_data['select_Field']
            print(clients)
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
=======
            form3 = UpdateForm()
            form2 = CreateForm()
            form = SearchForm()
>>>>>>> 283ffdb85b50d13598a9a7b511fd083e76c38cd5



    if not displayItems:
        message = "No results found."
    else:
        message = None

    context = {
        "form": form,
		"form2": form2,
		"form3": form3,
<<<<<<< HEAD
        "form4": form4,
        "cform": cform,
        "cform2": cform2,
        "cform3": cform3,
        "cform4": cform4,
        "object": displayItems,
        "object2": displayCustomers,
=======
        "object": displayItems,
>>>>>>> 283ffdb85b50d13598a9a7b511fd083e76c38cd5
        "message": message,
    }
    return render(request, "template3.html", context)