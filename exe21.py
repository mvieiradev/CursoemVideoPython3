#Tocando um MP3
import pygame
pygame.init()
pygame.mixer.music.load('blinding.mp3')
pygame.mixer.music.play()
pygame.event.wait()