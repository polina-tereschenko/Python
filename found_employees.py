employees = {
    "Кузін": "вул.Терещенка 5",
    "Куравльов": "вул.Терещенка 7",
    "Кудін": "вул.Терещенка 2",
    "Кульков": "вул.Терещенка 20",
    "Кубиків": "вул.Терещенка 19",
    "Атаманчук": "вул.Терещенка 99",
    "Бабіч": "вул.Терещенка 4",
    "Зубар": "вул.Терещенка 44",
    "Івашина": "вул.Терещенка 5",
    "Федишин": "вул.Терещенка 105"
}

def print_all_addresses():
    for employee, address in employees.items():
        print(f'{employee}: {address}')

def add_employee(employee, address):
    employees[employee] = address

def remove_employee(employee):
    if employee in employees:
        del employees[employee]
        print(f'{employee} був видалений зі списку співробітників.')
    else:
        print(f'{employee} не знайдений у списку співробітників.')

def check_employees(employees_dict, last_names):
    found_employees = []
    for last_name in last_names:
        if last_name in employees_dict:
            found_employees.append((last_name, employees_dict[last_name]))
    
    return found_employees
print('Адреси всіх співробітників:')
print_all_addresses()

add_employee('Кузькін', 'Терещенка 11')
print('Адреси всіх співробітників після додавання нового запису:')
print_all_addresses()

remove_employee('Бабіч')
print('Адреси всіх співробітників після видалення запису:')
print_all_addresses()

last_names_to_check = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]

found_employees = check_employees(employees, last_names_to_check)
if found_employees:
    print("Адреси знайдених співробітників:")
    for last_name, address in found_employees:
        print(f"{last_name}: {address}")
else:
    print("Співробітники не знайдені")