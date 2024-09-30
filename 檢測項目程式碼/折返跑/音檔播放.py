"""
import os
os.system("a.m4a")
"""
import pygame
pygame.init()
pygame.mixer.init()
track=pygame.mixer.music.load("voice.mp3")
pygame.mixer.music.play()