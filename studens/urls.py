from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("add/", views.add, name="add"),
	path("edit/<int:id>/", views.edit, name="edit"),
	path("delete/<int:id>/", views.delete, name="delete"),
	path("add_Project/", views.add_Project, name="add_Project"),
	path("add_Job_Type/", views.add_Job_Type, name="add_Job_Type"),
	path("add_Stages/", views.add_Stages, name="add_Stages"),
	path("search_Mission/", views.search_Mission, name="search_Mission"),
	path('testing/', views.testing, name='testing'),

]