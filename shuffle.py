
#Jianxin You 20134401
#19 avril 2022

#Ce programme consiste à développer une jeu de carte comme une application web
# Le jeu solitaire est un jeu de carte joué seul et un jeu bien populaire
# depuis la conception de l'internet. C'est avec un jeu de cartes standard
# qu'il est possible de jouer (52 cartes). Le but principal du jeu est de
# piger 25 cartes et ce une par une pour les placer sur une grille de cartes
# 5x5. Chaque rangée constitue d'un pointage selon la mains de poker placée.
# Lorsque la dernière carte est placée, le jeu s'arrête nette et le pointage
# s'affiche à l'écran et une nouvelle partie recommence. Le joueur peut tout
# de même recommencer une partie à tout moment s'il les souhaite ainsi que
# déplacer ses cartes sur la grille comme il le veut.

#Les points sont représentés de cette façon:
#-(100 points) Quinte Flush Royale
#-(75 points) Quinte Flush
#-(50 points) Carré
#-(25 points) Full House
#-(20 points) Couleur ou Flush
#-(15 points) Quinte
#-(10 points) Brelan
#-(5 points) Double Paire
#-(2 points) Une Paire

# Cette fonction permet de mettre les éléments HTML dans le ''main''. Cette
# fonction HTML a pourtant pour but de créer une grille 5x5 avec des cases
# cases vides qui permettent de placer les cartes et ainsi être la plaquette
# de jeu. Elle permet de vérifier les positions et cliquer sur chaque case
#vide.
import functools

# couleurs des cartes
colors = ['S','H','D','C']

# crée les nombres des cartes et toutes les possibilites de cartes(king,queen
#...)
cartes = list(range(13))
cartes = list(map(lambda x:x+1,cartes))
cartes[0] = 'A'
cartes[10] = 'J'
cartes[11] = 'Q'
cartes[12] = 'K'

# cette fonction permet la repetition d'une fonction HTML tableau.Par exemple,
# cree un tableau avec la fonction onclick ou le contenu est a remplacer.
def case(contenue):
    pre = '<td id="case'
    post = ')"></td>'
    res = pre + str(contenue) + '" onclick="clic(' + str(contenue) + post
    return  res

#Cette fonction sert a afficher les nombres des rangees en repetitions dans
#le language html ou encore une fois le contenu signifie un chiffre entre 0
#et 24 pour chaque case(position).
def caseChiffreAffichage(contenue):
    pre = '<td id="case'
    post = '"></td>'
    return  pre + str(contenue) + post


# cette fonction organise une ligne du tableau dans html. Elle organise chaque
#rangee et colonne d'un tableau cree en html.
def tr(contenu): return '<tr>' + contenu + '</tr>'


# cette fonction organise un tableau html
# en combinant avec la paramètre contenu
# paramètres x et y sont utilisés pour positionner la tableau
def table(contenu,x,y):
    pre = '<table style="margin:'
    res = pre + str(x)+'% 0 0'
    post = ' ' + str(y) + '%">'
    res = res + post
    return res + contenu + '</table>'

# cette fonction sert a mettre ensemble la grille de cases vides ou elle sera
#la plaquette de jeu en d'autres mots. Grace aux boucles, il est possible de
#ramener une grille entiere sans avoir de repetitions de code.
def buildGrilleHTML():
    grille = list(range(25))
    res = []
    text = ''
    for i in range(25):
        text += case(i)
        if (i+1) % 5 == 0:
            res += tr(text)
            text = ''
    caseSpecial = table(tr(case(25)),1,15)
    res = caseSpecial+ table(''.join(res),1,20)
    return res
   
    
# cette fonction sert a afficher les points sur chaque ligne. Car chaque
#mains de poker peut se trouver sur la colonne ou la rangee.
def chiffreLigne():
   
    #Ici, le principe est de prendre un range minimum de points ainsi que les
    #positions des colonnes specifiquement afin de pouvoir detecter les points
    
    # les ids des cases qu'on mets les point sont de 30 à 34
    # case id 35 est sert à afficher la point total
    lig = list(range(30,36))
    lig = list(map(caseChiffreAffichage,lig))
    lig = list(map(tr,lig))
    pre = '<table style="border-collapse:separate; border-spacing:0px 38px;">'
    post = '</table>'
    res = pre + ''.join(lig) + post
    return res
   
    
