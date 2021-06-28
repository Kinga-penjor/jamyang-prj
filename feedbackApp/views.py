from django.shortcuts import render, redirect
from . forms import CreateUserForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
	events = Event.objects.all()
	feedbacks = Feedback.objects.all()
	announcements = Announcement.objects.all()
	context = {
		'events': events,
		'feedbacks': feedbacks,
		'announcements': announcements,
	}
	return render(request, 'home.html', context)

def registerForm(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context={'form':form}
	return render(request, 'register.html', context)

def loginForm(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'username or password is incorrect')
	contex={}
	return render(request, 'login.html',contex)

def logoutUser(request):
	logout(request)
	return redirect('login')

def feedback(request):
	if request.method == 'POST':
		form = request.POST
		if request.user.is_authenticated:
			user = request.user
			if len(form['feedback_message'])<5:
				messages.success(request, 'Feedback is too short')
			else:
				Feedback.objects.create(
					user=user,
					feedback=form['feedback_message']
				) 
				messages.success(request, 'Feedback successfully submitted')
	return render(request, 'feedback.html')

def view_feedback(request):
	feedbacks = Feedback.objects.all()
	context = {
		'feedbacks':feedbacks,
	}
	return render(request, 'feedback_view.html', context)

def event(request):
	events = Event.objects.all()
	context = {
		'events':events,
	}
	return render(request, 'events.html', context)

def announcement(request):
	announcements = Announcement.objects.all()
	context = {
		'announcements':announcements,
	}
	return render(request, 'announcement.html', context)
