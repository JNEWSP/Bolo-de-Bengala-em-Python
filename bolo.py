import tkinter as tk
from tkinter import messagebox
import threading
import time

class BirthdayCakeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bolo de Aniversário Animado 🎂")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()

        self.candles_on = []
        self.candle_labels = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Digite seu nome:", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.name_var, font=("Arial", 12)).pack(pady=5)

        tk.Label(self.root, text="Quantas velas? (1-20):", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.age_var, font=("Arial", 12)).pack(pady=5)

        self.cake_frame = tk.Frame(self.root)
        self.cake_frame.pack(pady=20)

        self.candle_frame = tk.Frame(self.cake_frame)
        self.candle_frame.pack()

        self.cake_label = tk.Label(self.cake_frame, text=self.get_cake_text([]), font=("Courier", 14), justify="center")
        self.cake_label.pack()

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=10)

        self.light_btn = tk.Button(self.btn_frame, text="Acender Velas", command=self.start_light_candles, state="normal")
        self.light_btn.grid(row=0, column=0, padx=10)

        self.blow_btn = tk.Button(self.btn_frame, text="Apagar Velas", command=self.start_blow_candles, state="disabled")
        self.blow_btn.grid(row=0, column=1, padx=10)

    def get_cake_text(self, candles_on):
        # candles_on: lista de bool
        candles_line = ""
        for on in candles_on:
            candles_line += "i " if on else "  "
        cake = f"""
   {candles_line}
  |:H:a:p:p:y:|
__|___________|__
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~
"""
        return cake

    def start_light_candles(self):
        name = self.name_var.get().strip() or "Amigo"
        try:
            age = int(self.age_var.get())
            if age < 1 or age > 20:
                messagebox.showerror("Erro", "Por favor, escolha um número entre 1 e 20.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido para as velas.")
            return

        self.name = name
        self.age = age
        self.candles_on = [False] * age

        self.light_btn.config(state="disabled")
        self.blow_btn.config(state="disabled")
        threading.Thread(target=self.light_candles_animation).start()

    def light_candles_animation(self):
        for i in range(self.age):
            self.candles_on[i] = True
            self.update_cake()
            time.sleep(0.5)
        self.show_message(f"Parabéns, {self.name}! 🎂")
        self.blow_btn.config(state="normal")

    def start_blow_candles(self):
        self.light_btn.config(state="disabled")
        self.blow_btn.config(state="disabled")
        threading.Thread(target=self.blow_candles_animation).start()

    def blow_candles_animation(self):
        for i in range(self.age):
            self.candles_on[i] = False
            self.update_cake()
            time.sleep(0.5)
        self.show_message(f"Feliz Aniversário, {self.name}! Que todos os seus desejos se realizem! 🎉🎈")
        self.light_btn.config(state="normal")

    def update_cake(self):
        cake_text = self.get_cake_text(self.candles_on)
        self.cake_label.config(text=cake_text)

    def show_message(self, msg):
        messagebox.showinfo("Mensagem", msg)

def main():
    root = tk.Tk()
    app = BirthdayCakeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
