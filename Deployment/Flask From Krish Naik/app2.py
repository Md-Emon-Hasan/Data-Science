# building url dynamically
# variables rules and url building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my youtube channel'

@app.route('/sucess/<int:score>')
def sucess(score):
    return 'This person has passed and the marks is '+str(score)+'<html><body><h1>HTML TAG</h1></body></html>'

@app.route('/fail/<int:score>')
def fail(score):
    return 'This person has failed and the marks is '+str(score)

# result checker
@app.route('/results/<int:marks>')
def resutls(marks):
    result=''
    if marks<50:
        result='fail'
    else:
        result='sucess'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)
