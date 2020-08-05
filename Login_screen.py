from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
import random
from Register import* 
from Secondwindow import *


class Login_Window():
	def __init__(self,login):
		self.login = login                              #Setting up of the program 
		self.login.title("Covid-19 Game 2020")
		self.login.geometry('400x400+300+200')
		self.login.resizable(False, False)
		self.login.iconbitmap('c:/Users/Tuffic Gilzene/OneDrive - Goddard Enterprises Ltd/Desktop/Second Project/Game test/images/logo5.ico')
		
		#List of images use for the background
		self.bg_img = ImageTk.PhotoImage(file="images/bg.jpg")
		self.pwdshow = PhotoImage(file="images/showpwd.png")
		self.hpwd = PhotoImage(file="images/hidepwd.png")

		#Images assign to label to display the background
		bgpic = Label(self.login, image=self.bg_img)
		bgpic.place(x=0, y=0, relwidth=1, relheight=1)

		#A label use to display the welcome message  
		welabel = Label(self.login, text="Welcome to Group FIVE Game", bg="#330341", fg="white", font="Times 12 bold").grid(row=0, column=0, columnspan=2, padx=100, pady=20)

		#Set text and interger variables
		self.clicked = IntVar()
		self.usrentry_n = StringVar()
		self.pwdentry_w = StringVar()
		self.usrentry = StringVar()
		self.pwdentry = StringVar()

		#Decription of login details with entry, button and labels
		faline = Frame(self.login, bg="white", width=50, height=56, pady=3)
		faline.grid(row=1,column=1, padx=6, pady=5, sticky=W)
		
		loglabel =Label(faline, text="Login Window", bg="white", fg="#e1ad01", font="Times 14 bold")
		loglabel.grid(row=1, column=1, sticky=W, padx=5, pady=20)
		
		usrlabel =Label(faline, text="User ID: ", bg="white")
		usrlabel.grid(row=2, column=0, sticky=W)
		
		self.usrentry = Entry(faline, width=30, textvariable=self.usrentry_n)
		self.usrentry.grid(row=2, column=1, sticky= W)									#Entry fields for user password input and username					
		self.usrentry.focus()

		pwdlabel = Label(faline, text="Password: ", bg="white")
		pwdlabel.grid(row=3, column=0, sticky=W)
		
		self.pwdentry = Entry(faline, show="*", width=30, textvariable=self.pwdentry_w)
		self.pwdentry.grid(row=3, column=1, sticky=W, pady=5)
		self.pwdentry.focus()
		
		#A frame is set to hold all the widgets in a container, eg. label, entry, button,etc
		faline2 = Frame(self.login, bg="purple", bd=2)
		faline2.place(x=84, y=194, width=246, height=120)
		label1 = Label(faline2, text="_", fg="yellow", bg="yellow")
		label1.place(x=15, y=50, width=100, height=2)
		olabel = Label(faline2, text="OR", fg="lightgray", bg="purple")
		olabel.place(x=110, y=40)
		label2 = Label(faline2, text="_", fg="yellow", bg="yellow")
		label2.place(x=130, y=50, width=100, height=2)

		#Button set to sign in user who register
		lgbutton = Button(self.login, text="LOGIN", bg="purple", fg="yellow", command=self.login_usr)
		lgbutton.place(x=160, y=200, width=100)

		#Button set for user to register
		signbtn = Button(self.login, text="SIGN UP!", bg="purple", fg="yellow", command=self.registry)
		signbtn.place(x=160, y=270, width=100)

		#Checkbutton set which is assign by two pictures for 1 which show the password and 2 hide the password.
		showpwd = Checkbutton(faline, image=self.hpwd, selectimage=self.pwdshow, offvalue=1, onvalue=2, variable=self.clicked, command=self.hidepwd, bg="white", indicatoron=False, bd=0)
		showpwd.place(x=220, y=95)

		#A label use for the copyright of the program
		copyright =Label(self.login, text="\u00a9 Copyright Group FIVE Covid-19 2020", fg="white", bg="#731c9e").place(x=90, y=380)

	def login_usr(self):
		trackingLogin = 1 #Use to limit the amount of time a user can login in
		dict = {}
		if trackingLogin <=3: #Function is use to determine the number of fail attempt  
			try:
				file = open("user-record.txt","r")
				for line in file:
					if ':' in line:
						key,value = line.split(':', 1) #Function that fetch the correct data to gain gameplay
						cvalue = len(value)-1
						value = value[0:cvalue]
						dict[key]=value
					else:
						pass
				usrn = dict.get('Username') #function takes a key as an argument and returns the corresponding value.
				pwdw = dict.get('Password')	#function takes a key as an argument and returns the corresponding value.
				self.register_profile()
				if(usrn == self.usrentry_n.get() and pwdw == self.pwdentry_w.get()): 
					messagebox.showinfo(title="Successful", message=f"Welcome {self.usrentry.get()}, thank you for login.")
						
					#Destroy current window
					login.destroy()

					#This function is use to open the registry window
					mainevent = Tk()
					application = Second_Window(mainevent)
					game.mainloop()
				else:
					trackingLogin += 1 #Incrementing the tracking function 
					messagebox.showwarning(title="Caution", message="Invaild password, Please try again!") #This display a caution message when user input incorrect credentials
			except ValueError:
				pass
			file.close()
		else:
			messagebox.showerror(title="Failed", message="You have exceed the maximum login, Goodbye") #After numerous failed attempt the user is disconnected
			login.destroy() #This function close the window

	#Function to show password
	def hidepwd(self):
		if self.clicked.get() == 2: # On function that show the password
			self.pwdentry.config(show='')
		elif self.clicked.get() == 1: #Off function that hide the password
			self.pwdentry.config(show="*")

	def registry(self): #Function is use to open the register window
		login.destroy()

		regroot= Tk()
		application = Registration_Window(regroot)
		regroot.mainloop()


if __name__ == '__main__': #Function is use to execute the program as the main source file

	login = Tk()		#Ending of the program
	application = Login_Window(login)
	login.mainloop()



