from django import forms
from login.models import User
from .models import Client

# users

class SearchForm(forms.Form):
	email = forms.CharField(required=False)
	name = forms.CharField(label='Imię', required=False)
	last_name = forms.CharField(label='Nazwisko', required=False)
	
class CreateForm(forms.Form):
	name = forms.CharField(label='Imię')
	last_name = forms.CharField(label='Nazwisko')
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
	password = forms.CharField(label='Domyślne hasło', widget=forms.PasswordInput)
	permission = forms.ChoiceField(choices=(("1", "user"), ("2", "admin")), label='Uprawnienia')

class UpdateForm(forms.Form):
	select_Field = forms.ModelChoiceField(queryset=User.objects.all(), label="Wybierz użytkownika")
	name = forms.CharField(label='Imię', required=False)
	last_name = forms.CharField(label='Nazwisko', required=False)
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}), required=False)
	password = forms.CharField(label='Hasło', widget=forms.PasswordInput, required=False)
	default_password = forms.CharField(label='Domyślne hasło', widget=forms.PasswordInput, required=False)
	permission = forms.ChoiceField(choices=(("1", "user"), ("2", "admin")), label='Uprawnienia', required=False)

class DeleteForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=User.objects.all(), label="Wybierz użytkownika")

# clients

class SearchClientForm(forms.Form):
	nip = forms.CharField(label='NIP', required=False)
	name = forms.CharField(label='Nazwa', required=False)
	
class CreateClientForm(forms.Form):
    nip = forms.CharField(label='NIP')
    name = forms.CharField(label='Nazwa')
    payment = forms.ChoiceField(choices=(("1", "godzinowa"), ("2", "zadaniowa")), label='Metoda płatności')

class UpdateClientForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=Client.objects.all(), label="Wybierz klienta")
    nip = forms.CharField(label='NIP', required=False)
    name = forms.CharField(label='Nazwa', required=False)
    payment = forms.ChoiceField(choices=(("1", "godzinowa"), ("2", "zadaniowa")), label='Metoda płatności', required=False)

class DeleteClientForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=Client.objects.all(), label="Wybierz klienta")