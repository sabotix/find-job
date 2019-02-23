from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, DeleteView
from django.contrib.auth.mixins import *
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Job, Application
from .forms import JobForm, ApplicationForm
# Create your views here.

class JobList(ListView):
	model = Job
	template_name = "jobs/list.html"
	context_object_name = "jobs"
	paginate_by = 10
	queryset = Job.objects.all().order_by("-pk")


class JobDetail(DetailView):
	model = Job
	template_name = "jobs/detail.html"
	context_object_name = "job"

	def get(self, req, pk, *args, **kwargs):
		job = Job.objects.get(pk=pk)
		applicant = Application.objects.filter(job=job)

		return render(req, self.template_name, {"job": job, "applicants": applicant})


class JobCreate(LoginRequiredMixin, CreateView):
	model = Job
	template_name = "jobs/create.html"
	form_class = JobForm
	#fields = ("title", "description", "count", "expire")

	def form_valid(self, form):
		print(form.is_valid())
		return super().form_valid(form)


class JobDelete(LoginRequiredMixin, DeleteView):
	model = Job
	template_name = "jobs/delete.html"
	success_url = reverse_lazy("joblist")


class ApplicationList(LoginRequiredMixin, ListView):
	model = Application
	#template_name = "applications/list.html"
	context_object_name = "jobs"

	def get(self, req, *args, **kwargs):
		qs = self.model.objects.all()
		return JsonResponse(serialize("json", qs), safe = False)


class ApplicationCreate(CreateView):
	model = Application
	template_name = "applications/create.html"
	form_class = ApplicationForm

	def form_valid(self, form):
		form.instance.job = Job.objects.get(pk=self.kwargs["pk"])
		print(form.is_valid())
		return super().form_valid(form)



class ApplicationDetail(LoginRequiredMixin, DetailView):
	model = Application
	template_name = "applications/detail.html"
	context_object_name = "app"
