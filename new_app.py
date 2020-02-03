from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys

new_app = Flask(__name__)
new_app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLAlchemy(new_app)

class Todo(db.Model):
   
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return '<Task %r>' % self.id

@new_app.route('/')

def index():
    return render_template ('index.html')

if __name__=="__main__": 
    new_app.run(debug=True)
    print("hello")
    
