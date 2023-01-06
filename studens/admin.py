from django.contrib import admin
from . models import Projects, Mission, Stages, Job_Type
# Register your models here.

myModels =[Projects, Mission, Stages, Job_Type]
admin.site.register(myModels)