from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
import random 
from Login_screen import *


class Registration_Window:
	def __init__(self,register):
		#Description of the window setup
		self.register = register
		self.register.title("Registration 2020")
		self.register.geometry('400x400+100+250')
		self.register.iconbitmap('c:/Users/Tuffic Gilzene/OneDrive - Goddard Enterprises Ltd/Desktop/Second Project/Game test/images/logo5.ico')
		self.register.resizable(False, False)
		
		#A label set for the background of the program 
		self.imgbg = ImageTk.PhotoImage(file="images/bgg.jpg")
		self.imgback = Label(self.register, image=self.imgbg)
		self.imgback.place(x=0, y=0, relwidth=1, relheight=1)
		
		#self.register['background']='purple'


		#These are set text variables
		self.Username = StringVar()
		self.Password = StringVar()
		self.Age = StringVar()
		self.Email = StringVar()


		#Set frame use to hold the variables like label, button, entry,etc
		faline3 = Frame(self.register, bg="white")
		faline3.place(x=50, y=60, width=300, height=300)
		reglabel = Label(faline3, text="Registration", font="Times 14 bold", bg="white", fg="#e1ad01")
		reglabel.place(x=95, y=5)
		linereg = Label(faline3, text="___________", bg="black")
		linereg.place(x=40, y=35, width=220, height=2)

		usrName = Label(faline3, text="Username:", bg="white", fg="black").place(x=20, y=60)
		self.usr_entry = Entry(faline3, width=25, textvariable=self.Username)
		self.usr_entry.place(x=100, y=65)                                                              #Set entry feilds for user to sign up for the game
		self.usr_entry.focus()

		usrpass = Label(faline3, text="Password:", bg="white", fg="black").place(x=20, y=89)
		self.pwd_entry = Entry(faline3, width=25, show="*", textvariable=self.Password)
		self.pwd_entry.place(x=100, y=90)
		self.pwd_entry.focus()

		age_lbc = Label(faline3, text="Age:", bg="white", fg="black").place(x=20, y=115)
		self.age_entry = Entry(faline3, width=25, textvariable=self.Age)
		self.age_entry.place(x=100, y=115)
		self.age_entry.focus()

		mail = Label(faline3, text="Email:", bg="white", fg="black").place(x=20, y=140)
		self.email_entry = Entry(faline3, width=25, textvariable=self.Email)
		self.email_entry.place(x=100, y=140)
		self.email_entry.focus()
		
		#Button set to called the registration function and store the information
		reg = Button(faline3, text="Register Now", command=self.register_profile, bg="purple", fg="yellow").place(x=100, y=190, width=100)
		
		#Button use to close registration window after completed registration
		home = Button(faline3, text="Back to Login", command=self.homebtn, bg="purple", fg="yellow", bd=0).place(x=100, y=225, width=100)

		
	def register_profile(self):
		#Descriptive of the register profile 
		dict = { }
		try:
			usr_value = self.Username.get() #A dict use to store each record like username, password, age, email
			pwd_value = self.Password.get()
			age_value = int(self.Age.get())
			email_value = str(self.Email.get())
			dict['Username'] = usr_value
			dict['Password'] = pwd_value
			dict['Email'] = email_value
			dict['Age'] = age_value
			f = open("user-record.txt","a") #Function use to store user record in a text file and it can hold as many. 
			for key, value in dict.items():
				f.write('%s:%s\n' % (key, value))
			f.close()
			messagebox.showinfo(title="Completed", message="Registration completed, sign in to continue.") #Message display when complete the registration
		except ValueError:
			pass

	def homebtn(self): #Function that bring you back to login screen
		register.destroy()

		home = Tk()
		application = Login_Window(home)
		home.mainloop()

if __name__ == '__main__': #Function is use to execute the program as the main source file
    register = Tk()			#Ending of the program
    application = Registration_Window(register)
    register.mainloop()