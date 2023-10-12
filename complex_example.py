#BACKUp
# Importation des modules n√©cessaires
import tkinter
import tkinter.messagebox
import customtkinter

import random
from colorama import Fore, Style

diviseur = 3
dividende = 0
final = 0
student_choices = {}
# Initialisez un compteur et le dictionnaire pour le syst√®me de 3 √©l√®ves
numero = 1  # D√©buter le compteur
eleves = {}  # Nom + Num√©ro
resultats = {}
students_assigned = set()

# Initialisez le dictionnaire pour le syst√®me de 2 √©l√®ves
resultats01 = {}

# Configuration de l'apparence et du th√®me par d√©faut
customtkinter.set_appearance_mode(
    "Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ToplevelWindow(customtkinter.CTkToplevel):

  def __init__(self, app, group):
    super().__init__(app)
    self.geometry("400x120")
    # Configuration de la grille (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2), weight=1)
    self.title("Groupe num√©ro : " + str(group))  # Titre de la fen√™tre

    self.resultats = resultats
    print(resultats)
    if group in self.resultats:
      liste_correspondante = self.resultats[group]
      liste_formatee = ', '.join(map(str, liste_correspondante))
      print("Liste correspondante au groupe", group, ":", liste_formatee)

      # D√©truisez les widgets existants dans la fen√™tre Toplevel
      for widget in self.winfo_children():
        widget.destroy()

      # Affichez les noms des √©l√®ves pour le groupe sp√©cifi√©
      for student_number in liste_correspondante:
        nom_eleve = list(eleves.keys())[list(
            eleves.values()).index(student_number)]
        label_texte_supplementaire = customtkinter.CTkLabel(self,
                                                            text="√âl√®ve : " +
                                                            str(nom_eleve))
        label_texte_supplementaire.pack(padx=40, pady=5)
    else:
      print("Le groupe", group, "n'existe pas dans le dictionnaire.")


class ToplevelWindow02(customtkinter.CTkToplevel):

  def __init__(self, app, group02):
    super().__init__(app)
    self.geometry("400x120")
    # Configuration de la grille (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2), weight=1)
    self.title("Groupe numero : " + str(group02))  # Titre de la fen√™tre

    self.resultats01 = resultats01
    print(resultats)
    if group02 in self.resultats01:
      liste_correspondante = self.resultats01[group02]
      liste_formatee = ', '.join(map(str, liste_correspondante))
      print("Liste correspondante au groupe", group02, ":", liste_formatee)

      # D√©truisez les widgets existants dans la fen√™tre Toplevel
      for widget in self.winfo_children():
        widget.destroy()

      # Affichez les noms des √©l√®ves pour le groupe sp√©cifi√©
      for student_number in liste_correspondante:
        nom_eleve = list(eleves.keys())[list(
            eleves.values()).index(student_number)]
        label_texte_supplementaire = customtkinter.CTkLabel(self,
                                                            text="Eleve : " +
                                                            str(nom_eleve))
        label_texte_supplementaire.pack(padx=40, pady=5)
    else:
      print("Le groupe", group02, "n'existe pas dans le dictionnaire.")


class ToplevelWindowPaires_create(customtkinter.CTkToplevel):
    def __init__(self, app, use_elev):
        super().__init__(app)
        self.geometry("400x400")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.title("Eleve : " + use_elev)

        self.selected_students = []  # Pour stocker les √©l√®ves s√©lectionn√©s

        # Cr√©ation d'une CustomScrollableFrame pour afficher les √©l√®ves
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Liste des eleves")
        self.scrollable_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Ajout des cases √† cocher pour chaque √©l√®ve
        for i, student in enumerate(list_sep, start=1):
            if student != use_elev:  # Ne pas inclure l'√©l√®ve actuel
                frame = customtkinter.CTkFrame(master=self.scrollable_frame)
                frame.grid(row=i, column=0, padx=10, pady=(0, 20))

                # Ajouter une case √† cocher pour chaque √©l√®ve
                check_var = tkinter.BooleanVar()
                checkbox = customtkinter.CTkCheckBox(
                    master=frame,
                    text=f" N°{eleves[student]}  {student}",
                    variable=check_var,
                    command=lambda s=student: self.on_checkbox_click(use_elev, s)
                )
                checkbox.pack()

    def on_checkbox_click(self, current_student, selected_student):
        global student_choices

        if selected_student not in self.selected_students:
            self.selected_students.append(selected_student)
            print(f"Eleve selectionne : {selected_student}")

            # Mettre √† jour le dictionnaire des choix
            student_choices[current_student] = selected_student

            if len(self.selected_students) >= 2:
            
                print("Trop d'eleves selectionnes")
                self.label_error = customtkinter.CTkLabel(master=self, text="NE SELECTIONNE UNIQUEMENT 1 ELEVE")
                self.label_error.grid(row=2, column=1, padx=20, pady=(0, 10))
                self.selected_students.remove(selected_student)
                del student_choices[current_student]
                print(student_choices)
        else:
            self.selected_students.remove(selected_student)
            del student_choices[current_student]
            print(f"Eleve deselectionne : {selected_student}")






class ToplevelWindowPaires(customtkinter.CTkToplevel):
  def open_group_window_create_pair(self, student):
    use_elev = student
    # Fermez la fen√™tre Toplevel existante s'il y en a une
    if self.toplevel_window_paires_create and self.toplevel_window_paires_create.winfo_exists(
    ):
      self.toplevel_window_paires_create.destroy()

    self.toplevel_window_paires_create = ToplevelWindowPaires_create(
        self, use_elev)
    print(resultats)
  def __init__(self, app):
    super().__init__(app)
    self.geometry("400x480")
    # Configuration de la grille (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2), weight=1)
    self.title("Créer ")  # Titre de la fen√™tre
    self.toplevel_window_paires_create = None
    self.scrollable_frame = customtkinter.CTkScrollableFrame(
        self, label_text="Listes des eleves")
    self.scrollable_frame.grid(row=0,
                               column=1,
                               padx=(20, 20),
                               pady=(20, 0),
                               sticky="nsew")
    self.scrollable_frame.grid_columnconfigure(0, weight=1)
    self.scrollable_frame_switches = []  # R√©initialiser la liste
    global list_sep
    for i, student in enumerate(list_sep, start=1):
      frame = customtkinter.CTkFrame(master=self.scrollable_frame)
      frame.grid(row=i, column=0, padx=10, pady=(0, 20))
      self.scrollable_frame_switches.append(frame)

      label = customtkinter.CTkButton(
          master=frame,
          text=f" N°{eleves[student]}  {student}",
          command=lambda student=student: self.open_group_window_create_pair(student))
      label.pack()


# D√©finition de la classe principale de l'application
class App(customtkinter.CTk):

  def __init__(self):
    super().__init__()
    # Initialisez le dictionnaire resultats ici
    self.resultats = {}
    self.resultats01 = {}

    # Configuration de la fen√™tre principale
    self.title("Made By William")  # Titre de la fen√™tre
    self.geometry(f"{1100}x{580}")  # G√©om√©trie de la fen√™tre

    # Configuration de la grille (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2), weight=1)

    # Cr√©ation du cadre lat√©ral avec des widgets
    self.sidebar_frame = customtkinter.CTkFrame(self,
                                                width=140,
                                                corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(4, weight=1)

    # Ajout d'une √©tiquette de logo
    self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                             text="NSI - CLASS",
                                             font=customtkinter.CTkFont(
                                                 size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    # Cr√©ation de boutons dans la barre lat√©rale
    self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,
                                                    text="PRINT",
                                                    command=self.create_group,
                                                    state="disabled")
    self.sidebar_button_3.grid(row=1, column=0, padx=20, pady=10)

    # Ajout d'options de personnalisation d'apparence
    self.appearance_mode_label = customtkinter.CTkLabel(
        self.sidebar_frame, text="Appearance Mode:", anchor="w")
    self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
    self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
        self.sidebar_frame,
        values=["Light", "Dark", "System"],
        command=self.change_appearance_mode_event)

    self.appearance_mode_optionemenu.grid(row=6,
                                          column=0,
                                          padx=20,
                                          pady=(10, 10))

    # Ajout d'options de mise √† l'√©chelle de l'interface utilisateur
    self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                text="UI Scaling:",
                                                anchor="w")
    self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
    self.scaling_optionemenu = customtkinter.CTkOptionMenu(
        self.sidebar_frame,
        values=["80%", "90%", "100%", "110%", "120%"],
        command=self.change_scaling_event)
    self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    # Cr√©ation d'un onglet "Eleves"
    self.tabview = customtkinter.CTkTabview(self, width=250)
    self.tabview.grid(row=0,
                      column=3,
                      padx=(20, 20),
                      pady=(20, 0),
                      sticky="nsew")
    self.tabview.add("Eleves")  # Placer l'onglet "Eleves" ici
    self.tabview.add("Paires")
    self.tabview.add("Tab 3")

    self.tabview.tab("Eleves").grid_columnconfigure(
        0, weight=1)  # Configuration de la grille des onglets individuels
    self.tabview.tab("Paires").grid_columnconfigure(0, weight=1)

    # Ajout de plusieurs widgets √† l'interface utilisateur

    self.total_eleves_label = customtkinter.CTkLabel(
        self.tabview.tab("Eleves"), text="Aucuns eleves")
    self.total_eleves_label.grid(row=3, column=0, padx=20, pady=(0, 10))

    self.string_input_button = customtkinter.CTkButton(
        self.tabview.tab("Eleves"),
        text="Ajouter des eleves",
        command=self.open_input_dialog_event)
    self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

    # Cr√©ez une √©tiquette pour afficher le nombre total d'√©l√®ves sous le bouton
    self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Paires"),
                                              text="Creer des paires d'eleves")
    self.label_tab_2.grid(row=3, column=0, padx=20, pady=(10, 10))

    self.label_tab_3 = customtkinter.CTkButton(
        self.tabview.tab("Paires"),
        text="Create",
        command=self.open_group_window_paires)
    self.label_tab_3.grid(row=2, column=0, padx=20, pady=(10, 10))

    self.appearance_mode_optionemenu.set("Dark")
    self.scaling_optionemenu.set("100%")
    self.toplevel_window = None
    self.toplevel_window02 = None
    self.toplevel_window_paires = None
    self.toplevel_window_paires_create = None

  def eleves_assign3(self):
    global final  # Ajoutez ceci pour acc√©der √† la variable globale final
    global students_assigned  # Ajoutez ceci pour acc√©der √† la variable globale students_assigned

    ttgrp = final // 3  # Utilisez final pour le nombre total de groupes

    for groupe in range(1, int(ttgrp) + 1):
      if groupe not in resultats:
        resultats[groupe] = []

      for _ in range(3):
        while True:
          eleve_selec = random.randint(1, final)

          if eleve_selec not in students_assigned:
            students_assigned.add(eleve_selec)
            resultats[groupe].append(eleve_selec)
            break

  def affichage_result(self):
    # Cr√©ation d'un cadre d√©roulant
    self.scrollable_frame = customtkinter.CTkScrollableFrame(
        self, label_text="Groupes 03")
    self.scrollable_frame.grid(row=0,
                               column=1,
                               padx=(20, 320),
                               pady=(25, 0),
                               sticky="nsew")
    self.scrollable_frame.grid_columnconfigure(0, weight=1)
    self.scrollable_frame_switches = []  # R√©initialiser la liste

    # Cr√©ation d'un cadre d√©roulant 02
    self.scrollable_frame02 = customtkinter.CTkScrollableFrame(
        self, label_text="Groupes 02")
    self.scrollable_frame02.grid(row=0,
                                 column=1,
                                 padx=(320, 20),
                                 pady=(25, 0),
                                 sticky="nsew")
    self.scrollable_frame02.grid_columnconfigure(0, weight=1)
    self.scrollable_frame02_switches = []  # R√©initialiser la liste

    for groupe, students in resultats.items():
      print(Fore.RED + "Resultats pour le groupe de 3 num√©ro : ", groupe,
            Fore.RESET)

      if students:
        nom_eleve = list(eleves.keys())[list(eleves.values()).index(
            students[0])]
        prenom_eleve = nom_eleve.split()[0]

      for student in students:
        nom_eleve = list(eleves.keys())[list(eleves.values()).index(student)]
        frame = customtkinter.CTkFrame(master=self.scrollable_frame)
        frame.grid(row=groupe, column=0, padx=10, pady=(0, 20))
        self.scrollable_frame_switches.append(frame)

        button = customtkinter.CTkButton(
            master=frame,
            text=f" N°{groupe}  {prenom_eleve}",
            command=lambda group=groupe: self.open_group_window(group))
        button.pack()
        print(nom_eleve)

    for groupe2, students in resultats01.items():
      print(Fore.RED + "Resultats pour le groupe de 2", groupe2, Fore.RESET)
      if students:
        nom_eleve = list(eleves.keys())[list(eleves.values()).index(
            students[0])]
        prenom_eleve = nom_eleve.split()[0]

      for student in students:
        nom_eleve = list(eleves.keys())[list(eleves.values()).index(student)]
        frame02 = customtkinter.CTkFrame(master=self.scrollable_frame02)
        frame02.grid(row=groupe2, column=0, padx=10, pady=(0, 20))
        self.scrollable_frame02_switches.append(frame02)

        button02 = customtkinter.CTkButton(
            master=frame02,
            text=f" N°{groupe2}  {prenom_eleve}",
            command=lambda group02=groupe2: self.open_group_window02(group02))
        button02.pack()
        print(nom_eleve)

  def open_input_dialog_event(self):
    global numero
    global eleves
    global final
    global students_assigned
    global resultats
    global resultats01
    global list_sep
    numero = 1
    eleves = {}
    students_assigned = set()
    resultats = {}
    resultats01 = {}

    dialog = customtkinter.CTkInputDialog(
        text="Entrer la liste des eleves dans ce format : E1, E2, ... ",
        title="Liste Eleves")

    eleves_list = dialog.get_input()
    eleves_list = eleves_list.replace(',', ' ')
    list_sep = eleves_list.split()

    for mot in list_sep:
      eleves[mot] = numero
      numero += 1

    final = numero - 1

    self.total_eleves_label = customtkinter.CTkLabel(
        self.tabview.tab("Eleves"),
        text="Nombre total d'eleves : " + str(final))
    self.total_eleves_label.grid(row=3, column=0, padx=20, pady=(0, 10))

    if final > 2:

      if final % 3 == 0:
        ttgrp = final // 3

        self.total_eleves_label2 = customtkinter.CTkLabel(
            self.tabview.tab("Eleves"),
            text="Nombre total groupe(s) de 3 : " + str(ttgrp))
        self.total_eleves_label3 = customtkinter.CTkLabel(
            self.tabview.tab("Eleves"), text="Nombre total groupe(s) de 2 : 0")
        self.total_eleves_label2.grid(row=4, column=0, padx=20, pady=(0, 10))

        self.eleves_assign3()
        self.affichage_result()

      else:

        dividende = final
        quotient = dividende // diviseur
        reste = dividende % diviseur

        groupe03 = quotient
        groupe02 = reste // 2

        if (reste % 2) == 0:
          self.total_eleves_label2 = customtkinter.CTkLabel(
              self.tabview.tab("Eleves"),
              text="Nombre total groupe(s) de 3 : " + str(groupe03))
          self.total_eleves_label3 = customtkinter.CTkLabel(
              self.tabview.tab("Eleves"),
              text="Nombre total groupe(s) de 2 : " + str(groupe02))
          self.total_eleves_label2.grid(row=4, column=0, padx=20, pady=(0, 10))
          self.total_eleves_label3.grid(row=5, column=0, padx=20, pady=(0, 10))

          for groupe in range(1, int(groupe03) + 1):
            # V√©rifiez si la cl√© existe dans le dictionnaire
            if groupe not in resultats:
              resultats[groupe] = []

            for _ in range(3):
              while True:
                eleve_selec = random.randint(1, final)

                if eleve_selec not in students_assigned:
                  students_assigned.add(eleve_selec)
                  resultats[groupe].append(eleve_selec)
                  break

          for groupe2_index in range(1, int(groupe02) + 1):
            # V√©rifiez si la cl√© existe dans le dictionnaire
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

          self.affichage_result()

        else:
          grpelev = quotient - 1
          groupe02 = reste * 2

          self.total_eleves_label2 = customtkinter.CTkLabel(
              self.tabview.tab("Eleves"),
              text="Nombre total groupe(s) de 3 : " + str(grpelev))
          self.total_eleves_label3 = customtkinter.CTkLabel(
              self.tabview.tab("Eleves"),
              text="Nombre total groupe(s) de 2 : " + str(groupe02))
          self.total_eleves_label2.grid(row=4, column=0, padx=20, pady=(0, 10))
          self.total_eleves_label3.grid(row=5, column=0, padx=20, pady=(0, 10))

          # Cr√©ation d'un cadre d√©roulant
          self.scrollable_frame = customtkinter.CTkScrollableFrame(
              self, label_text="Groupes 03")
          self.scrollable_frame.grid(row=0,
                                     column=1,
                                     padx=(20, 320),
                                     pady=(25, 0),
                                     sticky="nsew")
          self.scrollable_frame.grid_columnconfigure(0, weight=1)
          self.scrollable_frame_switches = []  # R√©initialiser la liste

          # Cr√©ation d'un cadre d√©roulant 02
          self.scrollable_frame02 = customtkinter.CTkScrollableFrame(
              self, label_text="Groupes 02")
          self.scrollable_frame02.grid(row=0,
                                       column=1,
                                       padx=(320, 20),
                                       pady=(25, 0),
                                       sticky="nsew")
          self.scrollable_frame02.grid_columnconfigure(0, weight=1)
          self.scrollable_frame02_switches = []  # R√©initialiser la liste

          for groupe in range(1, int(grpelev) + 1):
            # V√©rifiez si la cl√© existe dans le dictionnaire
            if groupe not in resultats:
              resultats[groupe] = []

            for _ in range(3):
              while True:
                eleve_selec = random.randint(1, final)

                if eleve_selec not in students_assigned:
                  students_assigned.add(eleve_selec)
                  resultats[groupe].append(eleve_selec)
                  break

          for groupe2_index in range(1, int(groupe02) + 1):
            # V√©rifiez si la cl√© existe dans le dictionnaire
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

          #DEBUG

          self.affichage_result()

    # Cr√©ation d'un cadre d√©roulant
    self.scrollable_frame = customtkinter.CTkScrollableFrame(
        self, label_text="Listes des eleves")
    self.scrollable_frame.grid(row=1,
                               column=3,
                               padx=(20, 20),
                               pady=(20, 0),
                               sticky="nsew")
    self.scrollable_frame.grid_columnconfigure(0, weight=1)
    self.scrollable_frame_switches = []  # R√©initialiser la liste
    for i, student in enumerate(list_sep, start=1):
      frame = customtkinter.CTkFrame(master=self.scrollable_frame)
      frame.grid(row=i, column=0, padx=10, pady=(0, 20))
      self.scrollable_frame_switches.append(frame)

      # Ajouter un label √† l'int√©rieur du cadre pour afficher le texte
      label = customtkinter.CTkLabel(master=frame,
                                     text=f" N°{eleves[student]}  {student}")
      label.pack()

  def open_group_window(self, groupe):
    group_number = groupe
    print(f"Ouvrir la fenetre du groupe {group_number}")

    # Fermez la fen√™tre Toplevel existante s'il y en a une
    if self.toplevel_window and self.toplevel_window.winfo_exists():
      self.toplevel_window.destroy()

    self.toplevel_window = ToplevelWindow(self, group_number)

  def open_group_window02(self, groupe2):

    group_number02 = groupe2
    print(f"Ouvrir la fenetre du groupe {group_number02}")

    # Fermez la fen√™tre Toplevel existante s'il y en a une
    if self.toplevel_window02 and self.toplevel_window02.winfo_exists():
      self.toplevel_window02.destroy()

    self.toplevel_window02 = ToplevelWindow02(self, group_number02)
    print(resultats)

  def open_group_window_paires(self):

    print("Ouvrir la fenetre de paires")

    # Fermez la fen√™tre Toplevel existante s'il y en a une
    if self.toplevel_window_paires and self.toplevel_window_paires.winfo_exists(
    ):
      self.toplevel_window_paires.destroy()

    self.toplevel_window_paires = ToplevelWindowPaires(self)



  def create_group(self):
    for widget in self.scrollable_frame.winfo_children():
      widget.destroy()
      print("reset01")

    for widget in self.scrollable_frame02.winfo_children():
      widget.destroy()
      print("reset02")
    self.update_idletasks()

  # Gestionnaire d'√©v√©nement pour le changement du mode d'apparence
  def change_appearance_mode_event(self, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

  # Gestionnaire d'√©v√©nement pour le changement de mise √† l'√©chelle de l'interface utilisateur
  def change_scaling_event(self, new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


# V√©rification si ce fichier est ex√©cut√© en tant que script principal
if __name__ == "__main__":
  app = App()
  app.mainloop()
