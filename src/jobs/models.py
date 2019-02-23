from django.db import models

# Create your models here.

class Job(models.Model):
	title = models.CharField(verbose_name='Job Title', max_length=150)
	description = models.TextField(verbose_name='Job Description')
	count = models.IntegerField(verbose_name='Number of people to hire', default= 1)
	expire = models.DateField(verbose_name='Last application date')


	def get_absolute_url(self):
		return "/{}/".format(self.pk)

class Application(models.Model):
	name = models.CharField(verbose_name='Name', max_length=150)
	email = models.EmailField(verbose_name='Email')
	phone = models.IntegerField(verbose_name='Phone number')
	address = models.CharField(verbose_name='Address', max_length=250)
	thoughts = models.TextField(verbose_name='Thoughts on job')
	resume = models.FileField(upload_to = "static/files/")
	job = models.ForeignKey(Job, on_delete = models.CASCADE)

	def get_absolute_url(self):
		return "/"