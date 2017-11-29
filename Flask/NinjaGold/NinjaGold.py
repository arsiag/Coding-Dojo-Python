from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsGold'

@app.route('/')
def index():
    if not session['total']:
        session['total'] = 0
    if not session['activity']:
        session['activity'] = []
    return render_template('NinjaGold.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    location = request.form['hidden']
    if location == 'farm':
        farmGold = random.randrange(10, 21)
        timestamp = datetime.datetime.now()
        session['total'] += farmGold
        session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(farmGold, 'farm', timestamp)])
        #addActivity(farmGold, 'earned', 'farm')
    elif location == 'cave':
        caveGold = random.randrange(5, 11)
        timestamp = datetime.datetime.now()
        session['total'] += caveGold
        session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(caveGold, 'cave', timestamp)])
        #addActivity(caveNum, 'earned', 'cave')
    elif location == 'house':
        houseGold = random.randrange(2, 6)
        timestamp = datetime.datetime.now()
        session['total'] += houseGold
        session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(houseGold, 'house', timestamp)])
        #addActivity(houseNum, 'earned', 'house')
    elif location == 'casino':
        casinoGold = random.randrange(0, 51)
        timestamp = datetime.datetime.now()
        chance = random.randrange(0, 2)
        if chance == 1:
            session['total'] += casinoGold
            session['activity'].append(['earn', 'Earned {} golds from the {}! ({})'.format(casinoGold, 'casino', timestamp)])
            #addActivity(casinoNum, 'earned', 'casino')
        elif chance == 0:
            session['total'] -= casinoGold
            session['activity'].append(['lost', 'Entered a casino and lost {} golds... Ouch! ({})'.format(casinoGold, timestamp)])
            #addActivity(casinoNum, 'lost', 'casino')
        else:
            print "Error"
    else:
        print "Error"
    return redirect('/')

@app.route('/clear', methods=['POST'])
def reset():
    session['total'] = 0
    session['activity'] = []
    return redirect('/')

app.run(debug=True) # run our server