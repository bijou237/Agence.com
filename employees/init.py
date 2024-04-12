from employee_dao import EmployeeDAO
from employee import Employee
employe= Employee("fck12354", "Diallo", "Abdou", "developpeur", "IT")
message= EmployeeDAO.create(employe)
#print(message)
#Resultat = Employee('TKCG2546', 'Clara', 'cla', 'Admin','IT','conseillere')

Resultat = EmployeeDAO.list_all()
print(Resultat) 


