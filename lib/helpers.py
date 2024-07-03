from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    matching_department = Department.find_by_name(name)
    print(matching_department) if matching_department else print(f'Department {name} not found')


def find_department_by_id():
    id = input("Enter the department's id: ")
    matching_department = Department.find_by_id(int(id))
    print(matching_department) if matching_department else print(f'Department {id} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id = input("Enter department's id: ")
    name = input("Enter department's name: ")
    location = input("Enter department's location: ")
    department_instance = Department.find_by_id(int(id))
    if department_instance:
        try:
            department_instance.name = name
            department_instance.location = location
            department_instance.update()
            print(f'Success: {department_instance}')
        except Exception as exc:
            print("Error creating department: ", exc)
    else:
        print('No department found')


def delete_department():
    id = input("Enter department's id: ")
    matching_dept = Department.find_by_id(int(id))
    if matching_dept:
        matching_dept.delete()
        print(f'Success: Department with id {id} was deleted')
    else:
        print('No department found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    matching_employee = Employee.find_by_name(name)
    print(matching_employee) if matching_employee else print(f'Employee {name} not found')


def find_employee_by_id():
    id = input("Enter the employee's id: ")
    matching_employee = Employee.find_by_id(int(id))
    print(matching_employee) if matching_employee else print(f'employee {id} not found')


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = int(input("Enter the employee department's id: "))
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id = input("Enter employee's id: ")
    name = input("Enter employee's name: ")
    job_title = input("Enter employee's job title: ")
    department_id = int(input("Enter employee department's id: "))
    employee_instance = Employee.find_by_id(int(id))
    if employee_instance:
        try:
            employee_instance.name = name
            employee_instance.job_title = job_title
            employee_instance.department_id = department_id
            employee_instance.update()
            print(f'Success: employee with {id} has been updated')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print('No employee found')


def delete_employee():
    id = input("Enter employee's id: ")
    matching_employee = Employee.find_by_id(int(id))
    if matching_employee:
        matching_employee.delete()
        print(f'Success: Employee with id {id} was deleted')
    else:
        print('No employee found')


def list_department_employees():
    id = int(input("Enter the department's id: "))
    matching_dept = Department.find_by_id(id)
    if matching_dept:
        employees = matching_dept.employees()
        for employee in employees:
            print(employee)
    else:
        print('No department found')