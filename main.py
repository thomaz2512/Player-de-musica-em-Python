import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("System") #Aplica o modo de luz de acordo com o sistema
customtkinter.set_appearance_mode("blue")

root = customtkinter.CTk()  #Inicializa a tela
root.title('Baronify')  #Nome na tela
root.geometry('410x480')    #Nome da tela
pygame.mixer.init()

lista_de_musica = ['music/']
album_de_musica = ['music/']
n = 1

def get_album(som_nome, n):
    image1 = Image.open(lista_de_musica[n])
    image2 = image1.resize((250,250))
    load = tkinter.label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)


def progresso():
    a = pygame.mixer.Sound(f{lista_de_musica[n]})
    som_len = a.get_length() * 3
    for i in range(0, math.ceil(som_len)):
        time.sleep(.3)
        progressobar.set(pygame.mixer.music.get_pos() / 1000000)

def threading():
    t1 = Thread(target=progresso)
    t1.start()

def play_music():
    threading()
    global n
    musica_atual = n
    if n > 2:
        n = 0
    nome_som = lista_de_musica[n]
    pygame.mixer.music.load(nome_som)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album(nome_som, n)

    print("play")
    n += 1

def skip_f():
    print(">")

def skip_b():
    print("<")

def volume(value):
    #print(value)
    pygame.mixer.music.set_volume(value)






# Botões
Play_button = customtkinter.CTkButton(master=root, text="Play", command=play_music)
Play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text=">", command=skip_f, width=2)
skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text="<", command=skip_b, width=2)
skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

volume = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=120)
volume.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progresso = customtkinter.CTkProgressBar(master=root, progress_color="green", width=250)
progresso.place(relx=.5, rely=.85, anchor=tkinter.CENTER)





root.mainloop()