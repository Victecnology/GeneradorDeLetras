import tkinter as tk
import random

def generate_letter():
  letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  letter = random.choice(letters)
  label.config(text=letter)

root = tk.Tk()
root.title("Generador de letras")

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Generar", command=generate_letter)
button.pack()

root.mainloop()