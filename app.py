from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector 
from dotenv import load_dotenv
from os import getenv
app = Flask(__name__)
load_dotenv('.env')

 
app.secret_key = b'verysecretkey'
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="missymay",
    database="studentdatabase"
)

mycursor = db.cursor(buffered=True)

@app.route('/')           
def home(): 
    mycursor.execute("SELECT  * FROM students")
    data = mycursor.fetchall()
    data = [list(student) for student in data]

    return render_template('/students/index.html', students=data )

@app.route('/courses')
def courses():
    mycursor.execute("SELECT  * FROM courses")
    data = mycursor.fetchall()
    data = [list(courses) for courses in data]

    return render_template('/courses/index.html', courses=data)



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Saved Successfully")
        id_number = request.form['id_number']
        name = request.form['name']
        department = request.form['department']
        course = request.form['course']
        year = request.form['year']
        mycursor.execute("INSERT INTO students (id_number, name, department, course, year) VALUES (%s,%s, %s, %s, %s)", (id_number, name, department, course, year))
        db.commit()
        return redirect(url_for('home'))







@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_number = request.form['id_number']
        name = request.form['name']
        department = request.form['department']
        course = request.form['course']
        year = request.form['year']
        mycursor.execute("""
               UPDATE students
               SET name=%s, department=%s, course=%s, year=%s
               WHERE id_number=%s
            """, (name, department, course, year, id_number))
        flash("Data Updated Successfully")
        db.commit()
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

