from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'FormValidation'

@app.route('/')
def index():
  location_list = ['San Jose', 'New York', 'Seattle', 'Dallas']
  language_list = ['Python', 'PHP', 'Javascript', 'Ruby']
  session['locations'] = location_list
  session['languages'] = language_list
  return render_template("index.html")

@app.route('/verify', methods=['POST'])
def verify_user():
  if len(request.form['name']) == 0:
      flash('Name cannot be blank', 'nameError')
      return redirect('/')
  if len(request.form['comment']) == 0:
      flash('Comment cannot be blank', 'commentError')
      return redirect('/')
  if len(request.form['comment']) > 120:
      flash('Comment is too long', 'commentError')
      return redirect('/')

  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['lang'] = request.form['lang']
  session['comment'] = request.form['comment']

  return redirect('/results')

@app.route('/results')
def show_results():
  return render_template("results.html")

app.run(debug=True) # run our server