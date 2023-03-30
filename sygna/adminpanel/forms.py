from django import forms

class CreateForm(forms.Form):
	name=forms.CharField()
	last_name=forms.CharField()
	email=forms.CharField()
	permision=forms.CharField()
	