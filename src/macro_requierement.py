import tkinter as tk

class MacroRequierement(tk.Frame):
    def __init__(self, parent, final_cal, weight):
        super().__init__(parent)
        self.protein = self.calcul_protein(weight)
        self.lipides = self.calcul_lipides(final_cal)
        self.glucides = self.calcul_glucides(self.protein, self.lipides, final_cal)
        self.init_widget(parent)


    def init_widget(self, parent):
        frame = tk.Frame(parent, width=300, height=200, highlightbackground="black", highlightthickness=1)
        label_protein = tk.Label(frame, text=f"Protéines = {self.protein}g.").pack()
        label_glucides = tk.Label(frame, text=f"Glucides = {self.glucides}g.").pack()
        label_lipides = tk.Label(frame, text=f"Lipides = {self.lipides}g.").pack()
        frame.pack(pady=10, ipady=10, ipadx=10)

    def calcul_protein(self, weight):
        return int(weight*2)

    def calcul_lipides(self, calories):
        pourcent = int(calories*0.30)
        return int(pourcent/9)

    def calcul_glucides(self, protein, lipides, calories):
        protein_cal = protein * 4
        lipides_cal = lipides * 9
        calories_remaining = calories - protein_cal - lipides_cal
        return int(calories_remaining / 4)




