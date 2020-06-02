import mouse
import keyboard
import pyautogui
import pickle
import os

### record function ### 

print("Enter 'r' to begin recording")
keyboard.wait('r')	## wait for 'r' to begin recording
print(mouse.get_position())
print("Beginning recording...")
print("Enter 's' to stop recording")
actions = []
mouse.hook(actions.append)
keyboard.wait('s')
mouse.unhook(actions.append)

## create templates directory if it doesn't exist'
try:
	os.mkdir("Templates/")
except FileExistsError:
	pass

fileName = input("Please enter a name for this template.\n")
fileName = "Templates/" + fileName + ".dat"

## save template file
with open(fileName, 'wb') as f:
	pickle.dump(actions, f)

f.close()

print("Template saved!")