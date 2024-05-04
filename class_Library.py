import shelve

# Створюємо клас Library, в ньому метод __init__, в який передаємо ім'я та адресу та кількість книг, 
# додаємо метод output_information котрий виводить ім'я та адресу та кількість книг

class Library:
    def __init__(self, name, address, genres_of_books):
        self.name = name
        self.address = address
        self.genres_of_books = genres_of_books

    def output_information(self):
        print(f"Library: {self.name}, Address: {self.address}")
        print(f"Genres of books: {self.genres_of_books}")

# Створюємо функцію add_library та додає бібліотеку, якщо такої ще немає в даних shelve

def add_library():
    while True:
        key = input("Which library do you want to add?: ")
        with shelve.open('library_db') as shelf:
            if key in shelf:
                print("A library with that name already exists.")
            else:
                name = input("Enter library name: ")
                address = input("Enter library address: ")
                genres_of_books = input(f"Enter genres of books for {name} library: ")

                library = Library(name, address, genres_of_books)
                shelf[key] = library
                print("Library added")
                break

# Створюємо функцію котра виводить інформацію про бібліотеку за ключем(назвою) котрий бере з shelf

def output_libraries():
    with shelve.open('library_db') as shelf:
        for key, library in shelf.items():
            print(f"Key: {key}")
            library.output_information()
            print("\n")

# Створюємо список функцій котрі може обрати користувач за своїм бажанням

def output_menu():
    print("1. Add Library\n"
          "2. Display Library Information by Key\n"
          "3. Display Information for All Libraries\n"
          "4. Exit")

# Функція в котрій починається цикл й поки користувач не натисне 4, він не закінчиться

def main():
    while True:
        output_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_library()
        elif choice == '2':
            key = input("Enter the key to search for a library: ")
            with shelve.open('library_db') as shelf:
                if key in shelf:
                    library = shelf[key]
                    library.output_information()
                else:
                    print("Library with that key not found.")
        elif choice == '3':
            output_libraries()
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
