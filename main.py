from employees.employee_dao import EmployeeDAO
from employees.employee import Employee
emp= Employee("fkt00300", "nom","prenom", "fonction", "IT")
data= EmployeeDAO.create(emp)
print(data)

(employee, message) =EmployeeDAO.list_all()
print(message, employee)

