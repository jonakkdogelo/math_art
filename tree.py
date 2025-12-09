import pygame
import pygame.gfxdraw
from pygame.locals import *
import numpy as np
from sys import exit
import os
import math

pygame.init()

largura_janela, altura_janela = 1600, 800
FPS = 2
lista_pontos = [(largura_janela//2,altura_janela)]
tamanho_inicial = 100
tamanho = tamanho_inicial
lista_tamanhos = [(0,tamanho)]
proporção = 1.33
anglo = math.radians(5)       #2*math.pi/11                     
termo = 0
termo_limite = 8
largura = False

tela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

def atualizar():
    global tamanhoy,tamanho,termo,lista_atual, lista_mae,lista_tamanhos
    
    lista_mae = []
    anglo1 = anglo*termo
    tamanhos_futuros = []
    if termo >= termo_limite:
        input()
    for i in range(len(lista_pontos)):
        #tamanhox1 = tamanho*math.sin(anglo1)
        #tamanhox2 = tamanho*math.sin(-anglo1)
        tamanhox1 = lista_tamanhos[i][0]+lista_tamanhos[i][1]*math.sin(anglo1)
        tamanhox2 = lista_tamanhos[i][0]+lista_tamanhos[i][1]*math.sin(-anglo1)
        tamanhoy =  tamanho*math.cos(anglo1)  #lista_tamanhos[i][1]+ lista_tamanhos[i][0]      
        lista_atual = []
        ponto_atual = lista_pontos[i]
        proximo_pontox1 = ponto_atual[0] + tamanhox1
        proximo_pontox2 = ponto_atual[0] + tamanhox2 
        proximo_pontoy = ponto_atual[1] - tamanhoy
        lista_atual.append((proximo_pontox1,proximo_pontoy))
        if termo != 0:
            lista_atual.append((proximo_pontox2,proximo_pontoy))
        lista_mae.append(lista_atual)
        tamanhos_futuros.append((tamanhox1,tamanhoy))
        tamanhos_futuros.append((tamanhox2,tamanhoy))
    lista_tamanhos = list(tamanhos_futuros)
    tamanho = tamanho/proporção
    termo += 1



def desenhar(tela):
    global lista_pontos
    for i in range(len(lista_pontos)):
        try:
            1 == 1
            #pygame.draw.rect(tela,(255,0,0),(lista_pontos[i][0],lista_pontos[i][1],2,2))
        except:
            1 == 1
        try:
            pygame.draw.line(tela,(250,250,250),lista_pontos[i],lista_mae[i][0],(8- (termo if termo != 0 else 1)if largura==True else 1))
            pygame.draw.line(tela,(250,250,250),lista_pontos[i],lista_mae[i][1],(8- (termo if termo != 0 else 1)if largura==True else 1))
        except:
            1 == 1
    lista_pontos = []
    for i in range(len(lista_mae)):
        lista_pontos.append(lista_mae[i][0])
        try:
            lista_pontos.append(lista_mae[i][1])
        except:
            1 == 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
    atualizar()
    desenhar(tela)
    clock.tick(FPS)
    pygame.display.flip()