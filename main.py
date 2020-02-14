import pygame  # import library

pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))

# Create the font
font = pygame.font.SysFont("arial", 72)
bfont = pygame.font.SysFont("arial", 52)
cfont = pygame.font.SysFont("arial", 42)

x = 200
y = 200

text = font.render("The Room...", True, (255, 100, 10))
btext = bfont.render("The Room...", True, (138, 68, 5))
ctext = cfont.render("The Room.", True, (115, 64, 15))

hero = pygame.image.load('assets/hero/sliced/idle-1.png')



img = pygame.image.load('assets/forest-assets/spooky_trees.png')
bimg = pygame.image.load('assets/forest-assets/floor.png')
cimg = pygame.image.load('assets/forest-assets/wall-e-1.png')
dimg = pygame.image.load('assets/forest-assets/door.png')
eimg = pygame.image.load('assets/forest-assets/stairs.png')
fimg = pygame.image.load('assets/forest-assets/wall-e-2.png')

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  
  
  
  
  
  win.fill((158, 115, 55))
  
  keys = pygame.key.get_pressed()



  win.blit(text, (100, 1))
  win.blit(btext, (105, 60))
  win.blit(ctext, (110, 110))

  win.blit(img, (365, 185))
  win.blit(img, (60, 200))
  
  win.blit(bimg, (200, 350))
  
    
  

  win.blit(cimg, (300, 280))
  win.blit(cimg, (300, 305))
  win.blit(cimg, (300, 320))
  win.blit(cimg, (300, 335))
  win.blit(cimg, (300, 350))
  win.blit(cimg, (300, 365))
  win.blit(cimg, (300, 380))
  win.blit(cimg, (300, 395))
  win.blit(cimg, (300, 410))
  win.blit(cimg, (300, 425))
  win.blit(cimg, (300, 440))




  win.blit(dimg, (300, 260))
  win.blit(eimg, (300, 450))
  win.blit(fimg, (300, 300))
  win.blit(hero,(x, y))
  
  keys = pygame.key.get_pressed()

 


  







  if keys[pygame.K_LEFT]:
    hero = pygame.image.load('assets/hero/sliced/walk-4.png')
    x -= 0.2
    
  
    win.blit(hero, (x, y))
  

 
  if keys[pygame.K_RIGHT]:
    
    hero = pygame.image.load('assets/hero/sliced/swim-1.png')
    x += 0.2
    
   
    win.blit(hero, (x, y))
  
  if keys[pygame.K_UP]:
    hero = pygame.image.load('assets/hero/sliced/surprise.png')
    y -=0.2
    

    win.blit(hero, (x,y))
  
  if keys[pygame.K_DOWN]:
    hero = pygame.image.load('assets/hero/sliced/peace.png')
    y +=0.2
    win.blit(hero, (x,y))
  
  if x >790:
    x = 790
  if x <20:
    x = 20
  if y > 580:
    y=580
  if y < 1:
    y = 1
  # Draw a rectangle

  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
