import tkinter as tk
from tkinter import ttk
from kalories_requierement import KaloriesRequierement
from PIL import ImageTk, Image

class GekaloriesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gekalories App')
        self.geometry('400x900')
        self.init_widget()
        self.configure(background="black")

    def init_widget(self):
        vcmd = (self.register(self.validate_number_only))
        self.img = Image.open("gekalories.png")
        width, height = self.img.size
        new_width = 100
        new_height = int((height / width) * new_width)
        self.img = self.img.resize((new_width, new_height))

        self.photo = ImageTk.PhotoImage(self.img)
        self.icon = tk.Label(self, image=self.photo)
        self.icon.pack()

        frame_genre = tk.Frame(self, height=70, width=300)
        frame_genre.configure(background="black")
        label_genre = tk.Label(master=frame_genre, text="Tu es ")
        self.select_genre = ttk.Combobox(frame_genre, values=['un homme', 'une femme'], state='readonly')
        self.select_genre.current(0)
        label_genre.pack()
        self.select_genre.pack()
        frame_genre.pack(pady=20)

        frame_weight = tk.Frame(self, height=70, width=300)
        frame_weight.configure(background="black")
        label_weight = tk.Label(frame_weight, text="Poids (kg)")
        self.input_weight = tk.Entry(frame_weight, validate='key', validatecommand=(vcmd, '%P'))
        label_weight.pack()
        self.input_weight.pack()
        frame_weight.pack(pady=20)

        frame_size = tk.Frame(self, height=70, width=300)
        frame_size.configure(background="black")
        label_size = tk.Label(frame_size, text="Taille (cm)")
        self.input_size = tk.Entry(frame_size, validate='key', validatecommand=(vcmd, '%P'))
        label_size.pack()
        self.input_size.pack()
        frame_size.pack(pady=20)

        frame_age = tk.Frame(self, height=70, width=300)
        frame_age.configure(background="black")
        label_age = tk.Label(frame_age, text="Ton âge")
        self.input_age = tk.Entry(frame_age, validate='key', validatecommand=(vcmd, '%P'))
        label_age.pack()
        self.input_age.pack()
        frame_age.pack(pady=20)

        frame_activity = tk.Frame(self, height=70, width=300)
        frame_activity.configure(background="black")
        label_activity = tk.Label(frame_activity, text="Quel est ton niveau d'activité ?")
        self.select_activity = ttk.Combobox(frame_activity, values=['sédentaire', 'actif', 'modérément actif', 'extremement actif'], state='readonly')
        self.select_activity.current(0)
        label_activity.pack()
        self.select_activity.pack()
        frame_activity.pack(pady=20)

        frame_objective = tk.Frame(self, height=70, width=300)
        frame_objective.configure(background="black")
        label_objective = tk.Label(frame_objective, text="Quel est ton objectif ?")
        self.select_objective = ttk.Combobox(frame_objective, values=['perdre du poids', 'me maintenir', 'prendre du poids'], state='readonly')
        self.select_objective.current(0)
        label_objective.pack()
        self.select_objective.pack()
        frame_objective.pack(pady=20)

        handle_submit = tk.Button(self, text="Calculer", command=self.submit).pack(pady=10)

    def submit(self):
        selected_genre = self.select_genre.get()
        selected_weight = int(self.input_weight.get())
        selected_size = int(self.input_size.get())
        selected_age = int(self.input_age.get())
        selected_activity = self.select_activity.get()
        selected_objective = self.select_objective.get()
        if selected_weight > 10 and selected_size > 100 and selected_age > 15:
            new = KaloriesRequierement(self, selected_genre, selected_weight, selected_size, selected_age, selected_activity, selected_objective)



    def validate_number_only(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False


if __name__ == "__main__":
    app = GekaloriesApp()
    app.mainloop()