from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk
import random 
from Register import *


class Second_Window():
	def __init__(self,game):                   
		self.game=game                                #Setting up of the program which include title, size, icon, background,etc
		self.game.title("Covid-19 Game 2020")
		self.game.geometry("500x450-300+200")
		self.game.resizable(False, False)
		self.game.iconbitmap('c:/Users/Tuffic Gilzene/OneDrive - Goddard Enterprises Ltd/Desktop/Second Project/Game test/images/logo5.ico')
		self.game['background']='purple'

		#Set text variables	
		self.fill = StringVar()
		self.fill.set(None)

		#Creating of the menu display with different commands
		menu = Menu(self.game)
		self.game.config(menu=menu)

		fil_menu = Menu(menu, tearoff=0)
		menu.add_cascade(label="File", menu=fil_menu)
		fil_menu.add_command(label="Quit", command=self.game.quit)
		fil_menu.add_command(label="Register", command=self.reg_win)

		rul_menu = Menu(menu, tearoff=0)
		menu.add_cascade(label="Rules", menu=rul_menu)
		rul_menu.add_command(label="Information", command=self.rules_in)

		restart_menu = Menu(menu, tearoff=0)
		menu.add_cascade(label="Restart", menu=restart_menu)
		restart_menu.add_command(label="Let's Play again", command=self.resetGame)
		
		#A label use for the welcome message of the game
		Label(self.game, text="Let The Game begins", fg="yellow", bg="purple", 
			font="Times 18 italic", justify=CENTER).grid(row=2, column=0, padx=125, pady=5, sticky=NE)
		
		#A label frame is set to hold each characters of the game
		optionframe= LabelFrame(self.game, text="Pick your Covid character", bg="purple", fg="yellow", font="Arial 10 italic", highlightcolor="black")
		optionframe.grid(row=2, column=0, padx=30, pady=50, sticky=NW)
		
		#A list set to store each character images in one variable 
		self.character = {'Jamaica':PhotoImage(file="images/Jamaica.png"),'US':PhotoImage(file="images/US.png"),'China':PhotoImage(file="images/China.png")}
		self.a_character=Radiobutton(optionframe, text="Andrew Holness", variable=self.fill, value='Jamaica', command=self.char_choices, bg="purple", font="Arial 11 bold")
		self.a_character.grid(row=2, column=0, padx=1, pady=2, sticky=NW)
		self.d_character=Radiobutton(optionframe, text="Donald Trump", variable=self.fill, value='US', command=self.char_choices, bg="purple", font="Arial 11 bold")
		self.d_character.grid(row=3, column=0, padx=1, pady=2, sticky=NW)
		self.x_character=Radiobutton(optionframe, text="Xi Jinping", variable=self.fill, value='China', command=self.char_choices, bg="purple", font="Arial 11 bold")
		self.x_character.grid(row=4, column=0, padx=1, pady=2, sticky=NW) #A radiobutton is use to assign each character when selected by users			
		self.icon=Label(self.game, image="", bg="purple")              
		self.icon.grid(row=2, column=0, padx=50, pady=55, sticky=NE)

		#Images store in a label to display whether win or loose 
		self.picgif = PhotoImage(file="images/win.gif", format='gif -index 2')
		self.picgif1= PhotoImage(file="images/lost.gif", format='gif -index 2')
		self.imgdisp = Label(self.game, image="", bg="purple", width=70, height=70)
		self.imgdisp.place(x=90, y=200, width=70, height=70)



		#A button use to action the game		
		btn=Button(self.game, text="FIGHT!!", justify=CENTER, bg="purple", fg="yellow", command=self.action)				
		btn.grid(row=3, column=0, padx=40, pady=2, sticky=NE)
		
		#Label set as a spacer
		design = Label(self.game, text="-------------------------------------------------------", justify=CENTER, bg="purple", fg="yellow")
		design.grid(row=3, column=0, padx=20, pady=10, sticky=NW)
		self.result = Label(self.game, text="", bg="purple", fg="white", font="Arial 11 italic")      #A labels set to display the results of the game
		self.result.grid(row=3, column= 0, padx=55, pady=25, sticky=NW)
		self.lb_choices=Label(self.game, text="", bg="purple", fg="yellow", font="Times 12 bold")
		self.lb_choices.grid(row=3, column=0, pady=55, padx=55, columnspan=2, sticky=NW)
		self.score = Label(self.game, text='Display of Total:\nWins: 0\nLosses: 0\nTies: 0', borderwidth=2, width=30, relief=SOLID, bg="white")
		self.score.grid(row=3, column=0, padx=70, pady=90, sticky=NW)	


	def resetGame(self): #This function is use to reset the game completely 
		win = 0
		lose = 0
		tie = 0
		
		self.imgdisp ["image"] = ""                                    
		self.result['text'] = 'You %s'%("") #All these label are reset to none(zero)
		self.lb_choices['text'] = 'You play: %s | Computer play: %s'%("", "")
		self.score['text'] = 'Display of Total:\nWins: %s\nLosses: %s\nTies: %s' %(0, 0, 0)
		self.icon["image"] = ""
		self.fill.set(None)
		self.a_character.deselect() #Function that deselect each character
		self.d_character.deselect()
		self.x_character.deselect()	
		

	def char_choices(self):   #A function when select the radibutton it display the character of user choice
		if self.fill.get() == 'Jamaica':
			self.icon["image"] = self.character['Jamaica']
		elif self.fill.get() == 'US':
			self.icon["image"] = self.character['US']
		elif self.fill.get() == 'China':
			self.icon["image"] = self.character['China']
		else:
			self.icon["image"] = ""

	 	
	def action(self): #Main function for the game play 
		win = 0
		lose = 0
		tie = 0

		global display

		computerPlayer = ['Jamaica','US','China'] #List of characters assign to a label
		computerPlayer = random.choice(computerPlayer) #Function which randomly select a characters for the computer player
		player = self.fill.get() #User function 
			

		if (win <= 10 or lose <= 10): #A function which determine whether win or lose over 10 times the game end.
			if (player == computerPlayer): #Function tells user and computer they are draw
				display = 'Tied!'
			elif (computerPlayer == 'US' and player == 'China') or (computerPlayer == 'China' and player == 'Jamaica') or (computerPlayer == 'US' and player == 'Jamaica'):
				display = 'Won!' #Function that display the winner
				self.imgdisp ["image"] = self.picgif
				messagebox.showinfo(title="Celebration!!", message=f"You {display}, thanks for controlling the spread of Covid-19.")			
			else:
				display = 'Lost!' #function that display user lost
				self.imgdisp ["image"] = self.picgif1
				messagebox.showinfo(title="Disappointed!!", message=f"You {display}, sorry continue the game to control the spread of Covid-19.")
			if (display == 'Tied!'):
				tie += 1
			elif (display == 'Won!'):
				win += 1
			else: 
				lose += 1
		else:
			messagebox.showerror(title="Exceed", message="You have exceed maximum game play, Thanks for playing!")
			self.game.destroy() #Function that close the window after 10 win or lose

		#Label set to display the results of the game	
		self.result['text'] = 'You %s'%(display) 
		self.lb_choices['text'] = 'You play: %s | Computer play: %s'%(player, computerPlayer)
		self.score['text'] = 'Display of Total:\nWins: %s\nLosses: %s\nTies: %s' %(win, lose, tie)
		
	
		
	def rules_in(self): # Function use to display the rules of the game
		messagebox.showinfo(title="Rules for the game", message="-You must register and create a login to play.\n-You are allowed to select only one character for each face off.\n-Your opponent will be randomly selected.\n-Preset conditions will determine the winner.\n-A scoreboard is used to track wins and losses.\n-A gameplay session ends after 10 wins or losses.")

	def reg_win(self): #Function that bring you to the register window 
		winroot = Tk()
		application = Registration_Window(winroot)
		winroot.mainloop()

if __name__ == '__main__': #Function is use to execute the program as the main source file 

	game = Tk()          #Closing of the program
	application = Second_Window(game)
	game.mainloop()



