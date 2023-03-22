from django.shortcuts import render
from .forms import ResetPasswordForm

def show_form(request):
    form=ResetPasswordForm()
    if form.is_valid():
        form.save()
        form=ResetPasswordForm()
    context={
        'form': form
    }
    return(render(request, "template.html", context))
