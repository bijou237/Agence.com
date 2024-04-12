from flask import Flask, render_template, request, session, redirect, url_for
from employees.employee_dao import EmployeeDAO
from employees.employee import Employee
from users.user import User
from users.user_dao import UserDAO


app = Flask(__name__)
app.secret_key= "clesecrete"

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
    if 'username' not in session:
        return redirect(url_for('login'))
    (message, employes) = EmployeeDAO.list_all()
    print(employes)
    return render_template("liste_employes.html", message=message,employes=employes)


@app.route('/add-employe', methods=['POST','GET'])
def add_employe():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    message=None
    print("Methode HTTP utiliée : ", request.method)
    if request.method == "POST":
        nom = req['nom']
        prenom = req['prenom']
        matricule = req['matricule']
        fonction = req['fonction']
        departement = req['departement']
        if nom=="" or prenom=="" or  matricule=="" or fonction=="" or departement=="":
            message="error"
            print("message")
        else:
            employe = Employee(nom, prenom, matricule, fonction, departement )
            message=EmployeeDAO.create(employe)
            #print(message)
    return render_template('add_employe.html', message=message)



@app.route('/login', methods=['GET','POST'])
def login():

    message=None
    
    if request.method == "POST":
        req = request.form
        username = req['username']
        password = req['password']
        if username=='' or password=='':
            message='error'
        else:
            (message, user)= UserDAO.get_one(username, password)
            print('test message',message)
            if message=='success' and user !=None:
                session['username'] = user[2] #on met username dans notre variable 
                session['nom_complet'] = user[1] # On met le nom complet dans notre variable 
                return redirect(url_for('home'))
        print(message)
        
    return render_template('login.html',message=message, user=None)

@app.route("/Logout")    
def logout():
    session.clear()
    return redirect(url_for('login'))