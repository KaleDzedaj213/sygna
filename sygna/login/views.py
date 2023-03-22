from django.shortcuts import render
from .forms import UserForm

def show_form(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=UserForm()
    context={
        'form': form
    }
    return(render(request, "template.html", context))
