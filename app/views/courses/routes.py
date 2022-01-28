from flask import Flask, render_template, request, redirect, url_for, flash
from ...models.courses import Courses
from . import course
from ... import db,mycursor

@course.route('/courses')
def courses():
    data = Courses().get_all()
    return render_template('/courses/index.html', courses=data )

@course.route('/delete/<string:code>', methods = ['GET'])
def delete(code):
    flash("Deleted Successfully")
    mycursor.execute("DELETE FROM courses WHERE code=%s", (code,))
    db.commit()
    return redirect(url_for('course.courses')) 


@course.route('/insert', methods = ['POST', 'GET'])
def insert():

    if request.method == "POST":
        flash("Data Saved Successfully")
        code = request.form['code']
        name = request.form['name']
        colleges = request.form['colleges']
      
        mycursor.execute("INSERT INTO courses (code, name, colleges ) VALUES (%s,%s, %s)", (code, name, colleges))
        db.commit()
        return redirect(url_for('course.courses'))
    return render_template('/courses/add.html')



@course.route('/update/<string:code>',methods=['POST','GET']) 
def update(code):

    if request.method == 'POST':
        newcode = request.form['code']
        name = request.form['name']
        colleges = request.form['colleges']
        mycursor.execute("""
               UPDATE courses
               SET code=%s, name=%s, colleges=%s
               WHERE code=%s
            """, (newcode, name, colleges, code))
        flash("Data Updated Successfully")
        db.commit()
        return redirect(url_for('course.courses'))
    data = Courses().get_one(code)
    return render_template('/edit/course2.html',code=code, data=data)


@course.route('/search')
def search():
    q = request.args.get('q') or None
    data = Courses().search(q)
    return render_template('/courses/index.html', courses=data )