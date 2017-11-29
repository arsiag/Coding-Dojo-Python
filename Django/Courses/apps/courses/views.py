# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from models import *

# Create your views here.
def courses(request):
    # print "*" * 50
    # print "Inside course"
    # print "*" * 50
    courses = Course.objects.all()
    context = {
        "courses" : courses
    }
    return render(request,"courses/courses.html", context)

def create(request):
    # print "*" * 50
    # print "Inside create"
    # print "*" * 50
    if request.method == "POST":
        error = Course.objects.course_validator(request.POST)
        if len(error):
            messages.error(request, error['name'], extra_tags='name')

        error = Description.objects.desc_validator(request.POST)
        if len(error):
            messages.error(request,error['desc'],extra_tags='desc')

        if len(error) == 0:
            Course.objects.create(name=request.POST['name'])
            course = Course.objects.last()
            Description.objects.create(content=request.POST['desc'], course=course)
            course.desc = Description.objects.last()
            course.save()

        return redirect("/courses")

def confirm(request, id):
    # print "*" * 50
    # print "Inside confirm"
    # print "ID: " + str(id)
    # print "*" * 50
    course = Course.objects.get(id=id)
    context = {
        "course": course
    }
    return render(request,"courses/destroy.html",context)

def remove(request, id):
    # print "*" * 50
    # print "Inside remove"
    # print "ID: " + str(id)
    # print "*" * 50
    if request.method == "POST":
        course = Course.objects.get(id=id)
        if course:
            course.delete()
    return redirect("/courses")

def comments(request, id):
    # print "*" * 50
    # print "Inside comments"
    # print "ID: " + str(id)
    # print "*" * 50
    course = Course.objects.get(id=id)
    context = {
        "course": course,
        "comments": course.comments.all()
    }
    return render(request,"courses/comments.html",context)

def create_comments(request, id):
    # print "*" * 50
    # print "Inside create_comments"
    # print "ID: " + str(id)
    # print "*" * 50
    if request.method == "POST":
        Comment.objects.create(content=request.POST['content'], course=Course.objects.get(id=id))
    return redirect('/courses/'+str(id)+'/comments')
