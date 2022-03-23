from turtle import title
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ToDo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column (db.String(100))
    complete = db.Column (db.Boolean)
    

@app.route("/")
def  index():
    #Show all database
    
    todo_list = ToDo.query.all()
  
    return render_template("base.html", todo_list = todo_list)



if __name__ == "__main__":
    db.create_all()
    
    # new_todo = ToDo(title='todo_app', complete = False)
    
    # db.session.add (new_todo)
    # db.session.commit()
    
    
    app.run (debug=True)
    
    