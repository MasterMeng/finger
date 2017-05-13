from django import forms
from django.db import models
from blackIP.models import *

class AddrForm(forms.Form):
    addr = forms.CharField()

    class Meta:
        model = Address
