from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
def new_balls():

	global x1, y1, r1, ball1, vx1, vy1
	global x2, y2, r2, ball2, vx2, vy2

	canv.delete('ball1')
	x1 = rnd(100, 700)
	y1 = rnd(100, 500)
	r1 = rnd(30, 50)
	ball1 = canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill = choice(colors), width=0, tag = 'ball1')
	vx1 = rnd(-2, 2)
	vy1 = rnd(-2, 2)

	canv.delete('ball2')
	x2 = rnd(100, 700)
	y2 = rnd(100, 500)
	r2 = rnd(30, 50)
	ball2 = canv.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill = choice(colors), width=0, tag = 'ball2')
	vx2 = rnd(-2, 2)
	vy2 = rnd(-2, 2)

	def move():
		global x1, y1, vx1, vy1
		global x2, y2, vx2, vy2

		canv.move(ball1, vx1, vy1)
		x1 = x1 + vx1
		y1 = y1 + vy1

		canv.move(ball2, vx2, vy2)
		x2 = x2 + vx2
		y2 = y2 + vy2

		root.after(50, move)

		if x1 <= 0 or x1 >= 800:
			vx1 = - vx1
		if y1 <= 0 or y1 >= 600:
			vy1 = - vy1

		if x2 <= 0 or x2 >= 800:
			vx2 = - vx2
		if y2 <= 0 or y2 >= 600:
			vy2 = - vy2		

	move()
	root.after(2000, new_balls)

score = 0

def click(event):
	global score, x1, y1, x2, y2
	if ((event.x - x1) ** 2 + (event.y - y1) ** 2) ** 0.5 <= r1:
		canv.delete('ball1')
		canv.delete('score')
		canv.create_text(750, 50, text=str(score + 1), justify = CENTER, font = "Verdana 14", tag = 'score')
		score = score + 1
		x1 = -1000
	if ((event.x - x2) ** 2 + (event.y - y2) ** 2) ** 0.5 <= r2:
		canv.delete('ball2')
		canv.delete('score')
		canv.create_text(750, 50, text=str(score + 1), justify = CENTER, font = "Verdana 14", tag = 'score')
		score = score + 1
		x2 = -1000


new_balls()
canv.bind('<Button-1>', click)
mainloop()