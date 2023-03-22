from django import forms


from django import forms

class ResetPasswordForm(forms.Form):
    email=forms.CharField(label='email', max_length=30)