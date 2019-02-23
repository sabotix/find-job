from django.urls import path
from .views import *

urlpatterns = [
    path('', JobList.as_view(), name="joblist"),
    path('add/', JobCreate.as_view(), name= "addjob"),
    path('<int:pk>/', JobDetail.as_view(), name= "jobdetail"),
    path('<int:pk>/delete', JobDelete.as_view(), name= "deletejob"),
    path("<int:pk>/apply", ApplicationCreate.as_view(), name= "apply"),
    path("application/<int:pk>", ApplicationDetail.as_view(), name= "applydetail"),
]