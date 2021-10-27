from tkinter import *
import pyautogui as cursor
import time as t
import random


window = Tk()
window.title("Mouse Mover")
window.geometry('200x200')

moving = True

def startClicked():
	print("Your mouse will start moving now.")
	global moving
	moving = True
	if moving==True:
		logic()


def stopClicked():
	print("Your mouse will stop moving now.")
	window.destroy()

def logic():
	#Allow for a maximum idle time of 30 seconds for the cursor
	idle_max = 30

	#Store the current position of the cursor
	currentx_cord, currenty_cord = cursor.position()

	#Infinite Loop
	next_x = 500
	while True:
		#Current position of cursor
		# to_x, to_y = cursor.position()

		#Generate two random coordinates
		# randomx = random.randrange(1, 1919)
		# randomy = random.randrange(1, 1079)

		#Generate a random idle time
		idletime = random.randint(1, idle_max)
		print("Your cursor will be idle for {}".format(idletime))
		sleeping_seconds.configure(text=" {}".format(idletime))

		#Move the cursor
		# if(to_x != currentx_cord):
		# 	print("Mouse moved")
		# else:
		print("Moving Mouse")
		# cursor.moveTo(randomx, randomy, 2)
		cursor.click(x=next_x, y=1, clicks=1)
		movement_label.configure(text="Moving!")

		# currentx_cord = randomx
		# currenty_cord = randomy

		print("Sleeping... zzz... zzz")
		movement_label.configure(text=" ")
		t.sleep(iid)
		print("~~~~~~~~~~~~")
		if (next_x == 500):
			next_x = 600
		else:
			next_x = 500


title_label = Label(window, text="Mouse Mover")
sleeping_label = Label(window, text = "Sleeping for: ")
sleeping_seconds = Label(window, text = " ")
movement_label = Label(window, text = " ")

#Formatted Labels
title_label.grid(column=1, row=0)
sleeping_label.grid(column=0, row=2)
sleeping_seconds.grid(column=1, row=2)
movement_label.grid(column=1, row=4)

#Created Buttons
startButton = Button(window, text="Start", command=startClicked)
stopButton = Button(window, text="Stop", command=stopClicked)

#Formatted Buttons
startButton.grid(column=0, row=3)
stopButton.grid(column=3, row=3)

window.mainloop()