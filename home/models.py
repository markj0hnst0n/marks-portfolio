from django.db import models
from django.db.models import query

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField(blank=False)
	query = models.TextField(max_length=300)