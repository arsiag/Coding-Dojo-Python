# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    rand_word = get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 1
    context = {
        'random_word': rand_word,
        'counter': request.session['counter'],
    }
    return render(request, 'random_word/index.html', context)

def generate(request):
    try:
        request.session['counter'] += 1
    except KeyError:
        pass
    return redirect('/')

def reset(request):
    try:
        request.session['counter'] = 1
    except KeyError:
        pass
    return redirect('/')


