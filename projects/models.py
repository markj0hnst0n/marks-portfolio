from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(blank=True)
	short_description = models.TextField()
	verbose_description = models.TextField()