from django.contrib import admin
from  .models import *

# Register your models here.

class JobAdmin(admin.ModelAdmin):
	list_display = ["title", "description", "count", "expire"]
	ordering = ["-pk"]

class ApplicationsAdmin(admin.ModelAdmin):
	list_display = ["name", "email", "phone", "address", "thoughts", "resume", "job"]

