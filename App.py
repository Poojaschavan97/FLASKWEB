from flask import Flask,render_template,request,redirect
#redirect to redirect from route to route
from DB import Database
import API

app=Flask(__name__) # name initialize the flask app
dbo=Database()

@app.route('/') # @ represents a decorator it says if someone names your website and adds / in it execute below program
def index():
    return render_template('login.html') # this will execute the login page when hit the url
#render template used to loads html

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/perform_registration',methods=['post']) # method is very important as we are using post
def perform_registration():
    name = request.form.get('name of user')
    email = request.form.get('email of user')
    password = request.form.get('password of user')
    response= dbo.insert(name,email, password)
    if response:
        return render_template('login.html',message='Registration complete you can login now......!')
    else:
        return render_template('login.html',message='Email Already Exists Kindly Login....!')

@app.route('/perform_login', methods=['post'])
def perform_login():
    email=request.form.get("user's email")
    password=request.form.get("user's password")
    response=dbo.search(email,password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('NER.html')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text=request.form.get('ner_text')
    entity=request.form.get('entity')
    response=API.ner(text,entity)
    txt=''
    for i in response['entities']:
        txt=txt+i['text']+'\n'
    return txt

@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('Sentiment.html')

@app.route('/perform_sentiment_analysis',methods=['post'])
def perform_sentiment_analysis():
    text=request.form.get('sentiment_text')
    response=API.sentiment_analysis(text)
    result=response['scored_labels'][0]['label']
    return result

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/perform_summary' , methods=['post'])
def perform_summary():
    text=request.form.get('summary_text')
    response=API.summary(text)
    return response['summary_text']


app.run(debug=True)# run to run the code and debug so we don't have to reopen the webpage repeatingly just reload it.
