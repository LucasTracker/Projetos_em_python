import customtkinter
import tkinter
from GeradorDeCpf import main
from pyperclip import copy,paste

# ativa o modo Dark
customtkinter.set_appearance_mode("dark") 

def button_callback():
    entryValue.set(main(radio_var.get()))

def button_copy():
    texto = str(entryValue.get())
    copy(texto)



# Debug Function
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

app = customtkinter.CTk()
app.title("Gerador de CPFs")
app.geometry("400x500")
app.grid_columnconfigure(0, weight=1)

# Labels
label = customtkinter.CTkLabel(app, text="Escolha uma Opção abaixo: ").grid(row=0, column=0, sticky="WE")

# Radio Buttons
radio_var = tkinter.IntVar(value=0)
radiobutton_0 = customtkinter.CTkRadioButton(master=app, text="RS",variable= radio_var, value=0).grid(row=1,column=0, padx=5, pady=5, sticky="w")
radiobutton_1 = customtkinter.CTkRadioButton(master=app, text="DF GO MS MT TO",variable= radio_var, value=1).grid(row=2,column=0, padx=5, pady=5, sticky="w")
radiobutton_2 = customtkinter.CTkRadioButton(master=app, text="AC AM AP PA RO RR", variable= radio_var, value=2).grid(row=3,column=0, padx=5, pady=5, sticky="w")
radiobutton_3 = customtkinter.CTkRadioButton(master=app, text="CE MA PI",variable= radio_var, value=3).grid(row=4,column=0, padx=5, pady=5, sticky="w")
radiobutton_4 = customtkinter.CTkRadioButton(master=app, text="AL PB PE RN", command= radiobutton_event,variable= radio_var, value=4).grid(row=5,column=0, padx=5, pady=5, sticky="w")
radiobutton_5 = customtkinter.CTkRadioButton(master=app, text="BA SE",variable= radio_var, value=5).grid(row=6,column=0, padx=5, pady=5, sticky="w")
radiobutton_6 = customtkinter.CTkRadioButton(master=app, text="MG",variable= radio_var, value=6).grid(row=7,column=0, padx=5, pady=5, sticky="w")
radiobutton_7 = customtkinter.CTkRadioButton(master=app, text="ES RJ",variable= radio_var, value=7).grid(row=8,column=0, padx=5, pady=5, sticky="w")
radiobutton_8 = customtkinter.CTkRadioButton(master=app, text="SP",variable= radio_var, value=8).grid(row=9,column=0, padx=5, pady=5, sticky="w")
radiobutton_8 = customtkinter.CTkRadioButton(master=app, text="PR SC",variable= radio_var, value=9).grid(row=10,column=0, padx=5, pady=5, sticky="w")

# Entry
entryValue = tkinter.StringVar()
entry = customtkinter.CTkEntry(app, textvariable=entryValue, state="disabled", width=250).grid(row = 12, column=0, padx=5, pady=20, sticky="w")

#button
button = customtkinter.CTkButton(app, text= "Gerar CPF", command=button_callback).grid(row = 11, column=0, padx=5, pady=20, sticky="ew")
button = customtkinter.CTkButton(app, text= "Copiar", command=button_copy , width=138).grid(row = 12, column=0, padx=5, pady=20, sticky="e")

app.mainloop()