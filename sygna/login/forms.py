from django import forms

class UserForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autocomplete': 'off'}))