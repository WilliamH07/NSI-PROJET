import time
import random
from colorama import Fore, Style

diviseur = 3
dividende = 0

while True:
    print('''\
 ________  ___       ________  ________   ________  _______          
|\   ____\|\  \     |\   __  \|\   ____\ |\   ____\|\  ___ \         
\ \  \___|\ \  \    \ \  \|\  \ \  \___|_\ \  \___|\ \   __/|        
 \ \  \    \ \  \    \ \   __  \ \_____  \\ \_____  \ \  \_|/__      
  \ \  \____\ \  \____\ \  \ \  \|____|\  \\|____|\  \ \  \_|\ \     
   \ \_______\ \_______\ \__\ \__\____\_\  \ ____\_\  \ \_______\    
    \|_______|\|_______|\|__|\|__|\_________\\_________\|_______|    
                                 \|_________\|_________|             
                                                                     
                                                                     ''')
    print("Entrez une liste d'élèves séparés par une virgule : ")
    list_elev = input()
    
    # Remplacez toutes les virgules par des espaces
    list_elev = list_elev.replace(',', ' ')
    
    # Divisez l'entrée utilisateur 
    list_sep = list_elev.split()
    
    # Initialisez un compteur et le dictionnaire pour le système de 3 élèves
    numero = 1 #Debuter le compteur 
    eleves = {} 
    resultats = {}
    students_assigned = set()
    
    # Initialisez le dictionnaire pour le système de 2 élèves
    resultats01 = {}
    
    # Attribuer un numéro pour chaque élève 
    for mot in list_sep:
        eleves[mot] = numero
        numero += 1
        
    print("Nombre total d'élèves : " + str(numero - 1))
    print(eleves)
    final = numero - 1

    def eleves_assign3(): #Fonction pour faire l'attribution des équipes de 3
        for groupe in range(1, int(ttgrp) + 1):
            # Vérifiez si la clé existe dans le dictionnaire
            if groupe not in resultats:
                resultats[groupe] = []

            for _ in range(3):
                while True:
                    eleve_selec = random.randint(1, final)

                    if eleve_selec not in students_assigned:
                        students_assigned.add(eleve_selec)
                        resultats[groupe].append(eleve_selec)
                        break


    if final > 0:
        
        if final % 3 == 0: #Si le nombre d'élèves est divisible par 3
            #print("debug00")
            ttgrp = final // 3
            print("On peut former : " + str(ttgrp) + " groupes de 3")

            eleves_assign3()
            
            for groupe, students in resultats.items():
                print(Fore.RED + "Résultats pour le groupe de 3", groupe, Fore.RESET)
                for student in students:
                    nom_eleve = list(eleves.keys())[list(eleves.values()).index(student)]
                    print(nom_eleve)




        else: #Si le nombre d'élèves n'est pas divisible par 3
            #print("debug01")
            dividende = final
            quotient = dividende // diviseur
            reste = dividende % diviseur
            
            
            groupe03 = quotient
            groupe02 = reste // 2
            
            if (reste % 2) == 0: #Si le nombre restant est pair 
                #print("debug02")
                print("On peut former : " + str(groupe03) + " d'équipes de 3 " +
                      "et " + str(groupe02) + " équipes de 2 : ")

                for groupe in range(1, int(groupe03) + 1):
                    # Vérifiez si la clé existe dans le dictionnaire
                    if groupe not in resultats:
                        resultats[groupe] = []

                    for _ in range(3):
                        while True:
                            eleve_selec = random.randint(1, final)

                            if eleve_selec not in students_assigned:
                                students_assigned.add(eleve_selec)
                                resultats[groupe].append(eleve_selec)
                                break
            

                
                for groupe, students in resultats.items():
                    print(Fore.RED + "Résultats pour le groupe de 3 numéro : ", groupe, Fore.RESET)
                    for student in students:
                        nom_eleve = list(eleves.keys())[list(eleves.values()).index(student)]
                        print(nom_eleve)
                        
            
                for groupe2_index in range(1, int(groupe02) + 1):
                    # Vérifiez si la clé existe dans le dictionnaire
                    if groupe2_index not in resultats01:
                        resultats01[groupe2_index] = []
                
                    for _ in range(2):
                        #print("debug03") 

                        while True:
                            eleve_selec = random.randint(1, final)
                
                            if eleve_selec not in students_assigned:
                                students_assigned.add(eleve_selec)
                                resultats01[groupe2_index].append(eleve_selec)
                                break
                
                for groupe2, students in resultats01.items():
                    print(Fore.RED + "Résultats pour le groupe de 2", groupe2, Fore.RESET)
                    for student in students:
                        nom_eleve = list(eleves.keys())[list(eleves.values()).index(student)]
                        print(nom_eleve)
 
                

            else:  # Si il n'est pas pair 
                grpelev = quotient - 1  # Soustrait quotient pour casser 1 groupe de 3
                finalv2 = grpelev // 2 + reste  # Nous donne le résultat total de groupes de 2

                for groupe in range(1, int(grpelev) + 1):
                    # Vérifiez si la clé existe dans le dictionnaire
                    if groupe not in resultats:
                        resultats[groupe] = []

                    for _ in range(3):
                        while True:
                            eleve_selec = random.randint(1, final)

                            if eleve_selec not in students_assigned:
                                students_assigned.add(eleve_selec)
                                resultats[groupe].append(eleve_selec)
                                break
                            
                for groupe2_index in range(1, int(finalv2) + 1):
                    # Vérifiez si la clé existe dans le dictionnaire
                    if groupe2_index not in resultats01:
                        resultats01[groupe2_index] = []
                
                    for _ in range(2):
                        #print("debug03") 
                        
                        
                        while True:
                            eleve_selec = random.randint(1, final)
                
                            if eleve_selec not in students_assigned:
                                students_assigned.add(eleve_selec)
                                resultats01[groupe2_index].append(eleve_selec)
                                break
                            
                    for groupe, students in resultats.items():
                        print(Fore.RED + "Résultats pour le groupe de 3 numéro : ", groupe, Fore.RESET)
                        for student in students:
                            nom_eleve = list(eleves.keys())[list(eleves.values()).index(student)]
                            print(nom_eleve)        
                            
                    for groupe2, students in resultats01.items():
                        print(Fore.RED + "Résultats pour le groupe de 2", groupe2, Fore.RESET)
                        for student in students:
                            nom_eleve = list(eleves.keys())[list(eleves.values()).index(student)]
                            print(nom_eleve)

                

    else:
        print("input invalide")
