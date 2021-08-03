import webbrowser
import time
from pynput.keyboard import Key,Controller
import urllib
import re
import keyboard

urls = 'https://humanbenchmark.com/tests/aim'
for b in range(0,10,1):
	webbrowser.open(urls,new=0)
	time.sleep(3)
	from pynput.mouse import Button,Controller
	mouse=Controller()
	mouse.position=(950,417)
	mouse.click(Button.left)
	time.sleep(1)
	mouse.position=(440,251)
	x=440
	y=251
	for a in range(0,30,1):
		for y in range(251,555,25):
			for x in range(440,1361,25):
				mouse.position = (x,y)
				mouse.click(Button.left)
				if keyboard.is_pressed('q'):
					break
				else: 
					pass



mouse.position=(1361,555)