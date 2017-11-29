# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.

def index(request):
    return render (request, 'session_words/index.html')

def process(request):
    this_word = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key !="bigfont":
            this_word[key] = value
        if key == "bigfont":
            this_word["font"] = "big"
        else:
            this_word["font"] = ""
            
    this_word['created_at'] = datetime.now().strftime("%I:%M:%S %p, %B %d, %Y")
    
    try:
        request.session['data']
    except KeyError:
        request.session['data'] = []
    
    temp = request.session['data']
    temp.append(this_word)
    request.session['data'] = temp

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')