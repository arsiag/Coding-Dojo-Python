# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.

def index(request):
    print "*" * 50
    print "Running ninja_gold_bonus"
    print "*" * 50

    if 'total' not in request.session:
        request.session['total'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render (request, 'ninja_gold_bonus/NinjaGold.html')

def process_money(request, place):
    this_gold = 0
    action = 'earned'
    if place == 'farm':
        this_gold = random.randrange(10,21)
    elif place == 'cave':
        this_gold = random.randrange(5,11)
    elif place == 'house':
        this_gold = random.randrange(2,6)
    else:
        this_gold = random.randrange(-50,51)
        if this_gold < 0:
            action = 'lost'

    request.session['total'] += this_gold

    timestamp = datetime.datetime.now()
    this_activity = {
        'class': action,
        'message': "You {} {} golds from the {} ({})".format(action, abs(this_gold), place, timestamp)
    }

    temp = request.session['activity']
    temp.append(this_activity)
    request.session['activity'] = temp

    return redirect('/')

def clear(request):
    request.session['total'] = 0
    request.session['activity'] = []
    return redirect('/')
