from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my youtube channel emon'

@app.route('/members')
def members():
    return 'Welcome to my youtube channel members'

if __name__=='__main__':
    app.run(debug=True)
    