import pygame, time

pygame.init()

soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()

pygame.mixer.music.load('rain-01.mp3')
pygame.mixer.music.play(-1,0.0)


time.sleep(2)
soundObj.stop()
pygame.mixer.music.stop()