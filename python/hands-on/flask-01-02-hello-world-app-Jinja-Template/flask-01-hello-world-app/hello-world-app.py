from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world from Flask!"

@app.route('/second')
def second():
    return "I am in  London!"

@app.route('/third/subthird')
def third():
    return "Third fffffff!"

if __name__ == '__main__':
    app.run(debug=True)