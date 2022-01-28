from flask import Flask, render_template, request, redirect, url_for, flash
from ...models.colleges import Colleges
from . import college
from ... import db,mycursor

@college.route('/colleges')
def colleges():


    data = Colleges().get_all()
    return render_template('/colleges/index.html', colleges=data )

@college.route('/delete/<string:code>', methods = ['GET'])
def delete(code):
    flash("Deleted Successfully")
    mycursor.execute("DELETE FROM colleges WHERE code=%s", (code,))
    db.commit()
    return redirect(url_for('college.colleges')) 


@college.route('/insert', methods = ['POST', 'GET'])
def insert():

    if request.method == "POST":
        flash("Data Saved Successfully")
        code = request.form['code']
        name = request.form['name']
      
        mycursor.execute("INSERT INTO colleges (code, name) VALUES (%s,%s)", (code, name))
        db.commit()
        return redirect(url_for('college.colleges'))
    return render_template('/colleges/add.html')



@college.route('/update/<string:code>',methods=['POST','GET']) 
def update(code):

    if request.method == 'POST':
        newcode = request.form['code']
        name = request.form['name']
        mycursor.execute("""
               UPDATE colleges
               SET code=%s, name=%s 
               WHERE code=%s
            """,(newcode, name, code))
        flash("Data Updated Successfully")
        db.commit()
        return redirect(url_for('college.colleges'))
    data = Colleges().get_one(code)
    return render_template('/edit/college2.html',code=code, data=data)

@college.route('/search')
def search():
    q = request.args.get('q') or None
    data = Colleges().search(q)
    return render_template('/colleges/index.html', colleges=data )




# step 1. Create blueprint (views>colleges>__init__.py)
# step 2. Register blueprint (app>__init__.py)
# step 3. Use blueprint to define the routes (views>colleges>routes.py)
# step 4. Create models (models>colleges.py)