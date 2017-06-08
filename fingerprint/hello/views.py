from django.shortcuts import render
from .forms import FingerForm

# Create your views here.


def home(request):
	form = FingerForm()
	return render(request,'home.html',{'form':form})