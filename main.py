import pygame  # import library

pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/forest-assets/door.png').convert()
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  win.fill((0, 0, 0))


  win.blit(img, (400, 300))
  # Draw a rectangle

  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
