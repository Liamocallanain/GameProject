#https://www.geeksforgeeks.org/python-display-images-with-pygame/

# importing required library
import pygame
 
# activate the pygame library .
pygame.init()
X = 600
Y = 600
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('My Game')
 
# create a surface object, image is drawn on it.
img = pygame.image.load("images\\10_of_clubs.png") # \ must be escaped with \\
 
# Using blit to copy content from one surface to other
scrn.blit(img, (100,100))
 
# paint screen one time
pygame.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()