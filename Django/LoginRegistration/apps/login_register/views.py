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
    return render(request,"login_register/index.html")

def create(request):
    # print "*" * 50
    # print "inside create"
    # print "*" * 50
    errors = User.objects.user_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = 'register')
    else:
        password = request.POST['pword']
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=hash_pw)
        messages.success(request, "Registration was successful! You can log in now.", extra_tags ="register")
    
    return redirect("/")


def login(request):
    # print "*" * 50
    # print "inside login"
    # print "*" * 50
    email = request.POST['email']
    password = request.POST['pword']
    try:
        user = User.objects.get(email = email)
    except:
        messages.error(request, "Please enter a valid email!", extra_tags = 'login')
        return redirect("/")
    encrypted_password = user.password.encode()
    id = user.id

    if bcrypt.checkpw(password.encode(), encrypted_password):
        messages.success(request, "login was successful! You are logged in now!", extra_tags ="login")
        return redirect("/success/" + str(id))
    else:
        print "Ouuuuuuch!!!"
        messages.error(request, "Invalid password!", extra_tags = 'login')
        return redirect("/")
    
    return redirect("/") # in case of other situations not taken care of above
    
def show(request, id):
    # print "*" * 50
    # print "inside show"
    # print "*" * 50
    return render(request,"login_register/success.html")

def logout(request):
    # print "*" * 50
    # print "inside logout"
    # print "*" * 50
    return redirect('/')
