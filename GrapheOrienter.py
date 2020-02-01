##################################################
#      Importation des Bibliotheques et fonctions:

from tkinter import *
from PIL import ImageGrab
from tkinter import PhotoImage
from Euler import *
from Hamilton import *
from maxflow import *
import tkinter as tk
from tkinter import ttk
from main import *

# -            Fenetre Graphe Orienter          - #
# /////////////////////////////////////////////// #
# Description: Programme traitant sur les graphes #
#              Orienter                           #
# /////////////////////////////////////////////// #
class GrapheOriente(Tk):

  def __init__(self):

    Tk.__init__(self)        # constructeur de la classe parente

    #recupere la taille de l'ecrant de l'ordinateur

    width=self.winfo_screenwidth()
    height=self.winfo_screenheight()
    self.largeure=900
    self.hauteure=500
    self.x=(width/2)-(self.largeure/2)
    self.y=(height/2)-(self.hauteure/2)

    #initialisation du canvas
    self.graphe =Canvas(self, width =self.largeure, height =self.hauteure, bg ="light yellow")
    self.geometry('{}x{}+{}+{}'.format(self.largeure,self.hauteure,int(self.x),int(self.y)))
    self.resizable(False,False)
    self.wm_title('Graphe Oriente')
    self.graphe.pack(side =TOP, padx =5, pady =5)
    
    #evenement declancher par les clic de la sourie
    self.bind("<Double-Button-1>", self.sommet)
    self.bind("<Button-3>", self.arc)

    #menu de la fenetre
    menubar = Menu(self)
    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_separator()
    filemenu.add_command(label = "Quitter ?", command = self.destroy)
    filemenu.add_command(label = "Sauvegarder", command = self.save)
    menubar.add_cascade(label = "Fichier", menu = filemenu)
    
    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_separator()
    filemenu.add_command(label = "Ordre du graphe", command=self.ordre_graphe)
    filemenu.add_command(label = "Degre du sommet", command=self.degres_sommet)
    filemenu.add_command(label = "Matrice d'adjacence", command=self.matriceAdj)
    filemenu.add_command(label = "Successeur du sommet", command=self.successeur)
    filemenu.add_command(label = "Predecesseur du sommet", command=self.predeccesseur)
    filemenu.add_command(label = "Demi degre supperieur du sommet", command=self.demi_deg_sup)
    filemenu.add_command(label = "Demi degre inferieur du sommet", command=self.demi_deg_inf)
    filemenu.add_command(label = "Graphe Hamiltonien ?", command=self.hamilton)
    filemenu.add_command(label = "Graphe Eulerien ?", command=self.euler)
    filemenu.add_command(label = "Flow maximal", command=self.maxflow)
    menubar.add_cascade(label = "Outils", menu = filemenu)

    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_separator()
    filemenu.add_command(label = "Tout effacer ?", command =self.delete)
    menubar.add_cascade(label = "Effacer", menu = filemenu)
    filemenu = Menu(menubar, tearoff = 0)

    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Aide", command =self.aide)
    menubar.add_cascade(label = "Aide", menu = filemenu)
    filemenu = Menu(menubar, tearoff = 0)
    
    self.config(menu = menubar)

    #variable globale
    self.i=int(0)
    self.compt=int()
    self.temp=list()
    self.connect=list()
    self.point=list()
    self.sommets=list()
    self.couple=list()
    self.matrice=list()
    self.var=StringVar()
    self.entier=int()


  def delete(self):
    for element in self.graphe.find_all():
      self.graphe.delete(element)
    self.i=int(0)
    self.compt=int()
    self.temp=list()
    self.connect=list()
    self.point=list()
    self.sommets=list()
    self.couple=list()
    self.matrice=list()
    self.var=StringVar()
    self.entier=int()
    pass
  # fonction permettant de fermer la fenetre fille
  def Close_Toplevel (self):
    self.compt=int()
    self.temp=list()
    self.wm_attributes("-disable",False)
    self.toplevel_dialog.destroy()
    self.deiconify()
  
  #fenetre permettant de fermet la fenetre fille de sauvegarde  
  def Close_Save (self,event=None):
  	
  	if len(self.var.get())>0:
  		x=self.graphe.winfo_rootx()
	  	y=self.graphe.winfo_rooty()
	  	w=self.graphe.winfo_width()
	  	h=self.graphe.winfo_height()
	  	image=ImageGrab.grab((x+2,y+2,x+w-2,y+h-2))
  		image.save("save/{}.png".format(self.var.get()))
  	else:
  		x=self.graphe.winfo_rootx()
	  	y=self.graphe.winfo_rooty()
	  	w=self.graphe.winfo_width()
	  	h=self.graphe.winfo_height()
	  	image=ImageGrab.grab((x+2,y+2,x+w-2,y+h-2))
  		image.save("save/Graphe.png")
  	self.wm_attributes("-disable",False)
  	self.toplevel_dialog.destroy()
  	self.deiconify()

  def aide(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(600,150)
    self.toplevel_dialog.wm_title("Aide")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=600
    hauteure=150
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.bind("<Return>", self.Close_Toplevel)
    self.toplevel_dialog.focus()
    aide="""
Tracer un sommet: Double clic
Tracer un arc: clic gauche sur chaque sommet
"""
    self.label=tk.Label(self.toplevel_dialog, text=aide,justify='left',font='Century 13 bold')
    self.label.pack(side='top')

    
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.pack(side='right',fill='x',expand=True)
  #fonction de sauvegarde du graphe dessiner	
  def save(self):
  	self.wm_attributes("-disable",True)
  	self.toplevel_dialog=tk.Toplevel(self)
  	self.toplevel_dialog.minsize(300,100)
  	self.toplevel_dialog.wm_title("Sauvegarder")
  	width=self.toplevel_dialog.winfo_screenwidth()
  	height=self.toplevel_dialog.winfo_screenheight()

  	self.toplevel_dialog.transient(self)
  	self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
  	self.toplevel_dialog.bind("<Return>", self.Close_Save)
  	self.toplevel_dialog.focus()

  	self.label=tk.Label(self.toplevel_dialog, text='Entrer le nom de limage: ')
  	self.label.pack(side='left')
  	self.var=tk.Entry(self.toplevel_dialog)
  	self.var.pack(side='left')
  	self.var.bind("<Return>", self.Close_Save)
  	self.var.bind("<Escape>", self.Close_Toplevel)
  	self.var.focus_set()
  	
  	self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
  	self.yes_button.pack(side='right',fill='x',expand=True)
  	self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_Save)
  	self.yes_button.pack(side='right',fill='x',expand=True)
  	

  # fonction permettant de detecter si le graphe est eulerien
  def euler(self):
  	self.wm_attributes("-disable",True)
  	self.toplevel_dialog=tk.Toplevel(self)
  	self.toplevel_dialog.minsize(600,100)
  	self.toplevel_dialog.wm_title("Graphe eulerien")
  	width=self.toplevel_dialog.winfo_screenwidth()
  	height=self.toplevel_dialog.winfo_screenheight()
  	largeure=600
  	hauteure=100
  	x=(width/2)-(largeure/2)
  	y=(height/2)-(hauteure/2)
  	self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

  	self.toplevel_dialog.transient(self)
  	self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
  	self.toplevel_dialog.bind("<Return>", self.Close_Toplevel)

  	l=len(self.couple)
  	lg=len(self.sommets)
  	if lg>=2:
	  	g1 = Euler(lg)
	  	for i in range(l):
	  		g1.addEdge(self.couple[i][0],self.couple[i][1])
	  	self.var=g1.test()
	  	self.label=tk.Label(self.toplevel_dialog, text=self.var)
	  	self.label.pack(side='top')
  	else:
  		self.label=tk.Label(self.toplevel_dialog, text="Votre requette ne peut etre traiter")
  		self.label.pack(side='top')

  	self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
  	self.yes_button.pack(side='right',fill='x',expand=True)
  	
  #fonction permettant de detecter si le graphe est hamiltonien
  def hamilton(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(600,100)
    self.toplevel_dialog.wm_title("Graphe hamiltonien")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=600
    hauteure=100
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.bind("<Return>", self.Close_Toplevel)
    lg=len(self.couple)
    if lg>1:
      l=len(self.sommets)
      self.matrice=list()
      for i in range(l):
        self.matrice.append([])
        for j in range(l):
          k=int(0)
          temp=list()
          temp.append(self.sommets[i])
          temp.append(self.sommets[j])
          for element in self.couple:
            if temp[0]==element[0] and temp[1]==element[1]:
              self.matrice[i].append(1)
              k+=1
          if k==0:
            self.matrice[i].append(0)
      g1 = Hamilton(l)
      g1.graph = self.matrice
      self.var=g1.hamCycle()
      self.label=tk.Label(self.toplevel_dialog, text=self.var)
      self.label.pack(side='top')
      pass
    else:
      self.label=tk.Label(self.toplevel_dialog, text="Votre requette ne peut etre traiter")
      self.label.pack(side='top')
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.pack(side='right',fill='x',expand=True)

  #fonction permettant de connetre le flow maximal
  def maxflow(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(600,200)
    self.toplevel_dialog.wm_title("Flow maximal")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=600
    hauteure=200
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.focus()

    self.label=tk.Label(self.toplevel_dialog, text='Entrer sommet source: ')
    self.label.grid(row=1)
    self.valeur1=tk.Entry(self.toplevel_dialog)
    self.valeur1.grid(row=1,column=1)
    
    self.label=tk.Label(self.toplevel_dialog, text='Entrer sommet destination: ')
    self.label.grid(row=2)
    self.valeur2=tk.Entry(self.toplevel_dialog)
    self.valeur2.grid(row=2,column=1)

    self.label=tk.Label(self.toplevel_dialog, text='\n\n')
    self.label.grid(row=3)
    
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_maxflow)
    self.yes_button.grid(row=4,column=1)
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.grid(row=4,column=3)

    pass
  def Close_maxflow (self):
    lg=len(self.couple)

    if self.valeur1.get() in str(self.sommets) and self.valeur2.get() in str(self.sommets) and lg>0 and self.valeur1.get()!=self.valeur2.get() :
      l=len(self.sommets)
      self.matrice=list()
      for i in range(l):
        self.matrice.append([])
        for j in range(l):
          k=int(0)
          temp=list()
          temp.append(self.sommets[i])
          temp.append(self.sommets[j])
          for element in self.couple:
            if temp[0]==element[0] and temp[1]==element[1]:
              self.matrice[i].append(element[2])
              k+=1
          if k==0:
            self.matrice[i].append(0)
      g = Max_flow(self.matrice)
      src=int(self.valeur1.get())
      des=int(self.valeur2.get())
      self.label=tk.Label(self.toplevel_dialog, text="Le flow maximal est %d " % g.FordFulkerson(src, des))
      self.label.grid(row=6)
    else:
      self.label=tk.Label(self.toplevel_dialog, text="Votre requette ne peut etre traiter")
      self.label.grid(row=6)
    pass
  def matriceAdj(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(300,300)
    self.toplevel_dialog.wm_title("Matrice D'adjacence")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=300
    hauteure=300
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.bind("<Return>", self.Close_Toplevel)
    lg=len(self.couple)
    if lg>0:
      l=len(self.sommets)
      self.matrice=list()
      for i in range(l):
        resultat=""
        self.matrice.append([])
        for j in range(l):
          k=int(0)
          temp=list()
          temp.append(self.sommets[i])
          temp.append(self.sommets[j])
          for element in self.couple:
            if temp[0]==element[0] and temp[1]==element[1]:
              self.matrice[i].append(1)
              resultat+="1 "
              k+=1
          if k==0:
            self.matrice[i].append(0)
            resultat+="0 "
        self.label=tk.Label(self.toplevel_dialog, text=resultat)
        self.label.pack(side='top')
      
      pass
    else:
      self.label=tk.Label(self.toplevel_dialog, text="Votre requette ne peut etre traiter")
      self.label.pack(side='top')
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.pack(side='right',fill='x',expand=True)

  #fonction permettant de donner le successeur d'un sommet
  def successeur(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(650,100)
    self.toplevel_dialog.wm_title("Successeur d'un sommet")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=650
    hauteure=100
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.focus()
    self.toplevel_dialog.bind("<Return>", self.Close_suc)

    self.label=tk.Label(self.toplevel_dialog, text='Entrer sommet: ')
    self.label.grid(row=1)
    self.valeur=tk.Entry(self.toplevel_dialog)
    self.valeur.grid(row=1,column=1)
    self.valeur.bind("<Return>", self.Close_suc)
    self.valeur.bind("<Escape>", self.Close_Toplevel)
    self.valeur.focus_set()
    
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.grid(row=1,column=6)
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_suc)
    self.yes_button.grid(row=1,column=4)
    pass

  def Close_suc(self):
    if  self.valeur.get() in str(self.sommets):
      resultat=""
      for element in self.couple:
        if self.valeur.get() == str(element[0]):
          resultat+=str(element[1])+"  "
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Le(s) successeur du sommet {} est: {}'.format(self.valeur.get(),resultat))
      self.toplevel_dialog_label.grid(row=2)
    else:
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Valeur entrer incorrecte')
      self.toplevel_dialog_label.grid(row=2)
  
  def predeccesseur(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(650,100)
    self.toplevel_dialog.wm_title("Predecesseur d'un sommet")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=650
    hauteure=100
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.bind("<Return>", self.Close_pred)
    self.toplevel_dialog.focus()

    self.label=tk.Label(self.toplevel_dialog, text='Entrer sommet: ')
    self.label.grid(row=1)
    self.valeur=tk.Entry(self.toplevel_dialog)
    self.valeur.grid(row=1,column=1)
    self.valeur.bind("<Return>", self.Close_pred)
    self.valeur.bind("<Escape>", self.Close_Toplevel)
    self.valeur.focus_set()
    
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.grid(row=1,column=6)
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_pred)
    self.yes_button.grid(row=1,column=4)
    
  
  def Close_pred(self):
    if  self.valeur.get() in str(self.sommets):
      resultat=""
      for element in self.couple:
        if self.valeur.get() == str(element[1]):
          resultat+=str(element[0])+"  "
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Le(s) predecesseur du sommet  {} est: {}'.format(self.valeur.get(),resultat))
      self.toplevel_dialog_label.grid(row=2)
    else:
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Valeur entrer incorrecte')
      self.toplevel_dialog_label.grid(row=2)
          
  def demi_deg_sup(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(700,100)
    self.toplevel_dialog.wm_title("Demi degre supperieur d'un sommet")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=700
    hauteure=100
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.bind("<Return>", self.Close_degre_sup)
    self.toplevel_dialog.focus()

    self.label=tk.Label(self.toplevel_dialog, text='Entrer sommet: ')
    self.label.grid(row=1)
    self.valeur=tk.Entry(self.toplevel_dialog)
    self.valeur.grid(row=1,column=1)
    self.valeur.bind("<Return>", self.Close_degre_sup)
    self.valeur.bind("<Escape>", self.Close_Toplevel)
    self.valeur.focus_set()
    
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.grid(row=1,column=6)
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_degre_sup)
    self.yes_button.grid(row=1,column=4)
  
  def Close_degre_sup(self):
    if  self.valeur.get() in str(self.sommets):
      k=int(0)
      for element in self.couple:
        if self.valeur.get() == str(element[0]):
          k+=1
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Le demi degre supperieur du sommet {} est: {}'.format(self.valeur.get(),k))
      self.toplevel_dialog_label.grid(row=2)
    else:
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Valeur entrer incorrecte')
      self.toplevel_dialog_label.grid(row=2)
  
  def demi_deg_inf(self):
    self.wm_attributes("-disable",True)
    self.toplevel_dialog=tk.Toplevel(self)
    self.toplevel_dialog.minsize(700,100)
    self.toplevel_dialog.wm_title("Demi degre inferieur d'un sommet")
    width=self.toplevel_dialog.winfo_screenwidth()
    height=self.toplevel_dialog.winfo_screenheight()
    largeure=700
    hauteure=100
    x=(width/2)-(largeure/2)
    y=(height/2)-(hauteure/2)
    self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

    self.toplevel_dialog.transient(self)
    self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
    self.toplevel_dialog.bind("<Return>", self.Close_degre_inf)
    self.toplevel_dialog.focus()

    self.label=tk.Label(self.toplevel_dialog, text='Entrer sommet: ')
    self.label.grid(row=1)
    self.valeur=tk.Entry(self.toplevel_dialog)
    self.valeur.grid(row=1,column=1)
    self.valeur.bind("<Return>", self.Close_degre_inf)
    self.valeur.bind("<Escape>", self.Close_Toplevel)
    self.valeur.focus_set()
    
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
    self.yes_button.grid(row=1,column=6)
    self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_degre_inf)
    self.yes_button.grid(row=1,column=4)

  
  def Close_degre_inf(self):
    if  self.valeur.get() in str(self.sommets):
      k=int(0)
      for element in self.couple:
        if self.valeur.get() == str(element[1]):
          k+=1
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Le demi degre inferieur du sommet {} est: {}'.format(self.valeur.get(),k))
      self.toplevel_dialog_label.grid(row=2)
    else:
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Valeur entrer incorrecte')
      self.toplevel_dialog_label.grid(row=2)

  def degres_sommet(self):
  	self.wm_attributes("-disable",True)
  	self.toplevel_dialog=tk.Toplevel(self)
  	self.toplevel_dialog.minsize(600,100)
  	self.toplevel_dialog.wm_title("Degre du sommet")
  	width=self.toplevel_dialog.winfo_screenwidth()
  	height=self.toplevel_dialog.winfo_screenheight()
  	largeure=600
  	hauteure=100
  	x=(width/2)-(largeure/2)
  	y=(height/2)-(hauteure/2)
  	self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

  	self.toplevel_dialog.transient(self)
  	self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
  	self.toplevel_dialog.bind("<Return>", self.Close_degre)
  	self.toplevel_dialog.focus()

  	self.label=tk.Label(self.toplevel_dialog, text='Entrer sommet: ')
  	self.label.grid(row=1)
  	self.valeur=tk.Entry(self.toplevel_dialog)
  	self.valeur.grid(row=1,column=1)
  	self.valeur.bind("<Return>", self.Close_degre)
  	self.valeur.bind("<Escape>", self.Close_Toplevel)
  	self.valeur.focus_set()

  	self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
  	self.yes_button.grid(row=1,column=5)
  	self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_degre)
  	self.yes_button.grid(row=1,column=3)

  		
  def Close_degre(self):
    if  self.valeur.get() in str(self.sommets):
      k=int(0)
      for element in self.couple:
        if self.valeur.get() in str(element):
          k+=1
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Le degre du sommet {} est: {}'.format(self.valeur.get(),k))
      self.toplevel_dialog_label.grid(row=2)
    else:
      self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='Valeur entrer incorrecte')
      self.toplevel_dialog_label.grid(row=2)	
  
  def ordre_graphe(self):
  	self.wm_attributes("-disable",True)
  	self.toplevel_dialog=tk.Toplevel(self)
  	self.toplevel_dialog.minsize(502,50)
  	self.toplevel_dialog.wm_title("Ordre du graphe")
  	width=self.toplevel_dialog.winfo_screenwidth()
  	height=self.toplevel_dialog.winfo_screenheight()
  	largeure=502
  	hauteure=50
  	x=(width/2)-(largeure/2)
  	y=(height/2)-(hauteure/2)
  	self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

  	self.toplevel_dialog.transient(self)
  	self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
  	self.toplevel_dialog.bind("<Return>", self.Close_Toplevel)
  	n=len(self.sommets)
  	self.toplevel_dialog_label=tk.Label(self.toplevel_dialog, text='L ordre du graphe est: {}'.format(n))
  	self.toplevel_dialog_label.pack(side='top')

  	self.toplevel_dialog_yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
  	self.toplevel_dialog_yes_button.pack(side='right',fill='x',expand=True)

  	for i in range(3):
  		self.toplevel_dialog_label3=tk.Label(self.toplevel_dialog, text='\n')
  		self.toplevel_dialog_label3.pack()
  	pass

  
  def sommet(self, event):

    x,y=event.x,event.y
    if self.point==[]:
      self.sommet=self.graphe.create_oval(x-10,y-10,x+10,y+10, fill="cyan")
      self.numero=self.graphe.create_text(x,y,text="{}".format(self.i))
      self.point.append([event.x,event.y,self.sommet,self.numero,self.i])
      self.sommets.append(self.i)
      self.i+=1
    else:
      controle=0
      for element in self.point:

        if element[0]-25 < event.x < element[0]+25 and element[1]-25 < event.y < element[1]+25:
          controle=1
      if controle==0:
        self.sommet=self.graphe.create_oval(x-10,y-10,x+10,y+10, fill="cyan")
        self.numero=self.graphe.create_text(x,y,text="{}".format(self.i))
        self.point.append([event.x,event.y,self.sommet,self.numero,self.i])
        self.sommets.append(self.i)
        self.i+=1

  #procedure permettant de dessiner un arc entre deux sommets
  
  def arc(self, event):

    for element in self.point:

      if element[0]-10 < event.x < element[0]+10 and element[1]-10 < event.y < element[1]+10:
        self.temp.append(element)
        self.compt+=1
     															
    if self.compt==2:

      self.wm_attributes("-disable",True)
      self.toplevel_dialog=tk.Toplevel(self)
      self.toplevel_dialog.minsize(502,100)
      self.toplevel_dialog.wm_title("Arc")
      width=self.toplevel_dialog.winfo_screenwidth()
      height=self.toplevel_dialog.winfo_screenheight()
      largeure=502
      hauteure=100
      x=(width/2)-(largeure/2)
      y=(height/2)-(hauteure/2)
      self.toplevel_dialog.geometry('{}x{}+{}+{}'.format(largeure,hauteure,int(x),int(y)))

      self.toplevel_dialog.transient(self)
      self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
      self.toplevel_dialog.bind("<Return>", self.Close_arc)
      self.toplevel_dialog.focus()

      self.label=tk.Label(self.toplevel_dialog, text='Entrer la distance entre le sommet {} et le sommet {}: '.format(self.temp[0][4],self.temp[1][4]))
      self.label.pack(side='top')
      self.valeur=tk.Entry(self.toplevel_dialog)
      self.valeur.pack(side='top')
      self.valeur.bind("<Return>", self.Close_arc)
      self.valeur.bind("<Escape>", self.Close_Toplevel)
      self.valeur.focus_set()

      self.yes_button=ttk.Button(self.toplevel_dialog,text='Retour',width=25,command=self.Close_Toplevel)
      self.yes_button.pack(side='right',fill='x',expand=True)
      self.yes_button=ttk.Button(self.toplevel_dialog,text='Valider',width=25,command=self.Close_arc)
      self.yes_button.pack(side='right',fill='x',expand=True)

  def Close_arc (self,event=None):
    
    if self.temp[0][0] < self.temp[1][0]:

      a=[self.temp[0][0]+10,self.temp[0][1]]
      b=[self.temp[1][0]-10,self.temp[1][1]]
      self.graphe.create_line(a,b,arrow="last")
      try:
        self.entier=int(self.valeur.get())
      except ValueError:
        pass
      if self.entier>0 or self.entier<0 :
        pass 
      else:
        self.entier=int(1)
      self.couple.append([self.temp[0][4],self.temp[1][4],self.entier])
        
    elif self.temp[0][0]==self.temp[1][0]:

      self.graphe.delete(self.temp[0][2])
      self.graphe.delete(self.temp[0][3])
      self.graphe.create_oval(self.temp[0][0]-10,self.temp[0][1]-25,self.temp[0][0]+1,self.temp[0][1])
      self.graphe.create_oval(self.temp[0][0]-10,self.temp[0][1]-10,self.temp[0][0]+10,self.temp[0][1]+10,fill="cyan")
      self.graphe.create_text(self.temp[0][0],self.temp[0][1],text="{}".format(self.temp[0][4]))
      a=(self.temp[0][0],self.temp[0][1]-10.5)
      b=(self.temp[0][0],self.temp[0][1]-10)
      self.graphe.create_line(a,b,arrow="last")
      try:
        self.entier=int(self.valeur.get())
      except ValueError:
        pass
      if self.entier>0 or self.entier<0 :
        pass 
      else:
        self.entier=int(1)
      self.couple.append([self.temp[0][4],self.temp[1][4],self.entier])
        
    else:

      a=[self.temp[0][0]-10,self.temp[0][1]]
      b=[self.temp[1][0]+10,self.temp[1][1]]
      self.graphe.create_line(a,b,arrow="last")
      try:
        self.entier=int(self.valeur.get())
      except ValueError:
        pass
      if self.entier>0 or self.entier<0 :
        pass 
      else:
        self.entier=int(1)
      self.couple.append([self.temp[0][4],self.temp[1][4],self.entier])

    self.compt=int()
    self.temp=list()
      
    self.wm_attributes("-disable",False)
    self.toplevel_dialog.destroy()
    self.deiconify()




