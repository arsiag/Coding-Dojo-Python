from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'ThisIsNumber' 

@app.route('/')
def set_number():
    if session['number'] is None:
        session['number'] = random.randrange(0, 101) 
    print "My number is: " + str(session['number'])
    return render_template('number.html')

@app.route('/guess', methods=['POST'])
def check_number():
    error = None
    success = None
    guessedNum = request.form['number']
    print "Guessed number is: " + str(guessedNum)
    if request.method == 'POST':
        if guessedNum.isdigit():
            guessedNum = int(guessedNum)
            if guessedNum < 1 or guessedNum > 100:
                flash('Number out of range', 'error')
            elif guessedNum == session['number']:
                flash(str(guessedNum) + ' was correct', 'success')
                return redirect('/')
            elif guessedNum > session['number']:
                flash(str(guessedNum) + ' was too high!', 'error')
            else:
                flash(str(guessedNum) + ' was too low!', 'error')
        else:
            flash('Not a valid guess', 'error')

    return redirect('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session['number'] = random.randrange(0, 101) 
    return redirect('/')

app.run(debug=True) # run our server