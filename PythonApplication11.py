import random
import tkinter as tk

def loe_kaart():
    return random.randint(2, 11)

def alusta_mängu():
    global player_sum
    player_sum = loe_kaart() + loe_kaart()
    kaardid_label.config(text=f"Sinu summa: {player_sum}")
    tulemus_label.config(text="")

def võta_kaart():
    global player_sum
    player_sum += loe_kaart()
    kaardid_label.config(text=f"Sinu summa: {player_sum}")
    if player_sum > 21:
        tulemus_label.config(text="Kaotasid! Sinu summa ületas 21.")

def peatu():
    arvuti_sum = mängi_arvuti()
    if arvuti_sum > 21 or player_sum > arvuti_sum:
        tulemus_label.config(text=f"Võitsid! Arvuti summa oli {arvuti_sum}.")
    elif player_sum == arvuti_sum:
        tulemus_label.config(text=f"Viik! Arvuti summa oli {arvuti_sum}.")
    else:
        tulemus_label.config(text=f"Kaotasid! Arvuti summa oli {arvuti_sum}.")

def mängi_arvuti():
    summa = 0
    while summa < 17:
        summa += loe_kaart()
    return summa

root = tk.Tk()
root.title("Mäng 21")
root.geometry("400x300")  
root.configure(bg="lightgray")  

frame = tk.Frame(root, bg="lightgray")
frame.pack(expand=True)

kaardid_label = tk.Label(frame, text="", bg="lightgray", font=("Arial", 14))
kaardid_label.pack()

tulemus_label = tk.Label(frame, text="", bg="lightgray", font=("Arial", 14))
tulemus_label.pack()

tk.Button(frame, text="Alusta mängu", command=alusta_mängu).pack()
tk.Button(frame, text="Võta kaart", command=võta_kaart).pack()
tk.Button(frame, text="Peatu", command=peatu).pack()

root.mainloop()