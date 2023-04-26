from django import forms
from login.models import User
from .models import Client

# users

class SearchForm(forms.Form):
	email=forms.CharField()
	
class CreateForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    permission = forms.CharField(label='Uprawnienie')

class UpdateForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=User.objects.all(), label="Wybierz użytkownika")
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    permission = forms.CharField(label='Uprawnienie')

class DeleteForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=User.objects.all(), label="Wybierz użytkownika")

# clients

class SearchClientForm(forms.Form):
	name=forms.CharField()
	
class CreateClientForm(forms.Form):
    nip = forms.CharField(label='NIP')
    name = forms.CharField(label='Nazwa')
    payment = forms.CharField(label='Metoda płatności')

class UpdateClientForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=Client.objects.all(), label="Wybierz klienta")
    nip = forms.CharField(label='NIP')
    name = forms.CharField(label='Nazwa')
    payment = forms.CharField(label='Metoda płatności')

class DeleteClientForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=Client.objects.all(), label="Wybierz klienta")