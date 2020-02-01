##################################################
#      Importation des Bibliotheques et fonctions:
from tkinter import *
from PIL import ImageGrab
from tkinter import PhotoImage
from Euler import *
from Hamilton import *
from maxflow import *
from GrapheOrienter import *
from GrapheNonOrienter import *
import tkinter as tk
from tkinter import ttk

# -              Programme Principale           - #
# /////////////////////////////////////////////// #
# Description: Fenetre Principale du Programme    #
# /////////////////////////////////////////////// #

if __name__ == '__main__':
	#initialisation du canvas
	fen =Tk()
	width=fen.winfo_screenwidth()
	height=fen.winfo_screenheight()
	largeure=900
	hauteure=500
	x=(width/2)-(largeure/2)
	y=(height/2)-(hauteure/2)
	graphe =Canvas(fen, width =largeure, height =hauteure, bg="light yellow")
	fen.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))
	fen.wm_title("Graphe Tracer")
	graphe.pack(side =TOP, padx =5, pady =5)
	fen.resizable(False,False)
	icon=PhotoImage(file='img/img.png')
	fen.tk.call('wm','iconphoto',fen._w,icon)
	photo = PhotoImage(file="img/img.png",width=largeure,height=hauteure)
	graphe.create_image(300, 90, anchor=NW, image=photo)
	
	

	def menu():
		menubar = Menu(fen)
		filemenu = Menu(menubar, tearoff = 0)
		filemenu.add_command(label="Graphe Oriente", command = graphe_oriente)
		filemenu.add_command(label="Graphe Non Oriente", command = graphe_non_oriente)
		filemenu.add_separator()
		filemenu.add_command(label = "Quitter", command = fen.destroy)
		menubar.add_cascade(label = "Graphe", menu = filemenu)

		filemenu = Menu(menubar, tearoff = 0)
		filemenu.add_command(label = "Auteur", command = Auteur)
		filemenu.add_command(label="Description", command = Description)
		filemenu.add_command(label="Version", command = Version)
		menubar.add_cascade(label = "A Propos", menu = filemenu)
		

		fen.config(menu = menubar)
		fen.mainloop()
		pass

	def donothing():
		#filewin = Toplevel(root)
		#button = Button(filewin, text="Do nothing button")
		#button.pack()
		pass

	def graphe_oriente():
		# mise en place du canevas
		app = GrapheOriente()
		app.mainloop()
		fen.mainloop()
	
	def graphe_non_oriente():
		# mise en place du canevas
		app = Graphe_Non_Oriente()
		app.mainloop()
		fen.mainloop()

	def Auteur():
		a_propos="""
	Ce programme a été conçu par
	 Amédée DERA, développeur FullStack
		"""
		
		
		fen.wm_attributes("-disable",True)
		fen.toplevel_dialog=tk.Toplevel(fen)
		fen.toplevel_dialog.minsize(502,210)
		fen.toplevel_dialog.wm_title("Auteur")

		width=fen.toplevel_dialog.winfo_screenwidth()
		height=fen.toplevel_dialog.winfo_screenheight()
		largeure=502
		hauteure=210
		x=(width/2)-(largeure/2)
		y=(height/2)-(hauteure/2)
		fen.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))
		
		fen.toplevel_dialog.transient(fen)
		fen.toplevel_dialog.protocol("WM_DELETE_WINDOW", Close_Toplevel)
		fen.label=tk.Label(fen.toplevel_dialog, text=a_propos,justify='left',font='Century 13 bold')
		fen.label.grid(row=1,padx =5, pady =5)
		fen.yes_button=ttk.Button(fen.toplevel_dialog,text='Ok',width=82,command=Close_Toplevel)
		fen.yes_button.grid(row=2)

	def Description():
		a_propos="""
	Ce logiciel a ete creer dans le cadre
	de traitement de graphe.
		"""
		fen.wm_attributes("-disable",True)
		fen.toplevel_dialog=tk.Toplevel(fen)
		fen.toplevel_dialog.minsize(502,126)
		fen.toplevel_dialog.wm_title("Description")

		width=fen.toplevel_dialog.winfo_screenwidth()
		height=fen.toplevel_dialog.winfo_screenheight()
		largeure=502
		hauteure=126
		x=(width/2)-(largeure/2)
		y=(height/2)-(hauteure/2)
		fen.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))
		
		fen.toplevel_dialog.transient(fen)
		fen.toplevel_dialog.protocol("WM_DELETE_WINDOW", Close_Toplevel)
		fen.label=tk.Label(fen.toplevel_dialog, text=a_propos,justify='left',font='Century 13 bold')
		fen.label.grid(row=1,padx =5, pady =5)
		fen.yes_button=ttk.Button(fen.toplevel_dialog,text='Ok',width=82,command=Close_Toplevel)
		fen.yes_button.grid(row=2)

	def Version():
		a_propos="""Version 1.2.0"""
		
		
		fen.wm_attributes("-disable",True)
		fen.toplevel_dialog=tk.Toplevel(fen)
		fen.toplevel_dialog.minsize(300,64)
		fen.toplevel_dialog.wm_title("Version")

		width=fen.toplevel_dialog.winfo_screenwidth()
		height=fen.toplevel_dialog.winfo_screenheight()
		largeure=300
		hauteure=64
		x=(width/2)-(largeure/2)
		y=(height/2)-(hauteure/2)
		fen.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))
		
		fen.toplevel_dialog.transient(fen)
		fen.toplevel_dialog.protocol("WM_DELETE_WINDOW", Close_Toplevel)
		fen.label=tk.Label(fen.toplevel_dialog, text=a_propos,justify='left',font='Century 13 bold')
		fen.label.grid(row=1,padx =5, pady =5)
		fen.yes_button=ttk.Button(fen.toplevel_dialog,text='Ok',width=48,command=Close_Toplevel)
		fen.yes_button.grid(row=4)
	
	def Close_Toplevel ():
		fen.wm_attributes("-disable",False)
		fen.toplevel_dialog.destroy()
		fen.deiconify()

	menu()
	fen.mainloop()
