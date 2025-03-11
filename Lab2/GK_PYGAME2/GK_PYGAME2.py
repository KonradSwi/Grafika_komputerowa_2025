import pygame

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
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)

# Œrodek ekranu
center_x, center_y = 300, 300
radius = 200  # Promieñ ko³a
square_size = 200  # Rozmiar kwadratu

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(BIALY)  # Wype³nienie t³a na bia³o

    # Rysowanie czarnego ko³a
    pygame.draw.circle(win, CZARNY, (center_x, center_y), radius)

    # Rysowanie ¿ó³tego kwadratu wewn¹trz ko³a
    square_x = center_x - square_size // 2
    square_y = center_y - square_size // 2
    pygame.draw.rect(win, ZOLTY, (square_x, square_y, square_size, square_size))

    pygame.display.update()

pygame.quit()