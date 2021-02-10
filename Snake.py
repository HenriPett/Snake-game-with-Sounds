import pygame
import time
import random

pygame.init()

black = (30, 30, 36)
green = (33, 161, 121)
score_green = (185, 210, 177)
pink = (251, 172, 190)
red = (251, 75, 78)

display_width = 800
display_height = 600

clock = pygame.time.Clock()

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Snake game')


snake_block = 10
snake_speed = 20

font_style = pygame.font.SysFont(None, 25)


def play_sound(file_name):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(0)


def blit_score(score):
    message = font_style.render('Pontuação: ' + str(score), True, score_green)
    display.blit(message, [25, 25])


def render_snake(snake_block, snake_list):
    for snake in snake_list:
        pygame.draw.rect(display, green, [
                         snake[0], snake[1], snake_block, snake_block])


def blit_game_over(message, color):
    message = font_style.render(message, True, color)
    display.blit(message, message.get_rect(
        center=(display_width / 2, display_height / 2)))


def loop():
    game_over = False
    game_close = False

    x = display_width / 2
    y = display_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    x_food = round(random.randrange(
        0, display_width - snake_block) / 10) * 10
    y_food = round(random.randrange(
        0, display_height - snake_block) / 10) * 10

    while not game_over:

        while game_close == True:
            display.fill(black)
            blit_game_over(
                "You lose! Press S to quit or J to Play again", red)
            blit_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_j:
                        loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= display_width or x < 0 or y >= display_height or y < 0:
            play_sound(#sound that will play when you lose)
            game_close = True

        x += x_change
        y += y_change

        display.fill(black)

        pygame.draw.rect(
            display, pink, [x_food, y_food, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for snake in snake_list[:-1]:
            if snake == snake_head:
                play_sound(#sound that will play when you eat your own body)
                game_close = True

        render_snake(snake_block, snake_list)

        blit_score(snake_length - 1)

        pygame.display.update()

        if x == x_food and y == y_food:
            x_food = round(random.randrange(
                0, display_width - snake_block) / 10) * 10
            y_food = round(random.randrange(
                0, display_height - snake_block) / 10) * 10
            snake_length += 1
            play_sound(#sound that will play when you eat)

            if (snake_length - 1) == 10:
                play_sound(#sound that will play when you score 10 points)
            if (snake_length - 1) == 15:
                play_sound(#sound that will play when you score 15 points)
            if (snake_length - 1) == 20:
                play_sound(#sound that will play when you score 20 points)

        reward = 0
        if snake_length >= 1:
            reward += 10
        elif game_close == True:
            reward -= 10
        else:
            reward = 0


        clock.tick(snake_speed)

    pygame.quit()
    quit()


loop()
