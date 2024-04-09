import database
#importation pour le test dans init.py
#from employee import Employee
#importation pour l'exterieur du package
#from employees import Employee
from employees.employee import Employee
class EmployeeDAO:

    connexion = database.connect_db()
    cursor=connexion.cursor()
    def __init__(self):
        pass

    @classmethod
    def create(cls, emp:Employee):
        sql = """INSERT INTO employee(matricule, nom, prenom, fonction, departement)
                VALUES(%s, %s, %s, %s, %s)
        """
        params = (emp.matricule, emp.nom, emp.prenom, emp.fonction, emp.departement)
        EmployeeDAO.cursor.execute(sql, params)
        EmployeeDAO.connexion.commit()
        EmployeeDAO.cursor.close()
        return  f"l'employé de matricule{emp.matricule} a été ajouté avec succes"

    @classmethod
    def list_all(cls):
        sql="SELECT * FROM employ "
        try:
            EmployeeDAO.cursor.execute(sql)
            employee = EmployeeDAO.cursor.fetchall()
            message= "success"
            EmployeeDAO.cursor.close()
        except Exception as error:
            print(error)
            message = "Une erreur est survenue lors de la recuperation des donnés"
            employee = []
        return (employee, message)

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




    
    
    



