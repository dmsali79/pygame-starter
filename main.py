import pygame  # import library

pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))

# Create the font
font = pygame.font.SysFont("arial", 72)
bfont = pygame.font.SysFont("arial", 52)
cfont = pygame.font.SysFont("arial", 42)

text = font.render("The Room.", True, (255, 100, 10))
btext = bfont.render("The Room.", True, (175, 50, 5))
ctext = cfont.render("The Room.", True, (40, 1, 1))

img = pygame.image.load('C:/Users/dmsali79/Downloads/dungeon_tiles.png').convert()
bimg = pygame.image.load('assets/forest-assets/floor.png')
cimg = pygame.image.load('assets/forest-assets/wall-e-1.png')

c1img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c2img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c3img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c4img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c5img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c6img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c7img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c8img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c9img = pygame.image.load('assets/forest-assets/wall-e-1.png')
c10img = pygame.image.load('assets/forest-assets/wall-e-1.png')

dimg = pygame.image.load('assets/forest-assets/door.png')
eimg = pygame.image.load('assets/forest-assets/stairs.png')
fimg = pygame.image.load('assets/forest-assets/wall-e-2.png')

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  win.fill((0, 0, 0))
  
  win.blit(text, (100, 1))
  win.blit(btext, (100, 60))
  win.blit(ctext, (75, 110))

  win.blit(img, (400, 300))
  win.blit(bimg, (200, 300))
  
  win.blit(cimg, (300, 230))
  win.blit(c1img, (300, 255))
  win.blit(c2img, (300, 270))
  win.blit(c3img, (300, 285))
  win.blit(c4img, (300, 300))
  win.blit(c5img, (300, 315))
  win.blit(c6img, (300, 330))
  win.blit(c7img, (300, 345))
  win.blit(c8img, (300, 360))
  win.blit(c9img, (300, 375))
  win.blit(c10img, (300, 390))
  
  win.blit(dimg, (300, 210))
  win.blit(eimg, (300, 400))
  win.blit(fimg, (300, 250))



  # Draw a rectangle

  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
