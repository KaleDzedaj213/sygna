from django.shortcuts import render
from .forms import SearchForm, CreateForm, UpdateForm
from login.models import User

def show_adminpanel(request):
    form = SearchForm()
    form2 = CreateForm()
    form3 = UpdateForm()
    users = User.objects.all()
    displayItems = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        form2 = CreateForm(request.POST)

        if form3.is_valid():
            selected_values = form3.cleaned_data['select_Field']
        if form2.is_valid():
            user = User.objects.create(email=form2.cleaned_data['email'], password=form2.cleaned_data['password'], permission=form2.cleaned_data['permission'])
            form2 = CreateForm()
            form = SearchForm()
            form3 = UpdateForm()
        if form.is_valid():
            pattern = form.cleaned_data['email']
            for user in users:
                if pattern in user.email:
                    displayItems.append(f"{user.email}, {user.permission}")
            form3 = UpdateForm()
            form2 = CreateForm()
            form = SearchForm()



    if not displayItems:
        message = "No results found."
    else:
        message = None

    context = {
        "form": form,
		"form2": form2,
		"form3": form3,
        "object": displayItems,
        "message": message,
    }
    return render(request, "template3.html", context)
