from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
# from ..timeDisplay.models import timeDisplay

def index(request):
	return render(request,'loginRegister/index.html')

def create_user(request):
	context = {
		'email' : request.POST["email"],
		'first_name' : request.POST["first_name"],
		'last_name' : request.POST["last_name"],
		'password' : request.POST["password"],
		'confirm_password' : request.POST["confirm_password"],
	}

	if User.userManager.registration(context, request):
		passFlag = True
		return redirect('/loginRegister/success')
	else:
		passFlag = False
		return redirect('/')
		


def login(request):
	content = {
	'email' : request.POST["email"],
	'password' : request.POST["password"],

	}
	if User.userManager.login(content, request):
		passFlag = True
		return redirect('/loginRegister/success')
	else:
		passFlag = False
		return redirect('/')

def success(request):
	return render( request, 'loginRegister/success.html')

# def timeDisplay(request):
# 	return render(request,'timeDisplay/index.html',context)

 		



