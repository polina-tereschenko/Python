class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_income(self):
        return 0

    def get_expenses(self):
        return 0  

class Preschooler(Human):
    def __init__(self, name, age, gender, guardian):
        super().__init__(name, age, gender)
        self.guardian = guardian

    def get_income(self):
        return 0

    def get_expenses(self):
        return 5000  # Витрати на дошкільну освіту батьками

class Schoolkid(Human):
    def __init__(self, name, age, gender, school):
        super().__init__(name, age, gender)
        self.school = school

    def get_income(self):
        return 500  # Стипендія школяра

    def get_expenses(self):
        return  500 # Витрати школяря

class Student(Human):
    def __init__(self, name, age, gender, university):
        super().__init__(name, age, gender)
        self.university = university

    def get_income(self):
        return 1000  # Стипендія студента

    def get_expenses(self):
        return 700  # Витрати студента

class Employee(Human):
    def __init__(self, name, age, gender, job_title):
        super().__init__(name, age, gender)
        self.job_title = job_title

    def get_income(self):
        return 1000  # Зарплата працівника

    def get_expenses(self):
        return 500  # Побутові витрати

# Демонстрація роботи класів
choice = input("Виберіть тип об'єкта (дошкільник, школяр, студент, працівник): ")
if choice == "дошкільник":
    p = Preschooler("Анна", 5, "жінка", "мама")
    print(f"{p.name} - Дохід: {p.get_income()}, Витрати: {p.get_expenses()}")
elif choice == "школяр":
    s = Schoolkid("Максим", 12, "чоловік", "Школа №5")
    print(f"{s.name} - Дохід: {s.get_income()}, Витрати: {s.get_expenses()}")
elif choice == "студент":
    st = Student("Ірина", 20, "жінка", "Університет")
    print(f"{st.name} - Дохід: {st.get_income()}, Витрати: {st.get_expenses()}")
elif choice == "працівник":
    e = Employee("Олег", 30, "чоловік", "Програміст")
    print(f"{e.name} - Дохід: {e.get_income()}, Витрати: {e.get_expenses()}")
else:
    print("Невідомий тип об'єкта")
