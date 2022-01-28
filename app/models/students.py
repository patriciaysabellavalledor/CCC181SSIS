from app.views import students
from .. import db, mycursor



class Student():
    def __init__(self, 
        id= None, 
        firstname = None,  
        lastname = None, 
        yearlevel = None, 
        gender = None, 
        coursecode = None):
        
    
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.yearlevel = yearlevel
        self.gender = gender
        self.coursecode = coursecode


    def get_all(self):
        query = 'SELECT * FROM students'
        mycursor.execute(query)
        result = mycursor.fetchall()
        students = [list(student) for student in result]
        print (students)

        return students

    def get_one(self,id):
        query = 'SELECT * FROM students WHERE id=%s'
        mycursor.execute(query,(id,))
        result = mycursor.fetchone()
        #students = [list(student) for student in result]
        return result

    def search(self, q=None):
        #query = 'SELECT * FROM students WHERE concat(id, firstname, lastname, gender, coursecode, yearlevel) LIKE %s'
        query = 'SELECT * FROM students WHERE concat(id, firstname, lastname, gender, COALESCE(coursecode,""), yearlevel) LIKE %s'
        mycursor.execute(query, ('%' + q + '%',))
        result = mycursor.fetchall()
        students = [list(student) for student in result]
        return students