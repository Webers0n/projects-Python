
"""
Informações das variaveis

veloc_via: Solicita a velocidade  da pista
veiculo : Solicita a velocidade que o veiculo estar

Contant = 3.14

"""

#INICIO



while True:

    veloc_via = int(input("Velocidade da Via: "))
    veiculo = int(input("Velocidade: "))

    if veiculo > veloc_via:
        
        mult = veiculo - veloc_via
        taxa = 3.14

        Multa = mult * taxa
        print("Veiculo Multado!")
        print(f"Valor da multa: R$ {Multa:.2f}")

    else: print("Veiculo Dentro da Via!! ")

    continuar = input("Deseja continuar ? (S / N )")

    if(continuar == 'n') or (continuar == 'N'):
        print("Programa Encerrado!!")
        break




#FIM