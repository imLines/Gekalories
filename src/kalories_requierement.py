import tkinter as tk
from macro_requierement import MacroRequierement

class KaloriesRequierement(tk.Toplevel):
    def __init__(self, parent, genre, weight, size, age, activity, objective):
        super().__init__(parent)
        self.title('Gekalories - Mon besoin calorique')
        self.geometry('600x500')
        self.genre = genre
        self.weight = weight
        self.size = size
        self.age = age
        self.activity = activity
        self.objective = objective
        self.init_widget()

    def init_widget(self):
        frame_init = tk.Frame(self, height=50, width=300)
        label_genre = tk.Label(frame_init, text=f'Genre : {self.genre}').pack()
        label_weight = tk.Label(frame_init, text=f'Poids : {self.weight}Kg').pack()
        label_size = tk.Label(frame_init, text=f'Taille : {self.size}cm').pack()
        label_age = tk.Label(frame_init, text=f'Age : {self.age}ans').pack()
        label_activity = tk.Label(frame_init, text=f'Activité : {self.activity}').pack()
        label_objective = tk.Label(frame_init, text=f'Objectif : {self.objective}').pack()
        frame_init.pack(pady=20)

        self.bmr = self.calcul_bmr()
        self.ttde = self.calcul_ttde()
        self.final_cal = self.calcul_final_cal()

        frame_info = tk.Frame(self, height=10, width=300)
        label_bmr = tk.Label(frame_info, text=f'Ton corps à besoin de {self.bmr}kcal pour fonctionner.').pack()
        label_ttde = tk.Label(frame_info, text=f"Ton niveau d'activité est {self.activity}, ton besoin calorique est {self.ttde}kcal").pack()
        label_final_cal = tk.Label(frame_info, text=f"Pour parvenir à tes objectifs, tu dois consommer {self.final_cal}kcal.")
        frame_info.pack()
        new = MacroRequierement(self, self.final_cal, self.weight)

    def calcul_ttde(self):
        if self.activity == 'sédentaire':
            ttde = self.bmr*1.55
            return int(ttde)
        elif self.activity == 'actif':
            ttde = self.bmr * 1.85
            return int(ttde)
        elif self.activity == 'modérément actif':
            ttde = self.bmr * 2.2
            return int(ttde)
        elif self.activity == 'extremement actif':
            ttde = self.bmr * 2.4
            return int(ttde)


    def calcul_bmr(self):
        if self.genre == 'un homme':
            first = 10 * self.weight
            second = 6.25 * self.size
            third = 5 * self.age
            bmr = first+second-third+5
            return int(bmr)
        elif self.genre == 'une femme':
            first = 10 * self.weight
            second = 6.25 * self.size
            third = 5 * self.age
            bmr = first+second-third-161
            return int(bmr)

    def calcul_final_cal(self):
        if self.objective == 'perdre du poids':
            final_cal = self.ttde-500
            return final_cal
        elif self.objective == 'me maintenir':
            final_cal = self.ttde
            return final_cal
        elif self.objective == 'prendre du poids':
            final_cal = self.ttde + 500
            return  final_cal

