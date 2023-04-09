from django.shortcuts import render
from .forms import UserForm, ResetPasswordForm
from .models import User
from django.shortcuts import redirect

def show_form(request):
    form=UserForm(request.POST or None)
    object=User.objects.all().values()
    selected_option=request.POST.get('permision')
    # user=User.objects.create(email="tak@onet.pl", password="Haslo1#", permission="admin")
    print(object)
    if form.is_valid():
        for item in object:
            if selected_option=="user":
                if item['email']==form.cleaned_data['email'] and item['password']==form.cleaned_data['password'] and item['permission']=="user":
                    form=UserForm()
                    print("zalogowano")
                    # tu będzie przekierowanie do panelu pracownika
                    break
            elif selected_option=="admin":
                if item['email']==form.cleaned_data['email'] and item['password']==form.cleaned_data['password'] and item['permission']=="admin":
                    form=UserForm()
                    print("zalogowano")
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
