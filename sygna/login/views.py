from django.shortcuts import render
from .forms import UserForm, ResetPasswordForm
from .models import User

def show_form(request):
    form=UserForm(request.POST or None)
    object=User.objects.all().values()
    if form.is_valid():
        for item in object:
            if item['email']==form.cleaned_data['email'] and item['password']==form.cleaned_data['password']:
                form=UserForm()
                # tu będzie przekierowanie do panelu pracownika
                break
    context={
        'form': form
    }
    return(render(request, "template.html", context))


def show_resetForm(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                print("wysyłam maila")
                # w tym wysyłany jest mail
            form = ResetPasswordForm()
    else:
        form = ResetPasswordForm()
        
    context = {'form': form}
    return render(request, "template2.html", context)
