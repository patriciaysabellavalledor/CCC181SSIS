from flask import Flask
from os import getenv
import mysql.connector 
import cloudinary

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="missymay",
    database="studentdatabase"
)

mycursor = db.cursor(buffered=True)

def create_app():
    app = Flask(__name__)
    app.secret_key = b'verysecretkey'
    
    cloudinary.config(
        cloud_name = 'dkpip1m39' ,
        api_key = '653781448243179', 
        api_secret = 'B-hjljedyAU4A5O8EiZESgePWNc',
        secure = True
    )

    # import blueprints
    from .views.students import student
    from .views.courses import course
    from .views.colleges import college
    from .views.main import main
    

    # register blueprints
    app.register_blueprint(student, url_prefix='/student')    
    app.register_blueprint(course, url_prefix='/courses')
    app.register_blueprint(college, url_prefix='/college')
    app.register_blueprint(main)


    return app

