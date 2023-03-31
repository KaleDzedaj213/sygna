from django.shortcuts import render
from .forms import CreateForm

def show_adminpanel(request):
	form=CreateForm()
	context={
	"form": form
	}
	return(render(request, "template3.html", context))