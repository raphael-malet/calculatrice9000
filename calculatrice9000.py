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

def lecture_historique():
    variable_historique = open('historique.txt', 'r')
    variable_historique = variable_historique.read()
    return variable_historique

#fonction afficher l'historique
def afficher_historique():
    historique = Tk()
    historique.title("Historique Calculatrice9000")

    variable_historique = lecture_historique()


    historique_affichage = Label(historique, text=variable_historique, font=('', 20))
    historique_affichage.grid(columnspan=1)

    actualiser = Label(historique, text='Actualiser', background="#FF8809", fg='#FFF', width=20, font=('', 20))
    actualiser.bind('<Button-1>', lambda e, bouton='Actualiser': afficher_historique())
    actualiser.grid(columnspan=1)

    effacer = Label(historique, text='Effacer historique', background="#868686", fg='#FFF', width=20, font=('', 20))
    effacer.bind('<Button-1>', lambda e, bouton='Effacer historique': effacer_historique())
    effacer.grid(columnspan=1)

    quitter = Label(historique, text='QUITTER', background="#DD0000", fg='#FFF', width=20, font=('', 20))
    quitter.bind('<Button-1>', lambda e, bouton='QUITTER': historique.destroy(), )
    quitter.grid(columnspan=1)

    historique.mainloop()

#focntion pour effacer l'historique
def effacer_historique():
    historique_effacement = open('historique.txt', 'w')
    historique_effacement.write('')
    historique_effacement.close()



if __name__ == '__main__':
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
        b = Label(fenetre, text=str(i), bg="#C8C8C8", fg='#000000', height=4, width=12, font=('',16))
        #rende les boutons cliquable
        b.bind("<Button-1>", lambda e, bouton = i: appuyer_bouton(bouton))

        #reour a la ligne lorsqu'une ligne dépasse 4
        b.grid(row=ligne, column=collone)
        collone += 1
        if collone == 4:
            collone = 0
            ligne += 1

    #bouton resultat le contenu
    b = Label(fenetre, text='=', bg="#FF8809", fg='#FFF', height=2, width=30, font=('',27))
    b.bind("<Button-1>", lambda e, bouton = '=': appuyer_bouton(bouton))
    b.grid(columnspan=4)

    historique = Label(fenetre, text='historique', bg="#868686", fg='#FFF', height=2, width=30, font=('',27))
    historique.bind("<Button-1>", lambda e, bouton = 'historique': afficher_historique())
    historique.grid(columnspan=4)


    #afficher la fenetre
    fenetre.mainloop()


    
