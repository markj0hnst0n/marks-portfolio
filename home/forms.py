from django import forms
from django.db import models
from django.forms import fields
from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = "__all__"