import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/target.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target2.png')
target_width = 80
target_heigth = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_heigth)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Шрифт для отображения количества попаданий
font = pygame.font.SysFont(None, 36)
hits = 0  # Количество попаданий

target_timer = 0  # Таймер для изменения положения цели

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_heigth:
                hits += 1  # Увеличиваем количество попаданий
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_heigth)

    current_time = pygame.time.get_ticks()
    # Проверяем, прошло ли 2 секунды (2000 миллисекунд)
    if current_time - target_timer > 2000:
        target_timer = current_time  # Сбрасываем таймер
        target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Изменяем положение цели
        target_y = random.randint(0, SCREEN_HEIGHT - target_heigth)

    screen.blit(target_img, (target_x, target_y))

    # Создаем изображение для отображения количества попаданий
    hits_text = font.render(f'Попадания: {hits}', True, (0, 0, 0))

    screen.blit(hits_text, (10, 10))  # Отрисовываем текст на экране

    pygame.display.update()

    pass

pygame.quit()
