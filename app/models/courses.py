from app.views import courses
from .. import db, mycursor


class Courses():
    def __init__(self, code = None, name = None):

        self.code = code
        self.name = name
    
    def get_all(self):
        query = 'SELECT * FROM courses'
        mycursor.execute(query)
        result = mycursor.fetchall()
        courses = [list(courses) for courses in result]
        return courses 

    def get_one(self,id):
        query = 'SELECT * FROM courses WHERE code=%s'
        mycursor.execute(query,(id,))
        result = mycursor.fetchone()
        #students = [list(student) for student in result]
        return result 

    def search(self, q=None):
        query = 'SELECT * FROM courses WHERE concat(code, name, colleges) LIKE %s'
        mycursor.execute(query, ('%' + q + '%',))
        result = mycursor.fetchall()
        courses = [list(course) for course in result]
        return courses

    