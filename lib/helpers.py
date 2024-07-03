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
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass