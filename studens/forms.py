from django import forms
from .models import Projects, Mission, Stages, Job_Type
import datetime

class MissionForm(forms.ModelForm):
	class Meta:
		model = Mission
		fields = ("project_Name", "project_Stage", "project_Job_Type", "quantity", "unit", "start_Date", "finish_Date", "number_Of_Days", "number_Of_Hours", "nots")
		labels = {
			"project_Name" : "اسم المشروع",
			"project_Stage" : "المرحلة المنفذة", 
			"project_Job_Type" : "نوع العمل المنفذ", 
			"quantity" : "الكمية", 
			"unit" : "الوحدة", 
			"start_Date" : "تاريخ البداية", 
			"finish_Date" : "تاريخ الانتهاء", 
			"number_Of_Days" : "عدد الايام", 
			"number_Of_Hours" : "عدد الساعات", 
			"nots" : "ملاحظات"
		}

		widgets = {
			"project_Name" : forms.Select(attrs={"class": "form-control"}),
			"project_Stage" : forms.Select(attrs={"class": "form-control"}),
			"project_Job_Type" : forms.Select(attrs={"class": "form-control"}),
			"quantity" : forms.NumberInput(attrs={"class": "form-control"}), 
			"unit" : forms.Select(attrs={"class": "form-control"}), 
			"start_Date" : forms.SelectDateWidget(attrs={"class": "form-control "},years=[datetime.date.today().year-i for i in range(5)]), 
			"finish_Date" : forms.SelectDateWidget(attrs={"class": "form-control "},years=[datetime.date.today().year-i for i in range(5)]),
			"number_Of_Days" : forms.NumberInput(attrs={"class": "form-control"}), 
			"number_Of_Hours" : forms.NumberInput(attrs={"class": "form-control"}), 
			"nots" : forms.Textarea(attrs={"class": "form-control"})
		}

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Projects
		fields = ("name", "date", "nots")
		labels = {
			"name" : "إسم المشروع",
			"date" : "تاريخ الاستلام", 
			"nots" : "ملاحظات"
		}

		widgets = {
			"name" : forms.TextInput(attrs={"class": "form-control"}),
			"date" : forms.SelectDateWidget(attrs={"class": "form-control "},years=[datetime.date.today().year-i for i in range(5)]),
			"nots" : forms.Textarea(attrs={"class": "form-control"})
		}

class StagesForm(forms.ModelForm):
	class Meta:
		model = Stages
		fields = ("name", )
		labels = {
			"name" : "اسم المرحلة",
		}

		widgets = {
			"name" : forms.TextInput(attrs={"class": "form-control"}),

		}


class Job_TypeForm(forms.ModelForm):
	class Meta:
		model = Job_Type
		fields = ("name", "m3_day")
		labels = {
			"name" : "اسم العمل المنفذ",
			"m3_day" : "معدل الانجاز في اليوم", 
		}

		widgets = {
			"name" : forms.TextInput(attrs={"class": "form-control"}),
			"m3_day" : forms.NumberInput(attrs={"class": "form-control"})
		}