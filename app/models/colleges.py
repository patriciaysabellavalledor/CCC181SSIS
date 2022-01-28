from app.views import colleges
from .. import db, mycursor


class Colleges():
    def __init__(self, code = None, name = None):

        self.code = code
        self.name = name
    
    def get_all(self):
        query = 'SELECT * FROM colleges'
        mycursor.execute(query)
        result = mycursor.fetchall()
        colleges = [list(colleges) for colleges in result]
        return colleges 

    def get_one(self,id):
        query = 'SELECT * FROM colleges WHERE code=%s'
        mycursor.execute(query,(id,))
        result = mycursor.fetchone()
        #students = [list(student) for student in result]
        return result 
    
    def search(self, q=None):
        query = 'SELECT * FROM colleges WHERE concat(code, name) LIKE %s'
        mycursor.execute(query, ('%' + q + '%',))
        result = mycursor.fetchall()
        colleges = [list(colleges) for colleges in result]
        return colleges