import pygame
import math
import numpy as np
from PIL import Image


# CONFIG

IMAGE_PATH = "input.jpg"

IMG_SIZE = 380          # make lower = faster
WINDOW_SIZE = 900

SPIRAL_TURNS = 180
POINTS_PER_TURN = 220
BASE_RADIUS = 0.8
STROKE_SCALE = 4.0

STEPS_PER_FRAME = 6     # SPEED BOOST try 4–10

BG_COLOR = (10, 10, 10)
LINE_COLOR = (240, 240, 240)
TEXT_COLOR = (160, 160, 160)   
WATERMARK_COLOR = (110, 110, 110)

INFO_TEXT = "Please wait till the artwork completes…"
WATERMARK_TEXT = "© Sarthak Bhopale"


# LOAD IMAGE

img = Image.open(IMAGE_PATH).convert("L")
img = img.resize((IMG_SIZE, IMG_SIZE))
pixels = np.array(img)


# PYGAME INIT

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("One-Stroke Spiral Art")

clock = pygame.time.Clock()

surface = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
surface.fill(BG_COLOR)

# Fonts
info_font = pygame.font.SysFont("Arial", 18)
watermark_font = pygame.font.SysFont("Arial", 12)

info_render = info_font.render(INFO_TEXT, True, TEXT_COLOR)
info_rect = info_render.get_rect(center=(WINDOW_SIZE // 2, 22))

watermark_render = watermark_font.render(WATERMARK_TEXT, True, WATERMARK_COLOR)
watermark_rect = watermark_render.get_rect(
    bottomright=(WINDOW_SIZE - 10, WINDOW_SIZE - 10)
)

cx, cy = WINDOW_SIZE // 2, WINDOW_SIZE // 2


# SPIRAL STATE

theta = 0.0
max_theta = SPIRAL_TURNS * 2 * math.pi
theta_step = (2 * math.pi) / POINTS_PER_TURN

prev_pos = None
drawing_done = False
running = True


# MAIN LOOP

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not drawing_done:
        for _ in range(STEPS_PER_FRAME):
            if theta >= max_theta:
                drawing_done = True
                break

            r = BASE_RADIUS * theta
            cos_t = math.cos(theta)
            sin_t = math.sin(theta)

            x = cx + r * cos_t
            y = cy + r * sin_t

            img_x = int((x - cx) / (WINDOW_SIZE / 2) * (IMG_SIZE / 2) + IMG_SIZE / 2)
            img_y = int((y - cy) / (WINDOW_SIZE / 2) * (IMG_SIZE / 2) + IMG_SIZE / 2)

            if 0 <= img_x < IMG_SIZE and 0 <= img_y < IMG_SIZE:
                brightness = pixels[img_y, img_x] / 255.0
                thickness = max(1, int((1 - brightness) * STROKE_SCALE))

                if prev_pos:
                    pygame.draw.line(surface, LINE_COLOR, prev_pos, (x, y), thickness)

                prev_pos = (x, y)

            theta += theta_step


    # RENDER

    screen.blit(surface, (0, 0))

    if not drawing_done:
        screen.blit(info_render, info_rect)

    screen.blit(watermark_render, watermark_rect)

    pygame.display.flip()
    clock.tick(240)   # high FPS

pygame.quit()
