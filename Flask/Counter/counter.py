from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# you need to set a secret key for security purposes
app.secret_key = 'ThisIsCount' 

@app.route('/')
def index():
    if not session.get('count'):
        session['count'] = 0
    session['count'] += 1
    return render_template('counter.html')

@app.route('/add2', methods=['POST'])
def add_two():
    session['count'] += 1
    #We only increment by 1 since reloading the page also increments
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True) # run our server