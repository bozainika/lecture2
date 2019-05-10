from flask import Flask as fl
from flask import render_template as rt
from flask import request
from flask_session import Session

#app.config["SESSION_PERMANENT"]=False 
#app.config["SESSION_TYPE"]="filesystem"
#Session(app)  --> start a session 

app=fl(__name__)

@app.route('/')#("/",methods=['GET','POST'])

def index():
	return rt('index.html')
	#if session.get("notes") is None:  -->if session variable notes is not set then:
	#	session["notes"]=[] --> session variable created and set to an empty array
@app.route('/sayHello', methods=['POST'])

def sayHello():
	name=request.form.get('name')
	return rt('sayHello.html',name=name)
#	names=['Azis', 'Galena', 'Alisia']
#	is_cute=True
#	return rt('names.html',names=names,is_cute=is_cute)

@app.route('/sayHello')

def sayHi():
	return hello()

@app.route('/hello')

def hello():
	return rt('hello.html')