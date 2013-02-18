import pygame, time

pygame.init()

soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()

time.sleep(1)
soundObj.stop()