from employees.employee_dao import EmployeeDAO
from employees.employee import Employee
emp= Employee("fkt002547", "nom","prenom", "fonction", "IT")
data= EmployeeDAO.create(emp)
print(data)