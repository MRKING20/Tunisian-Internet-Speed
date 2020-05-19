import pygame
import speedtest
import socket
import tkinter
from tkinter import messagebox

pygame.init()
win = pygame.display.set_mode((384,539))
win.fill((0,0,0))
black_color = (0,0,0)
white_color = (255,255,255)
gris_color = (59,59,59)
red = (229,67,45)
yellow = (236,199,76)

pygame.display.set_caption("Tunisian Internet Speed")
icon = pygame.image.load("Tunisian Internet Speed icon.png")
pygame.display.set_icon(icon)

police = pygame.font.Font("police.otf", 20)
police1 = pygame.font.Font("police.otf", 35)
police2 =  pygame.font.SysFont("arial", 20)
police3 = pygame.font.Font("police.otf", 8)
police4 =  pygame.font.SysFont("arial", 8)

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x,self.y,self.width,self.height))

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),2)

        if self.text != '':
            font = pygame.font.Font("police.otf", 70)
            text = font.render(self.text, 1, red)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def redrawWindow():
    win.fill(gris_color)
    blueButton.draw(win)


try :
    test = speedtest.Speedtest()
    Download =test.download()/1024/1024
    Upload = test.upload()/1024/1024
    servernames = []
    test.get_servers(servernames)
    Ping = test.results.ping
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname) 
except:
    app = tkinter.Tk()
    app.withdraw()
    messagebox.showwarning("ERREUR !", "Please check your connection")


run = True
blueButton = button(yellow,65,200,250,100,"Start")

while run:

    redrawWindow()
    rec1 = pygame.Rect(0,400,100,150)
    pygame.draw.rect(win, yellow, rec1,2)
    rec2 = pygame.Rect(100,400,142,155)
    pygame.draw.rect(win, yellow, rec2,2)
    rec3 = pygame.Rect(241,400,142,155)
    pygame.draw.rect(win,yellow, rec3,2)
    
    
    text_name_of_desktop = police3.render("Your Computer Name is :", True, white_color)
    win.blit(text_name_of_desktop,[0,0])
    text_name_of_desktop = police3.render(f"{hostname}", True, white_color)
    win.blit(text_name_of_desktop,[112,0])
    text_ip = police3.render("Your Computer IP Address is :", True, white_color)
    win.blit(text_ip,[0,8])
    text_ip = police3.render(f"{IP}", True, white_color)
    win.blit(text_ip,[135,8])
    text_name = police4.render("Created by :", True, white_color)
    win.blit(text_name,[333,0])
    text_name = police4.render("Mabrouk Nidhal", True, white_color)
    win.blit(text_name,[333,9])

    if blueButton.clicked:
        
        text_ping = police.render("Ping", True, white_color)
        win.blit(text_ping,[25,415])
        text_ping = police1.render(f"{Ping : .0f}", True, white_color)
        win.blit(text_ping,[17,450])
        text_ping = police2.render("ms", True, white_color)
        win.blit(text_ping,[38,500])
        text_download = police.render("Download", True, white_color)
        win.blit(text_download,[110,415])
        text_download = police1.render(f"{Download :.2f}", True, white_color)
        win.blit(text_download,[140,450])
        text_download = police2.render("Mbps", True, white_color)
        win.blit(text_download,[155,500])
        text_download = police.render("Upload", True, white_color)
        win.blit(text_download,[270,415])
        text_download = police1.render(f"{Upload :.2f}", True, white_color)
        win.blit(text_download,[275,450])
        text_download = police2.render("Mbps", True, white_color)
        win.blit(text_download,[290,500])
        


    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if blueButton.isOver(pos):
                print('clicked Button')
                blueButton.clicked = not blueButton.clicked

        if event.type == pygame.MOUSEMOTION:
            if blueButton.isOver(pos):
                blueButton.color = red
            else:
                blueButton.color = yellow


    pygame.display.update()
