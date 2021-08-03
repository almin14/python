import webbrowser
import time
from pynput.keyboard import Key,Controller
import urllib
import re
import keyboard

a=0
url = 'https://stackoverflow.com/questions/37769148/how-to-open-chrome-in-incognito-mode-from-python'
for i in range(0,10,1):
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
	webbrowser.get(chrome_path).open_new(url)
	time.sleep(5)
	from pynput.mouse import Button,Controller
	mouse=Controller()
	mouse.scroll(0,-10)
	time.sleep(2)
	mouse.scroll(0,10)
	time.sleep(2)
	from pynput.keyboard import Key,Controller
	keyboard=Controller()
	keyboard.press(Key.ctrl)
	keyboard.press('w')
	keyboard.release('w')
	keyboard.release(Key.ctrl)
	import keyboard
	if keyboard.is_pressed('q'):
		break
	else: 
		pass
