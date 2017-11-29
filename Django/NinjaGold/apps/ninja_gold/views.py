# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.

def index(request):
    print "*" * 50
    print "Running ninja_gold"
    print "*" * 50
    
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render (request, 'ninja_gold/NinjaGold.html')

def process_money(request):
    location = request.POST['hidden']
    if location == 'farm':
        farmGold = random.randrange(10, 21)
        timestamp = datetime.datetime.now()
        request.session['total'] += farmGold
        request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(farmGold, 'farm', timestamp)])
    elif location == 'cave':
        caveGold = random.randrange(5, 11)
        timestamp = datetime.datetime.now()
        request.session['total'] += caveGold
        request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(caveGold, 'cave', timestamp)])
    elif location == 'house':
        houseGold = random.randrange(2, 6)
        timestamp = datetime.datetime.now()
        request.session['total'] += houseGold
        request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(houseGold, 'house', timestamp)])
    elif location == 'casino':
        casinoGold = random.randrange(0, 51)
        timestamp = datetime.datetime.now()
        chance = random.randrange(0, 2)
        if chance == 1:
            request.session['total'] += casinoGold
            request.session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(casinoGold, 'casino', timestamp)])
        elif chance == 0:
            request.session['total'] -= casinoGold
            request.session['activity'].append(['lost', 'Entered a casino and lost {} golds... Ouch! ({})'.format(casinoGold, timestamp)])
        else:
            print "Error"
    else:
        print "Error"
    return redirect('/')

def clear(request):
    request.session['total'] = 0
    request.session['activity'] = []
    return redirect('/')
