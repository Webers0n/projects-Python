import tkinter as tk
from tkinter import Button,messagebox,Label,Entry



janela_principal = tk.Tk()
janela_principal.title ("CALCULO DE ENERGIA")
janela_principal.geometry ("400x250")
janela_principal.configure(bg="#4682B4" )

titulo =Label(janela_principal, text="CALCULO DE CONSUMO " , font=("Arial",18), bg="#4682B4")
titulo.grid(row=0 , column=0 , padx=10, pady=10 , columnspan=4)


#funções

def calcular ():
    try:
        consumo = float(consumo_Entry.get())
        taxa = float(taxa_entry.get())
        soma = consumo * taxa
        messagebox.showinfo("Resultado", f"O Valor total é: R$ {soma:.2f}")
    except ValueError:
        messagebox.showwarning("Entrada Inválida!" , "Por favor, Insirir valores Númericos válidos!!")


## CONSUMO

consumo_kwh = Label(janela_principal, text="Consumo(KWH): ", font=("Arial" , 16) , bg="#4682B4")
consumo_kwh.grid(row=1 , column=0, padx=10, pady=10)

consumo_Entry = Entry(janela_principal , width=20)
consumo_Entry.grid(row=1, column=1, padx=10, pady=10)



## TAXAS 

taxa = Label(janela_principal, text="Taxa de Consumo: " , font=("Arial", 16), bg="#4682B4")
taxa.grid(row=2 , column=0, padx=10, pady=10)

taxa_entry = Entry(janela_principal, width=20)
taxa_entry.grid(row=2 , column=1, padx=10, pady=10)

## BOTOES

calcular = Button(janela_principal, text="Calcular" , font=("Arial" , 16), command=calcular , width="8",height="1", bg="#5F9EA0")
calcular.grid(row=3 , column=0, padx=10, pady=10,columnspan=1)

sair = Button(janela_principal, text="Sair" , font=("Arial" , 16, ), width="8", height="1", command=janela_principal.destroy, bg="#5F9EA0")
sair.grid(row=3 , column=1, padx=10, pady=10, columnspan=2)





janela_principal.mainloop()