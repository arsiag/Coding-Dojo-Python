from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsColor' 

@app.route('/')
def index():
    if not session.get('color'):
        session['color'] = "255,255,255"
    return render_template("color.html")

@app.route('/color', methods=['POST'])
def change_color():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    session['color'] = str(red) + "," + str(green) + "," + str(blue)
    return redirect('/')

app.run(debug=True) 