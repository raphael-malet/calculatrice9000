#je suis une calculatrice 9000, et je suis prêt à tout calculer pour toi !!!!

#importe interface graphique
from tkinter import *

#set-up de l'expression de debut
expression = ""


#focntion appyer sur une touche.
def appuyer_bouton(touche):
    global expression

    if touche == 'X':
        touche = '*'

    if touche == '%':
        touche = '/100'
        expression += str(touche)
        equation.set(expression)
        calculer()
        return

    if touche == 'e':
        touche = '**'

    if touche == '²':
        touche = '**2'
        expression += str(touche)
        equation.set(expression)
        calculer()
        return

    if touche == '√':
        touche = '**0.5'
        expression += str(touche)
        equation.set(expression)
        calculer()
        return

    if touche == "=":
        calculer()
        return

    if touche == 'AC':
        effacer()
        return

    expression += str(touche)
    equation.set(expression)


#focntion calculer.
def calculer():
    global total
    try:
        global expression
        total = str(eval(expression))
        
        equation.set(total)
        stockage_historique()
        expression = total

    except:
        equation.set('erreur')
        total = 'erreur'
        stockage_historique()
        total =''
        expression = ""


#focntion effacer le contenu.
def effacer():
    global expression
    equation.set('')
    expression =""

#fonction stockage dans le fichier hsitorique.txt
def stockage_historique():
    global expression
    global total
    fichier_historique = open('historique.txt', 'a')
    fichier_historique.write(expression +'='+total+'\n')
    fichier_historique.close()

#fonction afficher l'historique
def afficher_historique():
    historique = Tk()

    # taille de la fenêtre)

    # Titre de l'application
    historique.title("Historique Calculatrice9000")
    variable_historique = open('historique.txt', 'r')
    variable_historique = variable_historique.read()

    historique_affichage = Label(historique, text=variable_historique, font=('', 20))
    historique_affichage.grid(columnspan=1)

    b = Label(historique, text='Actualiser', background="#984447", fg='#FFF', width=20, font=('', 20))
    b.bind('<Button-1>', lambda e, bouton='Actualiser': afficher_historique())
    b.grid(columnspan=1)

    b = Label(historique, text='Effacer historique', background="#984447", fg='#FFF', width=20, font=('', 20))
    b.bind('<Button-1>', lambda e, bouton='Effacer historique': effacer_historique())
    b.grid(columnspan=1)

    b = Label(historique, text='QUITTER', background="#984447", fg='#FFF', width=20, font=('', 20))
    b.bind('<Button-1>', lambda e, bouton='QUITTER': historique.destroy(), )
    b.grid(columnspan=1)

    historique.mainloop()

#focntion pour effacer l'historique
def effacer_historique():
    historique_effacement = open('historique.txt', 'w')
    historique_effacement.write('')
    historique_effacement.close()

#affichage fenetre
fenetre = Tk()

#couleur de fond
fenetre.configure(background='#101419')

#taille de la fenêtre
fenetre.geometry("510x650")

#Titre de l'application
fenetre.title("Calculatrice9000")

#variable pour stocker le contenu actuel
equation = StringVar()

#boite de résultat
resultat = Label(fenetre, bg='#101419', fg="#FFF", textvariable=equation, height="2", font=("", 40))
resultat.grid(columnspan=4)

#boutons
boutons = ['AC', 'e', '√', '²', 7, 8, 9, '+', 4, 5, 6, "-", 1, 2, 3, '%', 0, ".", "/", "X"]
ligne = 1
collone = 0

#affichage des touches sur l'interface graphique
for i in boutons:
    b = Label(fenetre, text=str(i), bg="#498467", fg='#FFF', height=4, width=12, font=('',16))

    #rende les boutons cliquable
    b.bind("<Button-1>", lambda e, bouton = i: appuyer_bouton(bouton))

    #reour a la ligne lorsqu'une ligne dépasse 4
    b.grid(row=ligne, column=collone)
    collone += 1
    if collone == 4:
        collone = 0
        ligne += 1

#bouton resultat le contenu
b = Label(fenetre, text='=', bg="#984447", fg='#FFF', height=2, width=30, font=('',27))
b.bind("<Button-1>", lambda e, bouton = '=': appuyer_bouton(bouton))
b.grid(columnspan=4)

historique = Label(fenetre, text='historique', bg="#984447", fg='#FFF', height=2, width=30, font=('',27))
historique.bind("<Button-1>", lambda e, bouton = 'historique': afficher_historique())
historique.grid(columnspan=4)



#afficher la fenetre
fenetre.mainloop()


    
