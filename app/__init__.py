from flask import Flask
from os import getenv
import os
import mysql.connector 
import cloudinary

db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

mycursor = db.cursor(buffered=True)

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    
    cloudinary.config(
        cloud_name = os.getenv('CLOUD_NAME'),
        api_key = os.getenv('API_KEY'),
        api_secret = os.getenv('API_SECRET'),
        secure = os.getenv('SECURE')
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

