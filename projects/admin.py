from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'image',
		'short_description',
		'verbose_description',
		'github_link',
		'live_link',
	)
	ordering = ('name',)

admin.site.register(Project, ProjectAdmin)
