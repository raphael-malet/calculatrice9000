#je suis une calculatrice 9000, et je suis prêt à tout calculer pour toi !!!!

#importe interface graphique
from tkinter import *

#set-up de l'expression de debut
expression = ""
total = ""

#focntion appyer sur une touche.
def appuyer_bouton(touche):
    global expression

    #pour faire multiplication
    if touche == 'X':
        touche = '*'

    #pour faire pourcentage
    if touche == '%':
        touche = '/100'
        expression += str(touche)
        equation.set(expression)
        calculer()
        return

    #pour faire exposant
    if touche == 'e':
        touche = '**'

    #pour faire au carré
    if touche == '²':
        touche = '**2'
        expression += str(touche)
        equation.set(expression)
        calculer()
        return

    #pour faire racine carré
    if touche == '√':
        touche = '**0.5'
        expression += str(touche)
        equation.set(expression)
        calculer()
        return

    #si on veut afficher le résultat
    if touche == "=":
        calculer()
        return

    #pour effacer l'expression en cours
    if touche == 'AC':
        effacer()
        return

    #ajout input a l'expression en cours
    expression += str(touche)
    equation.set(expression)


#focntion calculer.
def calculer():
    global total

    #si le resultat est possible
    try:
        global expression
        total = str(eval(expression))
        
        equation.set(total)
        stockage_historique()
        expression = total

    #si le resultat est impossible
    except :
        equation.set('erreur')
        total = 'erreur'
        stockage_historique()
        total =''
        expression = ""


#focntion effacer le contenu.
def effacer():
    global expression
    equation.set('')
    expression = ""  #on remet l'expression a '0'


#fonction stockage dans le fichier hsitorique.txt
def stockage_historique():
    global expression
    global total
    fichier_historique = open('historique.txt', 'a')
    fichier_historique.write(expression +'='+total+'\n') #on écrit l'expression et le résultat dans le fichier .txt
    fichier_historique.close()


#fonction lecture du fichier historique.txt
def lecture_historique():
    variable_historique = open('historique.txt', 'r')
    variable_historique = variable_historique.read() #permet d'assigner la lecture de l'historique a une variable.
    return variable_historique


#fonction afficher l'historique
def afficher_historique():
    #nom de la fenêtre historique
    historique = Tk()

    #titre de la fenêtre
    historique.title("Historique Calculatrice9000")
    #fond de la fenêtre
    historique.configure(background='#000000')
    #variable fonction lecture historique
    variable_historique = lecture_historique()

    #affichage de l'historique
    historique_affichage = Label(historique, text=variable_historique,background='#000000', font=('', 20))
    historique_affichage.grid(columnspan=4)

    #bouton actualiser
    actualiser = Label(historique, text='Actualiser', background="#FF8809", fg='#FFF', height=2, font=('', 20))
    actualiser.bind('<Button-1>', lambda e, bouton='Actualiser': rafraichir_historique(historique))
    actualiser.grid(column=1, row=1)

    #bouton effacer historique
    effacer = Label(historique, text='Effacer historique', background="#868686", fg='#FFF', height=2, font=('', 20))
    effacer.bind('<Button-1>', lambda e, bouton='Effacer historique': effacer_historique())
    effacer.grid(column=2, row=1)

    #bouton fermer fenêtre hsitorique
    quitter = Label(historique, text='QUITTER', background="#DD0000", fg='#FFF', height=2, font=('', 20))
    quitter.bind('<Button-1>', lambda e, bouton='QUITTER': historique.destroy(), )
    quitter.grid(column=3, row=1)

    historique.mainloop()


#focntion pour effacer l'historique
def effacer_historique():
    historique_effacement = open('historique.txt', 'w')
    historique_effacement.write('') #permet d'effacer le contenu de l'historique
    historique_effacement.close()

#Fonction pour actualiser l'historique
def rafraichir_historique(self):
    self.destroy() #on ferme la fenêtre historique
    afficher_historique() # on oouvre la fenêtre hsitorique


if __name__ == '__main__':
    #la fenêtre prend comme nom fenetre
    fenetre = Tk()

    #couleur de fond
    fenetre.configure(background='#101419')

    #taille de la fenêtre
    fenetre.geometry("550x615")

    #Titre de l'application
    fenetre.title("Calculatrice9000")

    #variable pour stocker le contenu actuel
    equation = StringVar()

    #boite d'expression/résultat
    resultat = Label(fenetre, bg='#101419', fg="#FFF", textvariable=equation, height="2", font=("", 40))
    resultat.grid(columnspan=4)

    #liste des boutons
    boutons = ['AC', 'e', '√', '²', 7, 8, 9, '+', 4, 5, 6, "-", 1, 2, 3, '%', 0, ".", "/", "X"]
    ligne = 1
    collone = 0

    #affichage des boutons sur l'interface graphique
    for i in boutons:
        b = Label(fenetre, text=str(i), bg="#C8C8C8", fg='#000000', height=4, width=12, font=('',16, "bold"))

        #rende les boutons cliquable
        b.bind("<Button-1>", lambda e, bouton = i: appuyer_bouton(bouton))

        #retour a la ligne lorsqu'une ligne de bouton dépasse 4
        b.grid(row=ligne, column=collone)
        collone += 1
        if collone == 4:
            collone = 0
            ligne += 1

    #bouton resultat le contenu
    b = Label(fenetre, text='=', bg="#FF8809", fg='#FFF', height=3, width=16, font=('',27))
    b.bind("<Button-1>", lambda e, bouton = '=': appuyer_bouton(bouton))
    b.grid(column=0, columnspan=2, row=6)

    #bouton affichage historique
    historique = Label(fenetre, text='historique', bg="#868686", fg='#FFF', height=3, width=16, font=('',27))
    historique.bind("<Button-1>", lambda e, bouton = 'historique': afficher_historique())
    historique.grid(column=2, columnspan=2, row=6)

    #afficher la fenetre
    fenetre.mainloop()