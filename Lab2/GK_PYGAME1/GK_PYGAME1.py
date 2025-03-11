import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0, 0, 0)
BIALY=(255,255,255)

# Œrodek i promieñ 13-k¹ta
center = (300, 300)
radius = 150
num_sides = 13

# Obliczanie wierzcho³ków
def calculate_vertices(center, radius, num_sides, angle_offset=0):
    vertices = []
    for i in range(num_sides):
        angle = 2 * math.pi * i / num_sides + angle_offset  # K¹t w radianach
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        vertices.append((x, y))
    return vertices

# Pierwotne wierzcho³ki
original_vertices = calculate_vertices(center, radius, num_sides)

# Aktualna lista wierzcho³ków
vertices = original_vertices.copy()

# Transformacje
def scale_polygon(vertices, scale_x, scale_y):
    return [(int(center[0] + (x - center[0]) * scale_x),
             int(center[1] + (y - center[1]) * scale_y)) for x, y in vertices]

def rotate_polygon(vertices, angle):
    angle = math.radians(angle)
    return [(int(center[0] + (x - center[0]) * math.cos(angle) - (y - center[1]) * math.sin(angle)),
             int(center[1] + (x - center[0]) * math.sin(angle) + (y - center[1]) * math.cos(angle))) for x, y in vertices]

def shear_polygon(vertices, shear_factor):
    return [(x + int(shear_factor * (y - center[1])), y) for x, y in vertices]

def shear_polygon_vertical(vertices, shear_factor):
    return [(x, y + int(shear_factor * (x - center[0]))) for x, y in vertices]


def stretch_and_lift(vertices, stretch_x, lift_y):
    return [(int(center[0] + (x - center[0]) * stretch_x), y - lift_y) for x, y in vertices]

def flip_and_rotate_180(vertices):
    return [(2 * center[0] - x, 2 * center[1] - y) for x, y in vertices]  # Obrót o 180° + odbicie

def lower_polygon(vertices, amount):
    return [(x, y + amount) for x, y in vertices]

def move_polygon_x(vertices, amount):
    return [(x + amount, y) for x, y in vertices]

def reset_polygon():
    global vertices
    vertices = original_vertices.copy()

# Pêtla gry
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Zmniejszenie
                vertices = scale_polygon(vertices, 0.5, 0.5)
            elif event.key == pygame.K_2:  # Obrót
                vertices = rotate_polygon(vertices, 45)
            elif event.key == pygame.K_3:  # Przeskalowanie
                vertices = flip_and_rotate_180(vertices)  # Obrót i efekt lustrzany
                vertices = scale_polygon(vertices, 0.5, 1)  # Zwê¿enie (X 0.7, Y bez zmian)
            elif event.key == pygame.K_4:  # Efekt no¿ycowy
                vertices = shear_polygon(vertices, 0.5)
            elif event.key == pygame.K_5:  # Podniesienie i rozci¹gniêcie
                vertices = stretch_and_lift(vertices, 1.5, 150)
            elif event.key == pygame.K_6:  # Efekt no¿ycowy i Obrót
                vertices = rotate_polygon(vertices, 90)
                vertices = shear_polygon_vertical(vertices, 0.5)
            elif event.key == pygame.K_7:  # Obrót o 180° + zwê¿enie
                vertices = rotate_polygon(vertices, 180)
                vertices = scale_polygon(vertices, 0.5, 1)
            elif event.key == pygame.K_8:  # Obrót o 45° + zwê¿enie y
                vertices = scale_polygon(vertices, 1, 0.5)
                vertices = rotate_polygon(vertices, 45)
                vertices = lower_polygon(vertices, 150)
                vertices = move_polygon_x(vertices, -100)
            elif event.key == pygame.K_9:  # Obrót o 180°, efekt no¿ycowy i przecuniêcie
                vertices = rotate_polygon(vertices, 180)
                vertices = shear_polygon(vertices, 0.5)
                vertices = move_polygon_x(vertices, 150)
            elif event.key == pygame.K_0:  # Reset
                reset_polygon()

    win.fill(CZARNY)

    # rysowanie 13-k¹ta foremnego
    pygame.draw.polygon(win, NIEBIESKI, vertices, 0)


    pygame.display.update()

pygame.quit()