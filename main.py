import tkinter as tk
from tkinter import ttk

class CalculetteMatricielle(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Calculette Matricielle")

        self.current_var = tk.StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.current_var)
        self.combobox['values'] = ('2', '3', '4', '5')
        self.combobox.set("choisissez une taille")
        self.combobox.pack(pady=20)

        self.frame_matrice = tk.Frame(self)
        self.frame_matrice.pack()

        self.combobox.bind("<<ComboboxSelected>>", self.afficher_matrice)

    def afficher_matrice(self, event):
        
        try:
            taille = int(self.current_var.get())
        except ValueError:
            return

        
        frame_A = tk.LabelFrame(self.frame_matrice, text="Matrice A")
        frame_A.grid(row=0, column=0, padx=10, pady=10)

        self.entries_A = []  
        for i in range(taille):
            row = []
            for j in range(taille):
                entry = tk.Entry(frame_A, width=5, justify="center")
                entry.grid(row=i, column=j, padx=3, pady=3)
                row.append(entry)
            self.entries_A.append(row)

    
        frame_B = tk.LabelFrame(self.frame_matrice, text="Matrice B")
        frame_B.grid(row=0, column=1, padx=10, pady=10)

        self.entries_B = [] 
        for i in range(taille):
            row = []
            for j in range(taille):
                entry = tk.Entry(frame_B, width=5, justify="center")
                entry.grid(row=i, column=j, padx=3, pady=3)
                row.append(entry)
            self.entries_B.append(row)
        


if __name__ == "__main__":
    app = CalculetteMatricielle()
    app.mainloop()
