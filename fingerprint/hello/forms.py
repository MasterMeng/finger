from django import forms
from django.db import models
from hello.models import *


class FingerForm(forms.Form):
    finger = forms.CharField()
    os = forms.CharField()
    os_ver = forms.CharField()
    browser = forms.CharField()
    browser_ver = forms.CharField()
    CPU = forms.CharField()
    device = forms.CharField()

    class Meta:
        model = Finger