# je suis une calculatrice 9000, et je suis prêt à tout calculer pour toi !!!!

# importe interface graphique
import tkinter as tk
from tkinter import *

# set-up de l'expression de debut
expression = ""
total = ""


# HISTORIQUE
# fonction stockage dans le fichier hsitorique.txt
def stockage_historique():
    global expression
    global total
    fichier_historique = open('historique.txt', 'a')
    fichier_historique.write(
        expression + '=' + total + '\n')  # on écrit l'expression et le résultat dans le fichier .txt
    fichier_historique.close()


# fonction lecture du fichier historique.txt
def lecture_historique():
    donnee_historique = open('historique.txt', 'r')
    # permet d'assigner la lecture de l'historique a une variable.
    donnee_historique = donnee_historique.readlines()[-25:]
    donnee_historique = "".join(donnee_historique)
    return donnee_historique


# focntion pour effacer l'historique
def effacer_historique():
    global historique

    historique_effacement = open('historique.txt', 'w')
    historique_effacement.write('')  # permet d'effacer le contenu de l'historique
    historique_effacement.close()


# Fonction pour actualiser l'historique
def actualiser_historique(fenetre):
    fenetre.destroy()  # on ferme la fenêtre historique
    afficher_historique()  # on oouvre la fenêtre hsitorique


# fonction afficher l'historique
def afficher_historique():
    # nom de la fenêtre historique
    historique = Tk()

    # titre de la fenêtre
    historique.title("Historique Calculatrice9000")
    # fond de la fenêtre
    historique.configure(background='#000000')
    # variable fonction lecture historique
    variable_historique = lecture_historique()

    # affichage de l'historique
    historique_affichage = Label(historique, text=variable_historique, background='#000000', font=('', 20))
    historique_affichage.grid(columnspan=4, row=10)

    # bouton actualiser
    actualiser = Label(historique, text='Actualiser', background="#FF8809", fg='#FFF', height=2, font=('', 20))
    actualiser.bind('<Button-1>', lambda e, bouton='Actualiser': actualiser_historique(historique))
    actualiser.grid(column=1, row=11)

    # bouton effacer historique
    effacer = Label(historique, text='Effacer historique', background="#868686", fg='#FFF', height=2, font=('', 20))
    effacer.bind('<Button-1>',
                 lambda e, bouton='Effacer historique': [effacer_historique(), actualiser_historique(historique)])
    effacer.grid(column=2, row=11)

    # bouton fermer fenêtre hsitorique
    quitter = Label(historique, text='QUITTER', background="#DD0000", fg='#FFF', height=2, font=('', 20))
    quitter.bind('<Button-1>', lambda e, bouton='QUITTER': historique.destroy(), )
    quitter.grid(column=3, row=11)

    historique.mainloop()


# CALCULATRICE9000
# focntion appuyer sur une touche.
def appuyer_bouton(touche):
    global total
    global expression

    # pour faire multiplication
    if touche == 'X':
        touche = '*'

    # pour faire pourcentage
    if touche == '%':
        touche = '/100'
        expression += str(touche)
        equation.set(expression)
        calculer()
        return

    # pour faire exposant
    if touche == 'exp':
        touche = '**'

    # pour faire au carré
    if touche == '²':
        touche = '**2'
        expression += str(touche)
        if len(expression) >= 5:
            expression = list(expression)
            if expression[-5] == '-':
                expression[-5] = '+'
                expression = "".join(expression)
            else:
                expression = "".join(expression)
        equation.set(expression)
        calculer()
        return

    # pour faire racine carré
    if touche == '√':
        touche = '**0.5'
        expression += touche
        equation.set(expression)
        calculer()
        return

    if touche == 'π':
        touche = '3.14159265359'
    # si on veut afficher le résultat
    if touche == "=":
        calculer()
        return

    # pour effacer l'expression en cours
    if touche == 'AC':
        effacer()
        return

    # pour reprendre ou non le calcul en cours
    if expression == total:
        if touche in range(0, 9) or touche == '(' or touche == ')':
            expression = ""

    # si le premier chiffre entrée = 0 l'expression repprend depuis le debut
    if expression == '0':
        if touche in range(0, 9):
            expression = ""

    # ajout input a l'expression en cours
    expression += str(touche)
    equation.set(expression)


# fonction calculer.
def calculer():
    global total
    global total_affichage

    # si le resultat est possible
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        stockage_historique()
        expression = total

    # si le resultat est impossible
    except:
        equation.set('erreur')
        total = 'erreur'
        stockage_historique()
        total = ''
        expression = ""


# focntion effacer le contenu.
def effacer():
    global expression
    equation.set('')
    expression = ""  # on remet l'expression a '0'


# affiche calculatrice9000
if __name__ == '__main__':
    # la fenêtre prend comme nom fenetre
    fenetre = tk.Tk()

    # couleur de fond
    fenetre.configure(background='#101419')

    # taille de la fenêtre
    fenetre.geometry("415x523")

    # Titre de l'application
    fenetre.title("Calculatrice9000")

    # variable pour stocker le contenu actuel
    equation = StringVar()

    # liste des boutons
    boutons = ['AC', '(', ')', 'e', 'π', 'exp', '√', '²', 7, 8, 9, '+', 4, 5, 6, "-", 1, 2, 3, '%', 0, ".", "/", "X"]
    ligne = 2
    collone = 0

    # boite d'expression/résultat
    resultat = Label(fenetre, bg='#101419', fg="#FFF", width=20, height=2, textvariable=equation, font=("", 30),
                     anchor=E)
    resultat.grid(columnspan=4)

    # affichage des boutons sur l'interface graphique
    for i in boutons:

        if i == 'AC':
            b = Label(fenetre, text=str(i), bg="red", height=3, width=9, font=('', 15, "bold"))
            # rende les boutons cliquable
            b.bind("<Button-1>", lambda e, bouton=i: appuyer_bouton(bouton))

            # retour a la ligne lorsqu'une ligne de bouton dépasse 4
            b.grid(row=ligne, column=collone)
            collone += 1

        else:
            b = Label(fenetre, text=str(i), bg="#C8C8C8", fg='#000000', height=3, width=9, font=('', 15, "bold"))
            # rende les boutons cliquable
            b.bind("<Button-1>", lambda e, bouton=i: appuyer_bouton(bouton))
            # retour a la ligne lorsqu'une ligne de bouton dépasse 4
            b.grid(row=ligne, column=collone)
            collone += 1

        if collone == 4:
            collone = 0
            ligne += 1

    # bouton resultat le contenu
    b = Label(fenetre, text='=', bg="#FF8809", fg='#FFF', height=2, width=12, font=('', 27))
    b.bind("<Button-1>", lambda e, bouton='=': appuyer_bouton(bouton))
    b.grid(column=2, columnspan=2, row=8)

    # bouton affichage historique
    historique = Label(fenetre, text='HISTORIQUE', bg="#868686", fg='#FFF', height=2, width=12, font=('', 27))
    historique.bind("<Button-1>", lambda e, bouton='historique': afficher_historique())
    historique.grid(column=0, columnspan=2, row=8)

    # afficher la fenetre
    fenetre.mainloop()
