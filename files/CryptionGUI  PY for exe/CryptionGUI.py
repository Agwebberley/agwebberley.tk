from tkinter import *
from tkinter.ttk import *
import random
import pyperclip
import json
import wget
import os
root = Tk()




def Encryption(operation, text, operationL, operationbe, eordb, e):
	operationbe.forget()
	operationL.forget()
	string = text.get()
	operation1 = operation.get()
	operation1 = int(operation1)
	operation.forget()
	new_string = ""
	for i in range(len(string)):
		new_string += chr(int(ord(string[i]) + operation1))
	new_stringL = Label(root, text=new_string).pack()
	clipL = Label(root, text="The encrypted messsage has been copied to your clipboard")
	clipL.pack()
	pyperclip.copy(new_string)
	copy = pyperclip.paste()
	restartb = Button(root, text="Restart", command=lambda: restart(eordb, e, restartb, exitb, clipL))
	restartb.pack()
	exitb = Button(root, text="Quit", command=root.quit)
	exitb.pack()

def Decryption(operation, text, operationL, operationbd, eordb, e):
	operationbd.forget()
	operationL.forget()
	string = text.get()
	operation1 = operation.get()
	operation1 = int(operation1)
	operation.forget()
	new_string = ''
	for i in range(len(string)):
		new_string += chr(int(ord(string[i]) - operation1))
	new_stringL = Label(root, text=new_string).pack()
	clipL = Label(root, text="Decrypted messsage has been copied to your clipboard")
	pyperclip.copy(new_string)
	copy = pyperclip.paste()
	restartb = Button(root, text="Restart", command=lambda: restart(eordb, e, restartb, exitb, clipL))
	restartb.pack()
	exitb = Button(root, text="Quit", command=root.quit)
	exitb.pack()


def eord(eordb, e, eordL2):
	eordL = Label(root, text="placement")
	eord = e.get()
	eord = eord.lower()
	if eord == "e" or eord == "encryption" or eord == "d" or eord == "decryption":
		eordb.pack_forget()
		eordL2.forget()
		e.forget()

		text(eord, eordL, eordb, e)

	else:
		exitb = Label(root, text="placement")
		restartb = Label(root, text="placement")
		clipL = Label(root, text="placement")
		eordL = Label(root, text="Please enter e or encryption or d or decryption").pack()
		restart(eordb, e, restartb, exitb, clipL)


def text(eord, eordL, eordb, e):
	eordL.forget()
	textL = Label(root, text="Enter Text")
	textL.pack()
	text = Entry(root)
	text.pack()
	textb = Button(root, text="Next Step", command=lambda: operation(eord, eordb, textL, e, text, textb))
	textb.pack()


def operation(eord, eordb, textL, e, text, textb):
	textL.forget()
	textb.forget()
	text.forget()
	operationL = Label(root, text="Enter Seed (Must be Int)")
	operationL.pack()
	operation = Entry(root)
	operation.pack()
	
	if eord == "e" or eord == "encryption":
		operationbe = Button(root, text="Encrypt", command=lambda: Encryption(operation, text, operationL, operationbe, eordb, e))
		operationbe.pack()
	else:
		operationbd = Button(root, text="Decrypt", command=lambda: Decryption(operation, text, operationL, operationbd, eordb, e))
		operationbd.pack()


def restart(eordb, e, restartb, exitb, clipL):
	restartb.forget()
	exitb.forget()
	clipL.forget()

	e.pack()
	eordb.pack()


def version_check():
	url = "https://raw.githubusercontent.com/Agwebberley/agwebberley.tk/master/files/newestversion.json"
	url2 = "https://raw.githubusercontent.com/Agwebberley/agwebberley.tk/master/files/newestversionexe.json"
	where = os.getcwd()
	where = str(where)
	wget.download(url, where)
	wget.download(url2, where)

	with open('newestversion.json') as json_file:
		newestversion = json.load(json_file)
	with open('newestversionexe.json') as json_file:
		newestversionexe = json.load(json_file)

	versionexe = 1.1
	version = 1.1

	if versionexe < newestversionexe:
		neednewexeL = Label(root, text="New version availible for exe")
		neednewexeL.pack()
		clipL = Label(root, text="placement")
		restartb = Button(root, text="Continue Anyway", command=lambda: restart(eordb, e, restartb, exitb, clipL))
		restartb.pack()
		exitb = Button(root, text="Quit", command=root.quit)
		exitb.pack()
		if os.path.exists("newestversion.json"):
			os.remove("newestversion.json")
		if os.path.exists("newestversionexe.json"):
			os.remove("newestversionexe.json")
	else:

		if version < newestversion:
			neednewL = Label(root, text="A new version is availible for py")
			neednewL.pack()
			clipL = Label(root, text="placement")
			restartb = Button(root, text="Continue Anyway", command=lambda: restart(eordb, e, restartb, exitb, clipL))
			restartb.pack()
			exitb = Button(root, text="Quit", command=root.quit)
			exitb.pack()
			if os.path.exists("newestversion.json"):
				os.remove("newestversion.json")
			if os.path.exists("newestversionexe.json"):
				os.remove("newestversionexe.json")

		if os.path.exists("newestversion.json"):
			os.remove("newestversion.json")
		if os.path.exists("newestversionexe.json"):
			os.remove("newestversionexe.json")



version_check()


eordL2 = Label(root, text="Encryption or Decryption")
eordL2.pack()

e = Entry(root)
e.pack()

eordb = Button(root, text="Next Step", command=lambda: eord(eordb, e, eordL2))
eordb.pack()




root.mainloop()