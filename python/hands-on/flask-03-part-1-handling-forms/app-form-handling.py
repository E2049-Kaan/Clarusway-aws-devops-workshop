# Import Flask modules
<<<<<<< HEAD
from flask import Flask, render_template, request


# Create an object named app
app = Flask (__name__)

=======
from flask import Flask, redirect, url_for, render_template, request

# Create an object named app
app = Flask(__name__)
>>>>>>> 65570f59f5f0b56194343c920fdd13ca9e337090


# Create a function named `home` which uses template file named `index.html` given under `templates` folder,
# send your name as template variable, and assign route of no path ('/')
<<<<<<< HEAD
@app.route("/")
def home ():
    return render_template ("index.html", name = "walt")

# Write a function named `greet` which uses template file named `greet.html` given under `templates` folder

@app.route ("/greet", methods = ["GET"])
def greet():
    if "user" in request.args:
        usr = requests.argsv["user"]
        return render_template ("greet.html", user = usr)
    else:
        render_template ("greet.html", user = "Send your username with 'user' param in query string")
        
=======
@app.route('/')
def home():
    return render_template('index.html', name='Tyler')

# Write a function named `greet` which uses template file named `greet.html` given under `templates` folder
# and assign to the dynamic route of ('/<name>')
@app.route('/greet', methods=['GET'])
def greet():
    if 'user' in request.args:
        usr = request.args['user']
        return render_template('greet.html', user=usr)
    else:
        return render_template('greet.html', user='Send your user name with "user" param in query string')

>>>>>>> 65570f59f5f0b56194343c920fdd13ca9e337090

# Write a function named `login` which uses `GET` and `POST` methods,
# and template files named `login.html` and `secure.html` given under `templates` folder
# and assign to the static route of ('login')
<<<<<<< HEAD

@app.route ("/login", methods =["GET", "POST"])
def login ():
    if request.method == "POST":
        user_name = request.form
        return render_template ("secure.html", user = user_name)
    else:
        return render_template ("login.html")
# Add a statement to run the Flask application which can be reached from any host on port 80.

if __name__ == "__main__":
    app.run (debug=True)
#    app.run(host='0.0.0.0', port=80)
=======
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        return render_template('secure.html', user=user_name)
    else:
        return render_template('login.html')

# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == '__main__':
    app.run(debug=True)
#    app.run(host='0.0.0.0', port=80)
>>>>>>> 65570f59f5f0b56194343c920fdd13ca9e337090
