from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from . forms import RegisterUserForm

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("index")
			
		else:
			messages.success(request, "خطاء في تسجيل الدخول ...حاول مرة اخري")
			return redirect("login")

	else:
		return render(request,"authenticate/login.html",{

			})

def logout_view(request):
	logout(request)
	messages.success(request, "تم تسجيل الخروج")
	return redirect("index")

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password1"]
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect("index")
	else:
		form = RegisterUserForm()
	return render(request, "authenticate/register.html",{
			"form": form,
			
		})

