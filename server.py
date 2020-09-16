from flask import Flask, render_template,request,redirect,flash,url_for
from Analysis import Analysis
import time
from predict import *
from datetime import datetime as dt
from db import Database

class Server:
    # def __init__(self):
    app = Flask(__name__,static_url_path='/static/styles')
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route('/', methods=['GET'])
    def root():
        return render_template('Crime Analysis.html')
    @app.route('/Analysis',methods=['GET','POST'])
    def visual():
        # if request.method == 'GET':    
        return render_template('visualization.html')
    @app.route('/Graph',methods=['GET','POST']) 
    def graph():
        if request.method == 'GET':
            return render_template('Graph.html')
        elif request.method == 'POST':
            x = int(request.form['graph'])
            Analysis(x)#.selection(x)
            time.sleep(5)
            return render_template('Images.html' )
    @app.route('/Animated_Graph',methods=['GET']) 
    def tableau(): #graphanimated.html
        return render_template('graphanimated.html')
    @app.route('/Live Chart',methods=['GET']) 
    def chartjs():
        return render_template('dataflowchart.html')
    @app.route('/Prediction',methods=['GET','POST'])
    def Predict():
        if request.method == 'GET':
            return render_template('prediction.html')
        elif request.method == 'POST':
            value = int(request.form['value'])
            predicted = Predict().model(value)
            yr = dt.now().year
            print(type(dt.now().time()) ,'  is todays date   ',dt.now().date()) 
            return render_template('predict.html',data = predicted,yr = yr, year = value)
    @app.route('/Contact',methods=['GET','POST'])
    def cont():
        if request.method == 'POST':
            name = request.form['firstname']
            s_name = request.form['lastname']
            nation = request.form['nation']
            state = request.form['state']
            cmmnt = request.form['subject']
            email = request.form['email']
            db = Database()
            db.execute(f"insert into project (name,s_name,nation,state,cmmnt,emailid) values ('{name}','{s_name}','{nation}','{state}','{cmmnt}','{email}')")
            flash(" Welcome, Registration successful")   
            return redirect(url_for('cont'))
        else:
            return render_template('contact.html')
    @app.route('/About')
    def about():
        return render_template('Aboutme.html')
    app.run(host='0.0.0.0', port=4040,debug=False)
if __name__ == '__main__':  
    Server()
