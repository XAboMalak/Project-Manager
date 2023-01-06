from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from . models import Projects, Mission, Stages, Job_Type
from . forms import MissionForm, ProjectsForm, StagesForm, Job_TypeForm
import datetime

def index(request):
	return render(request, "studens/index.html", {
		"Mission": Mission.objects.order_by("-finish_Date")[:10],
		})

def search_Mission(request):
	x = datetime.date.today().month
	y = datetime.date.today().year
	input_month = x if ((request.POST.get("input_month", False)) == 0) else  request.POST.get("input_month", False)
	input_year = y if ((request.POST.get("input_year", False))== 0) else request.POST.get("input_year", False)

	return render(request, "studens/search_Mission.html", {
		"searched": Mission.objects.filter(finish_Date__year=input_year).filter(finish_Date__month=input_month),

		})

def add(request):
	if request.method == "POST":
		form = MissionForm(request.POST)
		if form.is_valid():
			new_project_Name = form.cleaned_data["project_Name"]
			new_project_Stage = form.cleaned_data["project_Stage"]
			new_project_Job_Type = form.cleaned_data["project_Job_Type"]
			new_quantity = form.cleaned_data["quantity"]
			new_unit = form.cleaned_data["unit"]
			new_start_Date = form.cleaned_data["start_Date"]
			new_finish_Date = form.cleaned_data["finish_Date"]
			new_number_Of_Days = form.cleaned_data["number_Of_Days"]
			new_number_Of_Hours = form.cleaned_data["number_Of_Hours"]
			new_nots = form.cleaned_data["nots"]

			new_missiom = Mission(
				project_Name = new_project_Name,
				project_Stage = new_project_Stage,
				project_Job_Type = new_project_Job_Type,
				quantity = new_quantity,
				unit = new_unit,
				start_Date = new_start_Date,
				finish_Date = new_finish_Date,
				number_Of_Days = new_number_Of_Days,
				number_Of_Hours = new_number_Of_Hours,
				nots = new_nots
				)

			new_missiom.save()
			return render(request, "studens/add.html", {
				"form": MissionForm(),
				"success": True
				})
	else:
		form = MissionForm()
	return render(request, "studens/add.html", {
		"form": MissionForm(),
		
		})

def edit(request, id):
	if request.method == "POST":
		mission = Mission.objects.get(pk=id)
		form = MissionForm(request.POST, instance=mission)
		if form.is_valid():
			form.save()
			return render(request, "studens/edit.html", {
				"form": form,
				"success": True
				})
	else:
		mission = Mission.objects.get(pk=id)
		form = MissionForm( instance=mission)
	return render(request, "studens/edit.html", {
		"form": form
		})

def delete(request, id):
	if request.method == "POST":
		mission = Mission.objects.get(pk=id)
		mission.delete()
	return HttpResponseRedirect(reverse("index"))

# def getYears():
# 	current_date = datetime.date.today()
# 	y = current_date.year
# 	years = [y-i for i in range(5)]
# 	return years

# def getMonthes():
# 	monthes = [i for i in range(1,13)]
# 	return monthes


def add_Project(request):
	if request.method == "POST":
		form = ProjectsForm(request.POST)
		if form.is_valid():
			new_name = form.cleaned_data["name"]
			new_date = form.cleaned_data["date"]
			new_nots = form.cleaned_data["nots"]

			new_projects = Projects(
				name = new_name,
				date = new_date,
				nots = new_nots,
				)

			new_projects.save()
			return render(request, "studens/add_Project.html", {
				"form": ProjectsForm(),
				"success": True
				})
	else:
		form = ProjectsForm()
	return render(request, "studens/add_Project.html", {
		"form": ProjectsForm()
		})

def add_Stages(request):
	if request.method == "POST":
		form = StagesForm(request.POST)
		if form.is_valid():
			new_name = form.cleaned_data["name"]
			new_Stages = Stages(
				name = new_name,
				)
			new_Stages.save()
			return render(request, "studens/add_Stages.html", {
				"form": StagesForm(),
				"success": True
				})
	else:
		form = StagesForm()
	return render(request, "studens/add_Stages.html", {
		"form": StagesForm()
		})

def add_Job_Type(request):
	if request.method == "POST":
		form = Job_TypeForm(request.POST)
		if form.is_valid():
			new_name = form.cleaned_data["name"]
			new_m3_day = form.cleaned_data["m3_day"]

			new_Job_Type = Job_Type(
				name = new_name,
				m3_day = new_m3_day,
				)
			new_Job_Type.save()
			return render(request, "studens/add_Job_Type.html", {
				"form": Job_TypeForm(),
				"success": True
				})
	else:
		form = Job_TypeForm()
	return render(request, "studens/add_Job_Type.html", {
		"form": Job_TypeForm()
		})

def testing(request):
	x = datetime.date.today().month
	y = datetime.date.today().year
	ye= [datetime.date.today().year -i for i in range(5)]
	input_month = x if ((request.POST.get("input_month", False)) == 0) else  request.POST.get("input_month", False)
	input_year = y if (request.POST.get("input_year", False))== 0 else request.POST.get("input_year", False)
	return render(request, "studens/testing.html", {
		'fruits': ['Apple', 'Banana', 'Cherry'],
		"input_month": input_month,
		"input_year": input_year,
		"ye": ye,


		})