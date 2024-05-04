import turtle

class Hexagon:
    def __init__(self, side_length, x=0, y=0):
        """
        Конструктор класу
        """
        self.side_length = side_length
        self.x = x
        self.y = y

    def draw(self):
        """
        Метод для малювання шестикутника за допомогою бібліотеки Turtle.
        """
        turtle.penup()
        turtle.goto(self.x, self.y - self.side_length)
        turtle.pendown()

        for _ in range(6):
            turtle.forward(self.side_length)
            turtle.right(60)


    def move(self, new_x, new_y):
        """
        Метод для переміщення шестикутника на нові координати
        """
        self.x = new_x
        self.y = new_y
        turtle.clear()
        self.draw()  # Малюємо шестикутник на нових координатах

    def hide(self):
        """
        Метод для приховання шестикутника.
        """
        turtle.hideturtle()

    def show(self):
        """
        Метод для відображення шестикутника.
        """
        turtle.showturtle()


# Створюємо три екземпляри класу Hexagon
hexagon1 = Hexagon(20, 0, 50)
hexagon2 = Hexagon(40, 60, 50)
hexagon3 = Hexagon(60, 150, 50)

# Демонструємо виклик конструктора та роботу методів
hexagon1.draw()
hexagon2.draw()
hexagon3.draw()

# Переміщаємо шестикутники на нові координати
hexagon1.move(50, 20)
hexagon2.move(90, 100)
hexagon3.move(150, 150)

# Приховуємо шестикутники
hexagon1.hide()
hexagon2.hide()
hexagon3.hide()


# Відображаємо шестикутники
hexagon1.show()
hexagon2.show()
hexagon3.show()

turtle.done()