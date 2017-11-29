# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *

# Create your views here.

def users(request):
    # print "*" * 50
    # print "inside users"
    # print "*" * 50
    context = { 'users': User.objects.all()}
    return render(request,"users/users.html", context)

def new(request):
    # print "*" * 50
    # print "inside new"
    # print "*" * 50
    return render(request,"users/new.html")

def edit(request, id):
    # print "*" * 50
    # print "Inside edit"
    # print "ID: " + str(id)
    # print "*" * 50
    context = {'user':User.objects.get(id=id)}
    return render(request,"users/edit.html", context)

def show(request, id):
    # print "*" * 50
    # print "inside show"
    # print "ID: " + str(id)
    # print "*" * 50
    if request.method == 'POST':
        return update(request, id)
    else:
        context = {'user': User.objects.get(id=id)}
        return render(request,"users/show.html",context)

def create(request):
    # print "*" * 50
    # print "inside create"
    # print "*" * 50
    errors = User.objects.user_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect("/users/new")
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        id = User.objects.last().id
        return redirect("/users/"+str(id))

def destroy(request, id):
    # print "*" * 50
    # print "inside destroy"
    # print "ID: " + str(id)
    # print "*" * 50
    user = User.objects.get(id=id)
    if user:
        user.delete()
    return redirect("/users")

def update(request, id):
    # print "*" * 50
    # print "inside update"
    # print "ID: " + str(id)
    # print "*" * 50
    errors = User.objects.user_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect("/users/"+str(id)+"/edit")
    else:
        user = User.objects.get(id=id)
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.save()
        return redirect("/users/"+str(id))

