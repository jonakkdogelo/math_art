import pygame
from pygame.locals import *
import numpy as np
from sys import exit
import os
import math

pygame.init()

largura_janela, altura_janela = 800, 700
FPS = 10
raio = 300
pontos_circulo = 8
distroção = 0  #radianos
cor = True

tela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()
def atualizar():
    global listapontos,pontos_circulo
    listapontos = pontos(pontos_circulo)

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        pontos_circulo += 1
    if keys[K_s]:
        pontos_circulo -= 1
    
def pontos(j):
    listapontos = []
    radianos = 2*math.pi/j +j*distroção
    for i in range(j):
        ponto = (largura_janela//2+math.sin(radianos*i) *raio,altura_janela//2+math.cos(radianos*i) *-raio)
        listapontos.append(ponto)
    return listapontos

def desenhar(tela):
    tela.fill((0,0,0))
    for i in range (len(listapontos)):
        for j in range(len(listapontos)):
            if cor == False:
                pygame.draw.line(tela,(200,200,200),(listapontos[i][0],listapontos[i][1]),(listapontos[j][0],listapontos[j][1]))
            else:
                pygame.draw.line(tela,(min(i*2,255),listapontos[i][0]/3,listapontos[i][1]/3),(listapontos[i][0],listapontos[i][1]),(listapontos[j][0],listapontos[j][1]))
        #pygame.draw.rect(tela,(100,100,100),(listapontos[i][0],listapontos[i][1],2,2))
    pygame.draw.circle(tela, (255,255,255), (largura_janela//2,altura_janela//2), raio, 2)
    #pygame.draw.rect(tela,(255,0,0),(400,50,2,2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    xclique = event.pos[0]
                    yclique = event.pos[1]
                    
    atualizar()
    desenhar(tela)
    clock.tick(FPS)
    pygame.display.flip()