from django.db import models
from datetime import date

# Create your models here.
class Projects(models.Model):
	name = models.CharField(max_length=100, unique=True)
	date = models.DateField(default=date.today)
	nots = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name

class Stages(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name
	
class Job_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)
	m3_day = models.FloatField()

	def __str__(self):
		return self.name
	

class Mission(models.Model):
	unit_choice = (('1', 'متر مكعب'),('2', 'طابوقة'),('3', 'متر مربع'),('4', 'متر طولي'),)
	project_Name = models.ForeignKey(Projects, on_delete=models.CASCADE)
	project_Stage = models.ForeignKey(Stages, on_delete=models.CASCADE)
	project_Job_Type = models.ForeignKey(Job_Type, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	unit = models.CharField(max_length=1, choices=unit_choice)
	start_Date = models.DateField(default=date.today)
	finish_Date = models.DateField(default=date.today)
	number_Of_Days = models.IntegerField()
	number_Of_Hours = models.IntegerField()
	nots = models.TextField(null=True, blank=True)


	@property
	def start_Date_format(self):
		return self.start_Date.strftime("%Y/%m/%d")

	@property
	def finish_Date_format(self):
		return self.finish_Date.strftime("%Y/%m/%d")

	@property
	def production_Ratio(self):
		Hours = self.number_Of_Hours
		Q = self.quantity
		M3 = self.project_Job_Type.m3_day
		P_Ratio = (Q/(M3/2)*(8/Hours))*100
		return f"{P_Ratio:.0f} %"

