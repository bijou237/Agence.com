import database 
from employees.employee import Employee
from employees.employee_dao import EmployeeDAO
from departements.departement import Departement
class Departement:
     connexion = database.connect_db()
     cursor=connexion.cursor()
     def __init__(self):
        pass

@classmethod
def add(cls, dep:Employee):
        sql = """INSERT INTO employee(matricule, username, password, post)
                VALUES(%s, %s, %s, %s)
        """
        params = (emp.matricule, emp.nom, emp.prenom, emp.fonction, emp.departement)
        try :
            EmployeeDAO.cursor.execute(sql, params)
            EmployeeDAO.connexion.commit()
            EmployeeDAO.cursor.close()
            message ="success"
        except Exception as error:
            print(error)
            message = "failure"
        return  message

@classmethod
def list_all(cls):
        sql="SELECT * FROM employee "
        try:
            EmployeeDAO.cursor.execute(sql)
            employee = EmployeeDAO.cursor.fetchall()
            message= "success"
            EmployeeDAO.cursor.close()
        except Exception as error:
            print(error)
            message = "error"
            employee = []
        return (message, employee)

    @classmethod
    def delete(cls, matricule):
        sql="DELETE FROM employee WHERE matricule=%s "
        EmployeeDAO.cursor.execute(sql,(matricule,))
        EmployeeDAO.connexion.commit()
        EmployeeDAO.cursor.close()

        return f"l'employé de matric"

    @classmethod
    def update(cls, emp):
        sql= "UPDATE Employee SET matricule=%s, nom=%s. prenom=%s, fonction=%s, departement=%s "
        params = (emp.matricule, emp.nom, emp.prenom, emp.fonction, emp.departement,)
        EmployeeDAO.cursor.excecute(sql, params)
        EmployeeDAO.connexion.commit()
        EmployeeDAO.cursor.close()