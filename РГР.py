import pygame
import random

# Висота та ширина вікна
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class Obstacle:
    def __init__(self, width, height):
        # Генеруємо прямокутник випадковим чином на екрані
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - width), 
                                random.randint(0, SCREEN_HEIGHT - height), width, height)

    def reset_position(self, drone_rect):
        # Перевірка на перетин прямокутників дрона та перешкоди
        while self.rect.colliderect(drone_rect):
            # Якщо є перетин, генеруємо нові координати для перешкоди
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

class Program:
    def __init__(self):
        pygame.init()
        
        # Константи для ініціалізації вікна
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 600
        self.FPS = 30
        
        # Кольори
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 128, 255)
        self.RED = (255, 0, 0)
        
        # Ініціалізація вікна програми
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Drone Interface")
        self.clock = pygame.time.Clock()

        # Параметри дрона
        self.drone_speed = 10
        self.font = pygame.font.Font(None, 36)
        self.num_obstacles = 3
        
        # Початкові координати дрона
        self.drone_rect = pygame.Rect(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2, 50, 50)
        # Створення списку перешкод
        self.obstacles = [Obstacle(200, 50) for _ in range(self.num_obstacles)]
        self.reset_obstacle_positions()
        
        # Змінна для перевірки чи запущенна програма
        self.running = True

    # Функція для скидання позицій перешкод
    def reset_obstacle_positions(self):
        for obstacle in self.obstacles:
            obstacle.reset_position(self.drone_rect)

    # Функція для виходу при натисканні esc
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    # Функція руху дрона
    def move_drone(self, keys):
        if keys[pygame.K_LEFT]:
            self.drone_rect.x -= self.drone_speed
        if keys[pygame.K_RIGHT]:
            self.drone_rect.x += self.drone_speed
        if keys[pygame.K_UP]:
            self.drone_rect.y -= self.drone_speed
        if keys[pygame.K_DOWN]:
            self.drone_rect.y += self.drone_speed

        # Обмеження руху дрона в межах екрану
        self.drone_rect.x = max(0, min(self.drone_rect.x, self.SCREEN_WIDTH - 50))
        self.drone_rect.y = max(0, min(self.drone_rect.y, self.SCREEN_HEIGHT - 50))

    # Функція перевірки зіткнень дрона з перешкодами
    def check_collisions(self):
        for obstacle in self.obstacles:
            if self.drone_rect.colliderect(obstacle.rect):
                # Виведення повідомлення про завершення гри при зіткненні
                text = self.font.render("Гра завершена", True, self.RED)
                self.screen.blit(text, (self.SCREEN_WIDTH // 2 - text.get_width() // 2,
                                        self.SCREEN_HEIGHT // 2 - text.get_height() // 2))
                pygame.display.flip()
                pygame.time.delay(2000)
                self.running = False

    def update_screen(self):
        self.screen.fill(self.WHITE)

        # Відображення дрона та перешкод на екрані
        pygame.draw.rect(self.screen, self.BLUE, self.drone_rect)
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, self.RED, obstacle.rect)

        # Оновлення вікна
        pygame.display.flip()

    # Функція запуску гри
    def run(self):
        while self.running:
            # Обробка натискання esc
            self.handle_input()

            # Отримання натисканих клавіш
            keys = pygame.key.get_pressed()

            # Рух дрона
            self.move_drone(keys)

            # Перевірка зіткнень
            self.check_collisions()

            self.update_screen()

            # Встановлення частоти оновлення екрану
            self.clock.tick(self.FPS)

        # Завершення роботи Pygame при закритті вікна
        pygame.quit()


if __name__ == "__main__":
    # Створення об'єкту гри та його запуск
    game = Program()
    game.run()
