from employee_dao import EmployeeDAO
from employee import Employee
employe= Employee("fck12354", "Diallo", "Abdou", "developpeur", "IT")
message= EmployeeDAO.create(employe)
print(message)


