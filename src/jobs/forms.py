from django.forms import ModelForm
from django.forms.widgets import  Textarea, FileInput, TextInput, DateInput

from .models import Job, Application

class JobForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(JobForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Job
		fields = ("title", "description", "count", "expire")
		widgets = {
			'description': Textarea(attrs={'class':"form-control"}),
			"expire": DateInput(attrs= {"class": "form-control date", "data-mask": "00/00/0000"})
		}


class ApplicationForm(ModelForm):
	class Meta:
		model = Application
		fields = ("name", "email", "phone", "address", "thoughts", "resume")
		widget = {
			"thoughts": Textarea(attrs={"class": "form-control date"}),
			"resume": FileInput(attrs={"class": "form-control-file"}),
			"phone" : TextInput(attrs={"class": "form-control phone", "data-mask": "0000 000 00 00"})
		}