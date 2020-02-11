import pygame  # import library

pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))

# Create the font
font = pygame.font.SysFont("arial", 72)
bfont = pygame.font.SysFont("arial", 52)
cfont = pygame.font.SysFont("arial", 42)

text = font.render("The Room.", True, (255, 100, 10))
btext = bfont.render("The Room.", True, (220, 80, 5))
ctext = cfont.render("The Room.", True, (180, 60, 1))

img = pygame.image.load('C:/Users/dmsali79/Downloads/dungeon_tiles.png').convert()

img = pygame.image.load('assets/forest-assets/floor.png')

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  win.fill((0, 0, 0))
  
  win.blit(text, (125, 1))
  win.blit(btext, (100, 20))
  win.blit(ctext, (75, 40))


  win.blit(img, (400, 300))
  # Draw a rectangle

  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
