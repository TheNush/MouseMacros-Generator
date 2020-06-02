import mouse
import pickle

actions = []

fileName = input ("Enter template name w/o extension: \n")
fileName = "Templates/" + fileName + ".dat"

with open(fileName, 'rb') as f:
	actions = (pickle.load(f))

f.close()

mouse.play(actions)
