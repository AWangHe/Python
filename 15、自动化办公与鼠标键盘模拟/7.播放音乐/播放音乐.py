# -*- coding: utf-8 -*-
#pip install pygame
import time
import pygame

#音乐路径
filePath = r"F:\Python\data\15、自动化办公与鼠标键盘模拟\7.播放音乐\001.mp3"
#初始化
pygame.mixer.init()
#加载音乐
track = pygame.mixer.music.load(filePath)
#播放
pygame.mixer.music.play()

time.sleep(60)
#停止
pygame.mixer.music.stop()


























