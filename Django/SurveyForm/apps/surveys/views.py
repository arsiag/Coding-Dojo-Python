# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render (request, 'surveys/index.html')

def process(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['location'],
        "Favorite Language": request.POST['lang'],
        "Comment": request.POST['comment']
    }
    return redirect('/results')

def results(request):
    return render(request, 'surveys/results.html')