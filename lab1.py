class Room:
    """description room"""
    def __init__(self, length, width, height_in_m, window_length, window_width, door_length, door_width):
        self.length = length
        self.width = width
        self.height_in_m = height_in_m
        self.window_length = window_length
        self.window_width = window_width
        self.door_length = door_length
        self.door_width = door_width

    def square_wall_1(self):
        return self.length * self.height_in_m
    
    def square_wall_2(self):
        return self.length * self.height_in_m 
    
    def square_room(self):
        return self.square_wall_1() + self.square_wall_2()
    
    def square_room_without_window(self):
        return self.square_room() - (self.window_length * self.window_width)
    
    def square_room_without_door(self):
        return self.square_room() - (self.door_length * self.door_width)
    
    def square_room_without_door_and_window(self):
        return self.square_room() - ((self.window_length * self.window_width) + (self.door_length * self.door_width))

a = float(input("length = "))
b = float(input("width = "))
c = float(input("height_in_m = "))
window_length = 2
window_width = 15
door_length = 2
door_width = 8

answer_2 = input("Ви впевнені що вказали правильно параметри?\n")
if answer_2 == "no":
    e = input("Який об'єкт хочете переписати?\n")
    if e == "length":
        a = float(input("length = "))
    elif e == "width":
        b = float(input("width = "))
    elif e == "height_in_m":
        c = float(input("height_in_m = "))

    t = Room(a, b, c, window_length, window_width, door_length, door_width)
    print("Площа кімнати =", t.square_room())
    print("Площа кімнати без вікон та дверей:", t.square_room_without_door_and_window())

elif answer_2 == "yes":
    answer = input("Хочете видалити об'єкт?\n")
    if answer == "yes":
        f = input("Який об'єкт?\n")
        if f == "length":
            a = 0
        elif f == "width":
            b = 0
        elif f == "height_in_m":
            c = 0

        t = Room(a, b, c, window_length, window_width, door_length, door_width)
        print(f"Видалено об'єкт {f}")

        if (f == a, c): 
            print("     Ви не можете порахувати площу кімнати без об'єкту", f)

    else:
        t = Room(a, b, c, window_length, window_width, door_length, door_width)
        print("Площа кімнати =", t.square_room())
        print("Площа кімнати без вікон та дверей:", t.square_room_without_door_and_window())