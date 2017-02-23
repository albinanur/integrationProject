from django.shortcuts import render, redirect
from .models import Course
from ..loginRegister.models import User
from django.db.models import Count
from django.core.urlresolvers import reverse


def index(request):
	context = {
		'courses': Course.objects.all()
	}
	return render(request, 'courses/index.html',context)

def create(request):
	Course.objects.create(name = request.POST['name'], description = request.POST['description'])

	return redirect('/')


def delete(request, id):
	course = Course.objects.get(pk=id)
	context = {
		'second': course
	}

	return render(request, 'courses/delete.html', context)

def destroy(request):
	if 'yes' in request.POST:
		id = request.POST['course_id']
		Course.objects.filter(id = id).delete()
		return redirect('/')
	elif 'no' in request.POST:
		return redirect('/')

def addusertocourse(request):
    if request.method == 'POST':
        selected_user = User.objects.get(id=request.POST['user'])
        selected_course = Course.objects.get(id=request.POST['course'])
        selected_course.user.add(selected_user)
        selected_course.save()
    # countusers = Course.objects.annotate(num=Count('user'))
    context = {
        "users": User.objects.all(),
        "courses": Course.objects.all(),
        "counts": Course.objects.annotate(num=Count('user'))
    }
    return render(request, 'courses/adduser.html', context)






