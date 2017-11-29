from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def ninjas():
    return render_template("ninjas.html")
   
@app.route('/ninja/<ninja_color>')
def show_one_ninja(ninja_color):
    return render_template("ninja_color.html", color=ninja_color)

app.run(debug=True) # run our server