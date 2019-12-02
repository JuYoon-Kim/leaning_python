
from tkinter import*

window = Tk()

b1 = Button(window, text = "One")
b2 = Button(window, text = "Two")
b3 = Button(window, text = "Three")
b4 = Button(window, text = "Four")

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 1, column = 0)
b4.grid(row = 1, column = 1)

Label(window,text="박스 #1", bg="red",fg="white").pack()
Label(window,text="박스 #2", bg="green",fg="black").pack()
Label(window,text="박스 #3", bg="blue",fg="white").pack()

def checked(i):
   global player
   button = list[i]

   if button["text"] != "   ":
      return
   button["text"] = "   " + player + "   "
   button["bg"] = "yellow"
   if player == "X":
      player = "O"
      button["bg"] = "yellow"
   else:
      player = "X"
      button["bg"] = "lightgreen"

player = "X"
list = []

for i in range(9):
   b = Button(window,text="   ",command=lambda k=i: checked(k))
   b.grid(row=i // 3,column=i % 3)
   list.append(b)

import tkinter as tk

def startTimer():
	if(running):
		global timer
		timer += 1
		timeText.configure(text=str(timer))

	window.after(10,startTimer)

def start():
	global running
	running = True

def stop():
	global running
	running = False

running = False

window = tk.Tk()

timer = 0

timeText = tk.Label(window,text ='0',font=('Helvetica',80))
timeText.pack()

startButton = tk.Button(window,text='시작',bg='yellow',command=start)
startButton.pack(fill = tk.BOTH)

stopButton = tk.Button(window,text='중지',bg='yellow',command=stop)
stopButton.pack(fill = tk.BOTH)

startTimer()

def callback(event):
	print(event.x,event.y,"에서 마우스 이벤트 발생")

frame = Frame(window,width=100,height=100)
frame.bind("<Button-1>",callback)
frame.pack()

def key(event):
	print(repr(event.char),"가 눌렸습니다.")

def callback(event):
	frame.focus_set()
	print(event.x,event.y,"에서 마우스 이벤트 발생")

frame = Frame(window,width=100,height=100)
frame.bind("<Key>",key)
frame.bind("<Button-1>",callback)
frame.pack()

window.mainloop()