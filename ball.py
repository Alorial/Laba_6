from tkinter import *
from random import randrange as rnd, choice
import time

def Start():
        print('NAME:')
        name = str(input())
        file = open('Players.txt', 'a')
        file.write(name)
        file.write(' - ')
        file.close()
        
Start()

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg = 'white')
canv.pack(fill = BOTH,expand = 1)

colors = ['red','orange','yellow','green','blue']
score = 0
mistake = 0
Balls = []

class Ball:

        def __init__(self):
                self.x = rnd(100, 700)
                self.y = rnd(100, 500)
                self.r = rnd(30, 50)

                self.Vx = rnd(-2, 2)
                self.Vy = rnd(-2, 2)

                self.obj = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                                            self.y + self.r, fill = choice(colors), width = 2, tag = 'ball')

        def Refraction(self):
                if self.x <= self.r or self.x >= 800 - self.r:
                        self.Vx = - self.Vx
                if self.y <= self.r or self.y >= 600 - self.r:
                        self.Vy = - self.Vy

        def Movement(self):
                self.x = self.x + self.Vx
                self.y = self.y + self.Vy
                canv.move(self.obj, self.Vx, self.Vy)

        def Kill(self):
                canv.delete(self.obj)


        
def Creation():
        global Number
        for i in range(Number):
                Balls.append(Ball())
                        
def Play():
        for i in Balls:
                i.Movement()
                i.Refraction()
        root.after(20, Play)

def New_level():

        global Number
        Number = rnd(1, 5)
        canv.delete('ball')
        Creation()
        Play()

        root.after(2000, New_level)

def click(event):
        global Number, score, mistake
        mistake += 1
        for i in Balls:
                if ((event.x - i.x) ** 2 + (event.y - i.y) ** 2) ** 0.5 <= i.r:
                        score += 1
                        canv.delete('score')
                        canv.create_text(750, 50, text = str(score), justify = CENTER, font = "Verdana 14", tag = 'score')
                        i.Kill()
                        mistake -= 1
        if mistake == 5:
                root.quit()
                print('SCORE:', score)
                print('GAME OVER')
                file = open('Players.txt', 'a')
                file.write(str(score))
                file.write('\n')
                file.close()

canv.bind('<Button-1>', click)

New_level()
mainloop()