# Cette fonction est similaire a la fonction de chiffreColonne(), mais affiche
# les points dans les colones
# les ids des cases qu'on mets les point sont de 30 à 34
def chiffreColone():
    col = list(range(40,45))
    col = list(map(caseChiffreAffichage,col))
    pre = '<table style="margin:-8% 0 0 42%">'
    post = '</table>'
    res = pre + ''.join(col) + post
    return res  

# Ici, la fonction donne l'allure initiale de la plaquette de jeu avec les
#cases vides et les boutons dont nouvelle partie ainsi que les points sur
# chaque ligne et colonne.
def initialiseHTML():

    html = buildGrilleHTML()
    styleTableau = ' <style> #main table td { border: 0; padding: 1px 2px; }'
    buttonStyle = '#main button {position: absolute;left: 50px; top:60px;}'
    styleTableau += buttonStyle+'#main table td img { height: auto; }</style>'
    button = '<button onclick="init()">Nouvelle </br> partie </button>'
    html = styleTableau +button + html + chiffreLigne() + chiffreColone()
    return html

#Cette fonction va initialiser le html dans sa forme initiale. chaque fois que
# cette fonction est mise en marche, la forme "vide" de la plaquette de jeu
#est mise.
def init():
   
   
    global grille       # tableau qui contient les cartes
    global state                  
    global carteDejaExiste
    
    # composante mouse est une valeur booleen
    # si mouse est égal à 1, une carte est notre stack
    # sinon, aucune carte est dans notre stack
    # compostant casePre est le id de la case qui est dans le stack
    state = struct(mouse = 0, casePre = -1)
   
    grille = [''] * 26   #  tableau qui contient les cartes
                         #  il y a 26 cartes qu'on peut opérer
   
    grille[25] = 'dos'   # 25ìme carte est la case spécial qui nous donne des
                         # nouvelles cartes
       
    carteDejaExiste = [] # une tableau pour éviter les mêmes cartes dans grille
   
    
   
    html = initialiseHTML()
    main = document.querySelector('#main')
    main.innerHTML= html
       
    mettreHTMLAJour()
   
# Cette partie permet de remplir une liste de dos(initialise une liste)
# sélection initiale de la souris
                                        # aucune carte=0, 1 carte=1                
def recupererCase(i):
    idCase = "#case" + str(i)
    return document.querySelector(idCase)


#Cette fonction retourne un booleen lorsque la grille est remplie de cartes.
def grilleEstPlein():
    for i in range(25):
        if grille[i] == '':
            return False
    return True

# Met à jour le HTML en lisant l'état interne du jeu


# cette fonction somme les points obtenus dans la tableau
def sommerPoints():
    somme = 0
    for i in range(30,35):
        case = recupererCase(i)
       
        # si il y a un nombre, on l'ajoute dans notre résultat
        if case.innerHTML:
            somme += int(case.innerHTML)
           
    for j in range(40,45):
        case = recupererCase(j)
        if case.innerHTML:
            somme += int(case.innerHTML)
    return somme
       
#cette fonction permet de mettre a jour le programme
def mettreHTMLAJour():
    
    # si on finit le jeu
    if grilleEstPlein():
        # ici le pointage final lorsque toutes les cases sont
        #remplies avec les cartes et arrete le jeu.
        sommeDesPoints = sommerPoints()
        bravo = 'Bravo, votre pointage final est '+str(sommeDesPoints)
        alert(bravo)
        init()
        
    # sinon, on ajoute l'image dans les cases
    for i in range(26):
        carte = grille[i]
        carteHTML = CarteHTML(carte)
        case = recupererCase(i)
        case.innerHTML = carteHTML

       
       
# Permet de savoir quelle carte a été sélectionnée et la met en vert comme
# background. Elle tourne verte seulement lorsqu'elle sélectionnée.
def setCaseGreen(n):
    case = recupererCase(n)
    case.setAttribute('style', 'background-color: lime')

# Afin de déselectionner une carte et que le background vert se retire, cette
# fonction permet de faire cela.
def cancelCaseGreen(n):
    case = recupererCase(n)
    case.removeAttribute('style')


