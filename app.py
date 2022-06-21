import os
from flask import Flask,redirect, request, render_template, request, url_for
import pymysql

db = pymysql.connect(host='mysql1',user='root',password="",port=3306)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")
cursor.execute("CREATE TABLE IF NOT EXISTS students (name VARCHAR(20),class VARCHAR(20),age VARCHAR(10),address VARCHAR(100))")

app = Flask(__name__)

#mysql = MySQL()
#api=Api(app)




cursor = db.cursor()



@app.route("/",methods=['GET','POST'])
def read():
    if request.method == 'POST' and 'name' in request.form and 'student_class' in request.form and 'age' in request.form and 'address' in request.form:
       nm = request.form['name']
       sc = request.form['student_class']
       ag = request.form['age']
       addr = request.form['address']
       cursor.execute("INSERT INTO students VALUES (%s,%s,%s,%s)",(nm,sc,ag,addr))
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    return render_template('index.html',data=records)

@app.route('/delete/<string:name>', methods=['POST'])
def remove(name):
   cursor.execute("DELETE FROM students where name=%s",name)
   return redirect (url_for('read'))

if __name__ == "__main__":
    app.run()


