from flask import Flask, render_template, request, redirect, url_for, flash
from . import main



@main.route('/')
def index():
    
    return redirect(url_for('student.students')) 


