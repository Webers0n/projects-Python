import tkinter as tk


radar = tk.Tk()
radar.title("CALCULO DO RADAR")
radar.geometry("400x300")


label1 = tk.Label(radar, text="Velocidade da Via: ").place(x=10 , y= 30)
label2 = tk.Label(radar, text="Velocidade do Veiculo: ").place(x=10 , y=60)


via = tk.Entry(radar)
via.place(x = 150 , y=30)
veiculo = tk.Entry(radar)
veiculo.place(x= 150, y=60)

# Rótulos para exibir os resultados (inicialmente vazios)
multa_label = tk.Label(radar, text="", font=("Arial", 14))
multa_label.place(x=30, y=100)

valor_multa_label = tk.Label(radar, text="", font=("Arial", 14))
valor_multa_label.place(x=30, y=130)

aviso_label = tk.Label(radar, text="", font=("Arial", 14))
aviso_label.place(x=10, y=100)

# Função para calcular a multa
def calcular():
    # Limpa os rótulos antes de calcular
    multa_label.config(text="")
    valor_multa_label.config(text="")
    aviso_label.config(text="")
    
    try:
        velocidade_via = int(via.get())
        velocidade_veiculo = int(veiculo.get())

        if velocidade_veiculo > velocidade_via:
            mult = velocidade_veiculo - velocidade_via
            taxa = 3.14
            multa_valor = mult * taxa
            
            # Atualiza o texto dos rótulos
            multa_label.config(text="VEÍCULO MULTADO!!!")
            valor_multa_label.config(text=f"Valor da multa: R$ {multa_valor:.2f}")

        else:
            aviso_label.config(text="Veículo dentro da velocidade permitida!!!")

    except ValueError:
        multa_label.config(text="Por favor, insira valores numéricos válidos.")
        valor_multa_label.config(text="")



botao = tk.Button(radar, text= "Calcular", command=calcular ).place(x= 50 , y= 180   , height = 30 , width = 100)
encerrar = tk.Button(radar,text="Sair", command=radar.destroy).place(x=170 , y=180, height = 30 , width = 100)



radar.mainloop()