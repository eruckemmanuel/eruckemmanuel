from django.contrib import admin

from home.models import ContactMessage, Project

admin.site.register(ContactMessage)
admin.site.register(Project)