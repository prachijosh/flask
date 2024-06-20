from flask import Flask, render_template

# Create a Flask Instance 
app = Flask (__name__)

# Create a route decorator 
@app.route('/')
def index():
    first_name = "Prachi"
    stuff = "this is Bold text"
    favorite_pizza = ["pepperoni","cheese","mushroom",41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)
#http://localhost:5000/user/name
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)
