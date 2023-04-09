from django import forms
from login.models import User


class SearchForm(forms.Form):
	email=forms.CharField()
	
class CreateForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    permission = forms.CharField(label='Uprawnienie')

class UpdateForm(forms.Form):
    select_Field = forms.ModelChoiceField(queryset=User.objects.all())
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    permission = forms.CharField(label='Uprawnienie')
