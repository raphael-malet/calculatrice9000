#Je suis une calculatrice 9000, et je suis prêt à tout calculer pour toi !!!!
#doit se lancer sur macos pour avoir une interface graphique adapté

# importe interface graphique
import tkinter as tk
from tkinter import ttk
from tkinter import *

# set-up des expressions de debut
expression = ""
total = ""


# HISTORIQUE
def stockage_historique():
    global expression
    global total
    fichier_historique = open('historique.txt', 'a')
    fichier_historique.write(
        expression + '=' + total + '\n')  # on écrit l'expression et le résultat dans le fichier .txt
    fichier_historique.close()
    lecture_historique()


# fonction lecture du fichier historique.txt
def lecture_historique():
    global historique
    donnee_historique = open('historique.txt', 'r')
    # permet d'assigner la lecture de l'historique a une variable.
    donnee_historique = donnee_historique.readlines()

    if donnee_historique[-1] == NONE:
        pass
    else:
        donnee_historique = donnee_historique[-1]
        afficher_historique(historique, donnee_historique)


# afficher l'expression et son résultat dans l'historique
def afficher_historique(historique, expression):
    global total
    historique.insert(0, expression)


# focntion pour effacer l'historique
def effacer_historique_fichier():
    global historique

    historique_effacement = open('historique.txt', 'w')
    historique_effacement.write('')  # permet d'effacer le contenu de l'historique
    historique_effacement.close()
    lecture_historique()


# supprimer le contenu de l'historique
def supprimer_historique(historique):
    historique.delete(0, END)
    effacer_historique_fichier()


# fonction pour afficher l'historique dans la fenetre historique au lancement de l'application
def affichage_historique_ouverture_appli(historique):
    historique_ouverture = open('historique.txt', 'r')
    historique_ouverture = historique_ouverture.readlines()

    for i in range(len(historique_ouverture)):
        historique.insert(0, historique_ouverture[i])

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
        equation.set(expression)
        calculer()
        return

    # pour faire racine carré
    if touche == '\u221ax':
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
        if touche in range(0, 10) or touche == '(' or touche == ')':
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
    global historique

    # si le resultat est possible
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        stockage_historique()
        expression = total

    # si le resultat est impossible
    except:
        equation.set("erreur")
        total = "erreur"
        stockage_historique()
        total = ""
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

    # couleur de fond de la fenêtre
    fenetre.configure(background='#101419')

    # taille de la fenêtre
    fenetre.geometry("420x628")

    # Titre de l'application
    fenetre.title("Calculatrice9000")

    # variable pour stocker le contenu actuel
    equation = StringVar()

    # liste des boutons
    boutons = ['AC', '(', ')', 'e', 'π', 'exp', '\u221ax', '²', 7, 8, 9, '+', 4, 5, 6, "-", 1, 2, 3, '%', 0, ".", "/", "X"]
    ligne = 3
    collone = 0

    # boite d'expression/résultat
    resultat = Label(fenetre, bg='#101419', fg="#FFF", width=20, height=2, textvariable=equation, font=("", 30),
                     anchor=E)
    resultat.grid(columnspan=4)

    # fenetre historique
    historique = tk.Listbox(fenetre, height=5, font=('', 15))
    historique.grid(row=2, columnspan=4, sticky=EW)

    # Scrollbarr relier a l'historique
    scrollbar = ttk.Scrollbar(fenetre, orient='vertical', command=historique.yview)
    scrollbar.grid(row=2, column=3, sticky='nse')

    # communication entre la scrollbarr et le fenetre de l'historique
    historique['yscrollcommand'] = scrollbar.set

    # afficher l'historique lors de l'ouverture de l'appplication
    affichage_historique_ouverture_appli(historique)

    # affichage des boutons sur la fenêtre
    for i in boutons:

        # pour le boutton surrpimer l'expression en cours
        if i == 'AC':
            b = Label(fenetre, text=str(i), bg="red", height=3, width=9, font=('', 15, "bold"))
            # rende lee boutons cliquable
            b.bind("<Button-1>", lambda e, bouton=i: appuyer_bouton(bouton))
            # disposition du boutton sur la grille
            b.grid(row=ligne, column=collone)
            collone += 1

        # les autres boutons
        else:
            b = Label(fenetre, text=str(i), bg="#C8C8C8", fg='#000000', height=3, width=9, font=('', 15, "bold"))
            # rende les boutons cliquable
            b.bind("<Button-1>", lambda e, bouton=i: appuyer_bouton(bouton))
            # disposition des bouttons sur la grille
            b.grid(row=ligne, column=collone)
            collone += 1

        # retour a la ligne lorsqu'une ligne de bouton dépasse 4
        if collone == 4:
            collone = 0
            ligne += 1

    # bouton resultat le contenu
    b = Label(fenetre, text='=', bg="#FF8809", fg='#FFF', height=2, width=12, font=('', 27))
    b.bind("<Button-1>", lambda e, bouton='=': appuyer_bouton(bouton))
    b.grid(column=2, columnspan=2, row=9)

    # bouton affichage historique
    boutton_historique = Label(fenetre, text='AC Historique', bg="#868686", fg='#FFF', height=2, width=12,
                               font=('', 27))
    boutton_historique.bind("<Button-1>", lambda e, bouton='historique': [supprimer_historique(historique)])
    boutton_historique.grid(column=0, columnspan=2, row=9)

    # afficher la fenetre
    fenetre.mainloop()
