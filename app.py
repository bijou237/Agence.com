from flask import Flask, render_template
from employees.employee_dao import EmployeeDAO

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")    
def services():
    return render_template("services.html")

@app.route("/employes")    
def employes():
    (message, employes) = EmployeeDAO.list_all()
    return render_template("liste_employes.html", message=message,employes=employes)


@app.route("/add-employe")    
def add_employe():
    return render_template("add_employe.html")
