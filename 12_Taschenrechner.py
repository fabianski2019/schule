import tkinter as tk
import math

#-------------------------------------buttons-Funktionen----------------------------------------------------------

def button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))


def clear_entry():
    entry.delete(0, tk.END)

#-----------------------------------sonderfunktionen------------------------------------------------------------------

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def delete_last():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])


def double_clear():
    entry.delete(0, tk.END)

#----------------------------------------GUI----------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Taschenrechner")

entry = tk.Entry(root, width=20, font=('Arial', 14), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#--------------------------------buttons-----------------------------------------------------------------------------------------------

buttons = [
    'C', 'del', 'sqrt', '=',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '+/-', '0', '.', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button in ('sqrt', 'del', 'C'):
        tk.Button(root, text=button, padx=20, pady=20, font=('Times New Roman', 12),
                  command=lambda
                      b=button: square_root() if b == 'sqrt' else delete_last() if b == 'del' else double_clear()).grid(
            row=row_val, column=col_val, sticky='nsew')
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12),
                  command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val,
                                                                                              column=col_val,
                                                                                              sticky='nsew')

#-------------------------------------------------------------------------------------------------------------------------------

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