# Permet de mettre à jour où la carte sélectionnée va avec la souris.
def clic(n):
   
    # si on a pas cliqué la souris, c'est à dire, aucune carte est prête
    if state.mouse == 0:
        # on doit tout abord sélectionner une carte
        # ou obtenir une carte dans la case spciale
        selectionUneCarte(n)
               
    # si on a déjà cliqué une carte
    # autrement dire, une carte est prête à opérer
    elif state.mouse == 1:
        
        # si le carte prête provient la case special
        if state.casePre == 25:
            deposeUneCarte(n)
           
        else:
            # si on clique la case special
            if n == 25:
                cliqueCaseSpecial(n)
            
            # si on clique une case qui n'est pas la case spéciale
            # et on a une carte dans le stack
            # alors, on échange ces deux carte
            else:    
                echangeDeuxCarte(n)
               
#Lorsqu'une carte est selectionnee, elle devient verte
# Le parametre n est le numero de case sur la grille. Dans un
# autre cas lorsque le joueur decide de bouger la carte de place directement
# sur la grille de jeu, il est egalement selectionne en vert.
def selectionUneCarte(n):
    global grille
   
    # si on clique une case vide, on fait rien 
    if grille[n] == '':
        return
    
    # si on clique la case spéciale, et la carte dans cette case est dos
    elif grille[n] == 'dos' and n == 25:  
        
        
        # on met une nouvelle carte dans la case spéciale
        randomCarte = carteRandomise()
        while randomCarte in carteDejaExiste:
            randomCarte = carteRandomise()
        grille[25] = randomCarte
        
        # on reflesh le state
        setCaseGreen(25)
        state.mouse = 1
        state.casePre = 25
        mettreHTMLAJour()
        
    # si on clique une case d'autre part
    else:
        setCaseGreen(n)
        state.mouse = 1
        state.casePre = n


#cette fonction permet de deposer une carte vers une autre position. De plus,
#lorsque la carte est deposee, la couleur vert lime est enlevee pour signifier
# la deselection dune carte. 
def deposeUneCarte(n):
    if grille[n] == '':
        cancelCaseGreen(state.casePre)
        
        grille[n] = grille[state.casePre]
        grille[25] = 'dos'
        
        mettreHTMLAJour()
        state.mouse = 0
        ajouterDesPoints(n)
    else:
        cancelCaseGreen(25)
        setCaseGreen(n)
        state.casePre = n
        

#Lorsque la carte est a dos, dite special, elle permet sa selection, 
#lorsqu'elle est selectionnee une carte random dans le deck apparait. 
# Des que le joueur clique sur le dos de la carte, la carte random du deck se
#met a "face". Le vert est mis lorsque la carte est mise en face et cancelled
#lorsqu'elle est deselectionnee c'est-a-dire deposee ou une autre carte est
#selectionnee. n est pour la position de la grille. Qui ici est la carte a dos
#dans le deck alors 25.
def cliqueCaseSpecial(n):
    if grille[25] == 'dos':
        randomCarte = carteRandomise()
        while randomCarte in carteDejaExiste:
            randomCarte = carteRandomise()
            grille[25] = randomCarte
            setCaseGreen(25)
            
            cancelCaseGreen(state.casePre)
            state.casePre = 25
            mettreHTMLAJour()
     
    else:
        cancelCaseGreen(state.casePre)
        setCaseGreen(25)
        state.casePre = 25
        

#Cette fonction permet lechange entre deux cartes de position des qu'une carte 
#est selectionnee dans la grille elle devient verte et lorsqu'une autre carte 
#dans la grille est selectionnee, il est possible de faire un echange dans 
# la position de ces deux cartes. n etant le numero de la case(position).           
def echangeDeuxCarte(n):  
    cancelCaseGreen(state.casePre)
    
    # echange les elements
    tmp = grille[n]
    grille[n] = grille[state.casePre]
    grille[state.casePre] = tmp
    
    mettreHTMLAJour()
    
    # reflesh le state
    state.mouse = 0
    ajouterDesPoints(n)
    ajouterDesPoints(state.casePre)
   
               
