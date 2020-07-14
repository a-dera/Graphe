##################################################
#      Importation des Bibliotheques et fonctions:
from tkinter import *
from random import choice
#from PIL import ImageGrab
from tkinter import PhotoImage
from Euler import *
from Hamilton import *
from maxflow import *
from GrapheOrienter import *
from GrapheNonOrienter import *

# -              Programme Principale           - #
# /////////////////////////////////////////////// #
# Description: Fenetre Principale du Programme    #
# /////////////////////////////////////////////// #

if __name__ == '__main__':
	#initialisation du canvas
	fen =Tk()
	width=fen.winfo_screenwidth()
	height=fen.winfo_screenheight()
	largeure=1200
	hauteure=600
	x=(width/2)-(largeure/2)
	y=(height/2)-(hauteure/2)
	graphe =Canvas(fen, width =largeure, height =hauteure, bg ="white")
	fen.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))
	fen.wm_title("Programme de tracer et de traitement de graphe")
	graphe.pack(side =TOP, padx =5, pady =5)
	fen.resizable(True,True)
	icon=PhotoImage(file='img/img.png')
	fen.tk.call('wm','iconphoto',fen._w,icon)
	photo = PhotoImage(file="img/img.png")
	#graphe.create_image(10, 10, anchor=NW, image=photo)
	
	

	def menu():
		#photo = PhotoImage(file="img/img.png")
		#canvas = Canvas(fen,width=photo.width(), height=photo.height())
		#canvas.create_image(0, 0, anchor=NW, image=photo)
		#canvas.pack()
		#menubar = Menu(fen)
		
		#filemenu.add_command(label="Graphe Oriente", command = graphe_oriente)
		#filemenu.add_command(label="Graphe Non Oriente", command = graphe_non_oriente)
		titre = Label(graphe, text="Theories des graphes")
		titre.config(font =("Courier", 14))
		titre.place(x=490, y=50)

		go = Button(graphe, text="Graphe Orienté", command=graphe_oriente)
		go.place(x=100,y=500)
		gno = Button(graphe, text="Graphe non Orienté", command=graphe_non_oriente)
		gno.place(x=1000,y=500)

		#fen.config(menu = menubar)
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



	menu()
	fen.mainloop()
#prece sep    succ trait