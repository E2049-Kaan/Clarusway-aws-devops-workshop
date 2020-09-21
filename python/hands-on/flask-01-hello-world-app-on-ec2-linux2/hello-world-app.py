from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
=======
@app.route('/')
def hello():
    return 'Hello World'

if __name__=='__main__':
   app.run(host='0.0.0.0', port=80)
>>>>>>> 65570f59f5f0b56194343c920fdd13ca9e337090
