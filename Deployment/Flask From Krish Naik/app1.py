# building url dynamically
# variables rules and url building

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my youtube channel'

@app.route('/sucess/<int:score>')
def sucess(score):
    return 'This person has passed and the marks is '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'This person has failed and the marks is '+str(score)

# result checker
@app.route('/results/<int:score>')
def resutls(score):
    result=''
    if score<50:
        result='fail'
    else:
        result='sucess'
    return result

if __name__=='__main__':
    app.run(debug=True)