#Permet d'aller chercher les fichiers d'images de cartes de codebooth: case
# vide, le dos de la carte et le deck de carte. Cette fonction permet
#aucune repetition dans le code. Les images de cartes sont generees par 
#codebooth.
def CarteHTML(cart):
    if cart == '':
        return '<img src="http://codeboot.org/cards/empty.svg">'
    elif cart == 'dos':
        return '<img src="http://codeboot.org/cards/back.svg">'
    else:
        pre = '<image src="http://codeboot.org/cards/'
        post = '.svg">'
        res = pre + cart + post
        return res
       
# Cette fonction permet de randomisé le deck de cartes du jeu. Toutes les
# cartes sont de dos auparavant et ainsi lorsque le joueur clique sur le deck
# de cartes. Une carte random du deck apparait.
def carteRandomise():
    nombreRandom = math.floor(52*random())
    color = nombreRandom % 4
    nombre = nombreRandom // 4    
    carte = str(cartes[nombre]) + str(colors[color])
    return carte

# cette fonction permet d'analyser les points de chaque colonne et ligne et 
#ainsi les additionner. ou n est la rangee ou colonne des points. Si aucun 
#point n'a ete fait sur une certaine ligne ou colonne, la fonction n'additonne
#pas ce "rien".
def ajouterDesPoints(n):

    ligne = retireLigne(n)
    colone = retireColone(n)
    
    # on vérifie si on obtient les points
    lignePoint = verifierPoints(ligne)
    colonePoint = verifierPoints(colone)
   
    # si on obtient les points, on les ajout dans leurs cases associées
    if lignePoint > 0:
        afficherPointLigne(n//5,lignePoint)
    else:
        afficherPointLigne(n//5,'')
       
    if colonePoint > 0:
        afficherPointColone(n%5,colonePoint)
    else:
        afficherPointColone(n%5,'')
    
    somme = sommerPoints()
    # case avec id 35 est la case qu'on met les points totals
    case = recupererCase(35)
    if somme != 0:
        case.innerHTML = str(somme)
    else:
        case.innerHTML = ''

        
        
#Cette fonction permet d'afficher les points de la colonne ou elle 
#se trouve ou n est la case (position) et point est le pointage donne.
# les ids de nos cases colones sont des nombres de 40 à 44
def afficherPointColone(n,point):
    case = recupererCase(40+n)
    case.innerHTML = str(point)

    
#Cette fonction permet d'afficher les points de la ligne elle
#se trouve ou n est la case (position) et point est le pointage donne. 
# les ids de nos cases ligns sont des nombres de 30 à 34
def afficherPointLigne(n,point):
    case = recupererCase(30+n)
    case.innerHTML = str(point)
       
   
# cette fonction retourne la ligne où se trouve une carte
# paramètre n est l'index de la carte
def retireLigne(n):
    if n == 25:
        return
    niemeLigne = n//5
    res = []
    index = niemeLigne * 5
    for i in range(index,index+5):
        
        res.append(grille[i])
    return res
   
# cette fonction retourne la colonne où se trouve une carte  ou n est la 
# positon (numero de case dans la grille).  
def retireColone(n):
    if n == 25:
        return
    index = n % 5
    res = []
    while(index < 25):
        res.append(grille[index])
        index += 5
       
    return res
       
    
# Cette fonction permet de verifier les points lorsqu'une main de 
#poker a ete mise dans la grille de jeu. Chacune des possibilites de main
#dependemment de la rarete dans le jeu a des points specifiques.   
def verifierPoints(tab):
   
    # on retire les éléments qui sont pas nuls.
    tabNonVide = []
    for elem in tab:
        if elem != '':
            tabNonVide.append(elem)    
    
    # on vérifie chaque main cartes
    if quinteFlushRoyale(tabNonVide.copy()):
        return 100
   
    elif quinteFlush(tabNonVide.copy()):
        return 75
   
    elif carre(tabNonVide.copy()):
        return 50
   
    elif fullHouse(tabNonVide.copy()):
        return 25
   
    elif couleurOuFlash(tabNonVide.copy()):
        return 20

    elif quinte(tabNonVide.copy()):
        return 15
   
    elif brelan(tabNonVide.copy()):
        return 10
   
    elif doublePaire(tabNonVide.copy()):
        return 5
   
    elif unePaire(tabNonVide.copy()):
        return 2

    return 0


#Cette fonction est un algorithme bien connu , un algorithme de classement de
#tableau ou le tri est en bulle.
def trierBubble(tab):

    echange = True
    while echange:
        echange = False
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
                echange = True  
    return tab


       
#Cette fonction permet la main de poker Full House : Trois cartes de même valeur 
#etune paire de cartes de même valeur
#ou tabest soit la ligne ou tab est soit la ligne ou
# la colonne ou la main de poker est presente. Elle retourne un boleen True
#lorsque le joueur reussi a execute cette main. Sinon false.                 
def fullHouse(tab):
    if len(tab) != 5:
        return False
   
    indexARemove = brelan(tab.copy())
    if not indexARemove:
        return False

    tab = removeElement(tab,indexARemove)
   
    return True if unePaire(tab) else False
   
    
    
# cette fonction vérifie si tous les éléments dans le tableau sont mêmes, ou
#tab est le tableau de cartes sur une colonne ou rangee. Cette fonction 
#permet seulement une analyse et retourne un boleen afin d'etre appeler dans
#une autre fonction a cet effet.
def toutesSontMemes(tab):
   
    elemPre=tab[0]
    for i in range(1, len(tab)):
        if tab[i]!=elemPre:
            return False
       

    return True



# cette fonction eneleve la couleur des cartes pour n'avoir que sa valeur.
#elle retourne un tableau sans la couleur avec les elements. Cette fonction
#permet lanalyse de la valeur seule des cartes.
def retireCouleur(tab):
    for i in range(len(tab)):
        tab[i] = tab[i][-1]
    
    return tab
 

#Cette fonction retire la valeur des cartes que pour obtenir la couleur de 
#carte. ou tabest le tableau de carte sur la colonne ou ligne de la grille.
#Cela permet l'analyse seule de la couleur d'une carte dans la grille.   
def retireNombre(tab):
    for i in range(len(tab)):
        tab[i] = tab[i][:-1]
       
    return tab



#cette fonction permet de convertir les cartes speciales dont king, as, etc, a
# un nombre dans le tableau afin de simplifier l'analyse dans le code. Cela
#permet de donner une positiona ces cartes-la dans le tableau. ou tab est le
#tableau.
def convertLettreANombre(tab):
    for i in range(len(tab)):
        if tab[i] == 'A':
            tab[i] = 1
           
        elif tab[i] == 'J':
            tab[i] = 11
           
        elif tab[i] == 'Q':
            tab[i] = 12
           
        elif tab[i] == 'K':
            tab[i] = 13
           
        else:
            tab[i] = int(tab[i])
           
    return tab
   
# cette fonction trie un tableau de cartes
# les cartes dans ce tableau doivent être retirés leurs couleurs
# et les cartes ne doivent pas contenir les lettres
def trierCartes(tab):    
    tabNouveau = []
   
    # si il y a un '1', on doit le retirer en tout d'abord
    for i in range(len(tab)):
        if tab[i] != 1:
            tabNouveau.append(tab[i])
    tabTrie = trierBubble(tabNouveau)
   
   
    # on verifie si l'incrément est un ou non
    elementPre = tabTrie[0]
    for i in range (1,len(tabTrie)):
        if tabTrie[i] != (elementPre + 1):
            return False
        elementPre = tabTrie[i]
       
    # on ajout '1' dans sa position approprié
    if len(tabTrie) == 4:
        if tabTrie[-1] == 13:
            tabTrie.append(1)
            
            return tabTrie
        elif tabTrie[0] == 2:
            tabTrie = [1] + tabTrie
            return tabTrie
        return False
    return tabTrie


#Cette fonction permet la main de poker quint flush royal:L'as, le roi,
#la dame, le valet et le 10 d'une même couleur. ou tab est soit la ligne ou
# la colonne ou la main de poker est presente. Elle retourne un boleen True
#lorsque le joueur reussi a execute cette main. Sinon false. 

def quinteFlushRoyale(tab):
    if len(tab) != 5:
        return False
    
    if not quinteFlush(tab):
        return False
    
    # après on apple la fonction quinteFlush, le tab est changé
    # et le tab est trié et juste contient les nombres
    # si le dernier element n'est pas 1, autremenr dit, n'est pas AS
    # return False
    if tab[-1] != 1:
        return False
    return True
   
   


#Cette fonction permet la main de poker Quinte Flush : Cinq cartes de même couleur
#qui se suivent outab est soit la ligne ou
#la colonne ou la main de poker est presente. Elle retourne un boleen True
#lorsque le joueur reussi a execute cette main. Sinon false.     
def quinteFlush(tab):
    if len(tab) != 5:
        return False
    
    tabSansNombre = retireCouleur(tab.copy())
    if not toutesSontMemes(tabSansNombre):
        return False
    
    # si les couleurs sont mêmes. on vérifie si ils sont dans bon ordre
    if not quinte(tab):
        return False
    return True

    
    
#Cette fonction permet la main de poker Carré : Quatre cartes de même valeur
#ou tabest soit la ligne ou tab est soit la ligne ou
# la colonne ou la main de poker est presente. Elle retourne un boleen True
#lorsque le joueur reussi a execute cette main. Sinon false.     
def carre (tab):
    tabSansCouleur = retireNombre(tab.copy())
    if len(tab) == 5:
        for i in range(len(tabSansCouleur)):
            if toutesSontMemes(tabSansCouleur[:i]+tabSansCouleur[i+1:]):
                return True
    elif len(tab) == 4:
        return toutesSontMemes(tabSansCouleur)
       
    return False




#Cette fonction permet la main de poker Couleur ou Flush : Toutes les cartes de
#même couleur
# la colonne ou la main de poker est presente. Elle retourne un boleen True
#lorsque le joueur reussi a execute cette main. Sinon false. 
def couleurOuFlash(tab):
    if len(tab) != 5:
        return False
    tabSansNombre = retireCouleur(tab.copy())
    return toutesSontMemes(tabSansNombre)
       

    
#Cette fonction permet la main de poker Quinte : Cinq cartes qui se suivent
#ou ab est soit la ligne ou tab est soit la ligne ou
# la colonne ou la main de poker est presente. Elle retourne un boleen True
#lorsque le joueur reussi a execute cette main. Sinon false.     
def quinte(tab):
    if len(tab) != 5:
        return False
    tabSansCouleur = retireNombre(tab)
    tabDeNombre = convertLettreANombre(tabSansCouleur)
    return True if trierCartes(tabDeNombre) else False    
   

    
#Cette fonction permet la main de poker Brelan : Trois cartes de même valeur 
# la colonne ou la main de poker est presente. 
# Elle retourne un tableau des index ou se trouve ces trois cartes de même 
# valeur,lorsque le joueur reussi a execute cette main. Sinon false.     
def brelan(tab):
    # on essaie trouver si il y a trois meme cartes
    tabNouveau = retireNombre(tab.copy())
    longueur = len(tabNouveau)
    indexARemove = []
    for i in range(longueur):
        for j in range(i+1,longueur):
            for k in range(j+1,longueur):
                # si on trouve il y a trois même cartes
                if tabNouveau[i] == tabNouveau[j] == tabNouveau[k]:
                    indexARemove.extend([i,j,k])
    if not indexARemove:
        return False
    return indexARemove
   

    
#Cette fonction permet d'enlever des elements du tableau, Cela permet l'analyse
#d'un tableau ou eleminant les cartes du tableau. ou tab est le tableau de 
#cartes sur la ligne ou colonne et indexAremove est un tableau d'index à remove
def removeElement(tab,indexARemove):
    # on trie les index
    indexARemove = trierBubble(indexARemove)
    
    # nombre pour compter on a déjà eliminé combien d'index
    nombre = 0
    for elem in indexARemove:
        elem -= nombre
        tab.pop(elem)
        nombre += 1
       
    return tab



#Cette fonction permet la main de poker Double Paire : Une paire de cartes de
#même valeur et une autre paire de cartes de même valeur 
# la colonne ou la main de poker est presente. Elle retourne un boleen True
#lorsque le joueur reussi a execute cette main. Sinon false.
def doublePaire(tab):
    if len(tab) < 4:
        return False
    
    # si il y a une paire, indexARemove va contenir 
    # les index de ces deux nombres
    indexARemove = unePaire(tab.copy())
    if not indexARemove:
        return False
    
 # ici il y a analyse du tableau ou deux elements sont elemines lorsqu'ils
# sont pareils alors pour avoir deux Paires.
    tab = removeElement(tab,indexARemove)
    return True if unePaire(tab) else False

   
# cette fonction vérifie si un tableau contient une paire de cartes de
# même nombres, si oui, retourne des index de ces deux cartes
# sinon, retourne False
def unePaire(tab):
    if len(tab) <= 1:
        return False
    tab = retireNombre(tab)
 
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            if tab[i] == tab[j]:
                return [i,j]
         
    return False


#Cette fonction permet de faire des tests sur le jeu, principalement les mains
#de poker du jeu, les fonctions associees aux mains de poker et la generation
#des fichiers de l'image d'une carte.
def testUnitaires():
    
    assert unePaire(['AS','2S','3S','4S','5S']) == False
    assert unePaire(['AS','AD','3S']) == [0,1]
    assert unePaire(['AS','2S','AD','4S','8S']) == [0,2]
    
    assert doublePaire(['AS','1D','3S','3D','AS']) == True
    assert doublePaire(['AS','2S','3S','4S','5S']) == False
    assert doublePaire(['AS','2S']) == False
    
    assert brelan(['2S','2D','4S','5S','2C']) == [0,1,4]
    assert brelan(['AS','2S','3S']) == False
    assert brelan(['8S','8D','8C']) == [0,1,2]
    
    assert quinte(['AS','2S','3S','4S','5S']) == True
    assert quinte(['AS','2S','3S']) == False
    assert quinte(['AS','2S','3S','4S','8S']) == False
                   
    assert couleurOuFlash(['3S','9S','4S','10S','1S']) == True
    assert couleurOuFlash(['2D','4D','1D','5D','8D']) == True
    assert couleurOuFlash(['2D','3D']) == False
    
    assert fullHouse(['8D','8S']) == False
    assert fullHouse(['8D','8S','8H']) == False
    assert fullHouse(['8D','8S','8H','2C','2D']) == True
    
    assert carre(['AD','2D','3D']) == False
    assert carre(['2D','2S','2H','2C']) == True
    assert carre(['8D','8S','8H','8C','10D']) == True
    
    assert quinteFlush(['AD','2D','3D','4D','5D']) == True
    assert quinteFlush(['2D','3D','4D','5D','6D']) == True
    assert quinteFlush(['2D','3D','4D','5D','8D']) == False
    
    assert trierCartes([2,3,4,5,1]) == [1,2,3,4,5]
    assert trierCartes([12,10,11,13,1]) == [10,11,12,13,1]
    assert trierCartes([8,9,10,6,7]) == [6,7,8,9,10]
    
    assert quinteFlushRoyale(['10D','JD','QD','KD','AD']) == True
    assert quinteFlushRoyale(['10D']) == False
    assert quinteFlushRoyale(['10S','JS','QS','KS','AS']) == True
    
    assert toutesSontMemes(['10H','1S'])==False
    assert toutesSontMemes(['KD', 'KD'])==True
    assert toutesSontMemes(['QH', 'JC', '10S'])==False

    assert retireNombre(['QH','JC','10S'])==['Q','J','10']
    assert retireNombre(['AD','2H','3S','4C'])== ['A','2','3','4']
    assert retireNombre(['AS','2S','3S','4S'])==['A','2','3','4']

    assert retireCouleur(['QH', 'JC', '10S'])== ['H', 'C', 'S']
    assert retireCouleur(['AS','2S','3S','4S'])==['S','S','S','S']
    assert retireCouleur(['AD', '2H', '3S', '4C'])==['D', 'H', 'S', 'C']
    
    assert trierBubble([3,2,5,10,1,-1])==[-1,1,2,3,5,10]
    assert trierBubble([-4,-7,10,1])==[-7,-4,1,10]
    assert trierBubble([150,-1,4,7])==[-1,4,7,150]
   
    assert CarteHTML('')=='<img src="http://codeboot.org/cards/empty.svg">'
    assert CarteHTML('dos')=='<img src="http://codeboot.org/cards/back.svg">'
    assert CarteHTML('QH')=='<image src="http://codeboot.org/cards/QH.svg">'
   
    assert toutesSontMemes(['10H','1S'])==False
    assert toutesSontMemes(['KD', 'KD'])==True
    assert toutesSontMemes(['10S', '10S', '10S'])==True
init()
