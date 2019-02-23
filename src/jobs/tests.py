from django.test import TestCase
from .models import *
from .views import *
from .forms import *
import datetime
# Create your tests here.

class JobTest(TestCase):
	def __init__(self, *args, **kwargs):
		print("running job test")
		self.j1 = Job(title="CEO", description= "CEO for company", count= 1, expire= datetime.datetime.today())
		self.j2 = Job(title="Staff", description= "Staff for company", count= 1, expire= datetime.datetime.today())
		self.j1.save()
		self.j2.save()

	def test_jobs(self):
		print("Jobs equal")
		self.assertEqual(Job.objects.get(title="CEO"), self.j1)


class JobFormTest(TestCase):
	def __init__(self, *args, **kwargs):
		print("testin JobForm")
		

	def test_validation(self):
		form = JobForm(data={"title": "ceo", "description": "example",
			"count": 2, "expire": "12/03/2018"})
		self.assertTrue(form.is_valid())
		print("......................... OK!")

class ApplicationFormTest(TestCase):
	def __init__(self, *args, **kwargs):
		print("Testing ApplicationForm")

	def test_form_validation(self):
		form = ApplicationForm(data= {"name": "Name", "email": "django@django.com", "phone": "0555 555 5555", "address": "dgsdgsgs", "thoughts": "dsfsfs", "job":1})
		self.assertFalse(form.is_valid())
		print("........................... OK!")