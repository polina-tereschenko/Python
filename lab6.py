import tkinter as tk
from tkinter import simpledialog

# Створюємо клас, в якому метод __init__, котрому передаємо значення parent, 
# й його присвоюємо до self.parent а self.result = пусте значення
# також метод get_data котрий приймає дані й якщо вони не пусте значення, то закриває вікно, 
# якщо пусте значення то автоматично скасовує введення

class UserInputData:
    def __init__(self, parent):
        self.parent = parent
        self.result = None

    def get_data(self):
        input_data = simpledialog.askstring("Input", "Enter your data:")
        if input_data is not None and input_data != "":
            self.result = input_data
            self.parent.destroy()
        else:
            self.result = None 
            self.parent.destroy()

def main():
    root = tk.Tk()
    root.title("User Input Dialog")

    user_input_dialog = UserInputData(root)

    # Виклик функції для показу вікна
    user_input_dialog.get_data()

    # Після завершення діалогу виводить данні введені користувачем
    user_data = user_input_dialog.result

    # Виведення повідомлення у потік stdout
    if user_data is not None:
        print("Користувач ввів дані:", user_data)
    else:
        print("Користувач скасував введення.")

    root.mainloop()

if __name__ == "__main__":
    main()
