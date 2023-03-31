from django.shortcuts import render
from .forms import UserForm, ResetPasswordForm
from .models import User

def show_form(request):
    form=UserForm(request.POST or None)
    object=User.objects.all().values()
    selected_option=request.POST.get('permision')
    # user=User.objects.create(email="wotstyle@onet.pl", password="Kiribati123#")
    print(object)
    if form.is_valid():
        for item in object:
            if selected_option=="user":
                if item['email']==form.cleaned_data['email'] and item['password']==form.cleaned_data['password'] and item['isAdmin']==False:
                    form=UserForm()
                    print("zalogowano")
                    # tu będzie przekierowanie do panelu pracownika
                    break
            elif selected_option=="admin":
                if item['email']==form.cleaned_data['email'] and item['password']==form.cleaned_data['password'] and item['isAdmin']==True:
                    form=UserForm()
                    print("zalogowano")
                    # tu będzie przekierowanie do panelu admina
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
