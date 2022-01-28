from flask import Flask, render_template, request, redirect, url_for, flash
from ...models.students import Student
from . import student
from ... import db,mycursor
from cloudinary.uploader import upload as cloudinary_upload, destroy as cloudinary_destroy
from cloudinary.utils import cloudinary_url

@student.route('/students') 
def students():
    data = Student().get_all()
    return render_template('/students/index.html', students=data, cloudinary_url=cloudinary_url)


@student.route('/delete/<string:id_number>', methods = ['GET'])
def delete(id_number):
    flash("Student Record Has Been Deleted Successfully")
    mycursor.execute("DELETE FROM students WHERE id=%s", (id_number,))
    db.commit()
    return redirect(url_for('student.students')) 


@student.route('/insert', methods = ['POST', 'GET'])
def insert():

    if request.method == "POST":
        flash("Data Saved Successfully")
        id_number = request.form['id_number']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        photo = request.files['photo']
        if photo:
            cloudinary_response = cloudinary_upload(photo, upload_preset='ml_default', invalidate=True)
            new_photo = cloudinary_response['public_id']
        else:
            new_photo=""
        mycursor.execute("INSERT INTO students (id, firstname, lastname, gender, coursecode, yearlevel, photo) VALUES (%s,%s, %s, %s, %s, %s, %s)", (id_number,firstname, lastname, gender, coursecode, yearlevel, new_photo))
        db.commit()
        return redirect(url_for('student.students'))
    return render_template('/students/add.html')



@student.route('/update/<string:id_number>',methods=['POST','GET']) 
def update(id_number):

    if request.method == 'POST':
        newid_number = request.form['id_number']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        photo = request.files['photo']
        if photo:
            cloudinary_response = cloudinary_upload(photo, upload_preset='ml_default', invalidate=True)
            new_photo = cloudinary_response['public_id']
            mycursor.execute("""
                UPDATE students
                SET id=%s, firstname=%s, lastname=%s, gender=%s, coursecode=%s, yearlevel=%s, photo=%s
                WHERE id=%s
                """, (newid_number, firstname, lastname, gender, coursecode, yearlevel, new_photo, id_number))
        else:
           
            mycursor.execute("""
                UPDATE students
                SET id=%s, firstname=%s, lastname=%s, gender=%s, coursecode=%s, yearlevel=%s
                WHERE id=%s
                """, (newid_number, firstname, lastname, gender, coursecode, yearlevel, id_number))
        flash("Data Updated Successfully")
        db.commit()
        return redirect(url_for('student.students'))
    data = Student().get_one(id_number)
    return render_template('/edit/student2.html',id_number=id_number, data=data)

@student.route('/search')
def search():
    q = request.args.get('q') or None
    data = Student().search(q)
    return render_template('/students/index.html', students=data, cloudinary_url=cloudinary_url )




