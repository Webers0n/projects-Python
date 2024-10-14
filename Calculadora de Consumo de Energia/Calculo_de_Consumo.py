## Import


## funções


## INICIO


##Contantes
RESIDENCIAL_ABAIXO_DE_500 = 0.40
RESIDENCIAL_ACIMA_DE_500 = 0.65

COMERCIAL_ABAIXO_1000 = 0.55
COMERCIAL_ACIMA_1000 = 0.60

INDUSTRIAL_ABAIXO_5000 = 0.55
INDUSTRIAL_ACIMA_5000 = 0.55



consumo_em_kwh = float(input("Total (kWh) : "))
tipo_intalação = input("Tipo de Instalação: R (Instalação) / C (Comercial) / I (Industrail): ")

if (tipo_intalação == "r") or (tipo_intalação == "R"): 
    if (consumo_em_kwh > RESIDENCIAL_ABAIXO_DE_500):
        valor = consumo_em_kwh * RESIDENCIAL_ABAIXO_DE_500
        print(f"Valor a Pagar: %.2f" % valor)
    else: 
        valor = consumo_em_kwh * RESIDENCIAL_ACIMA_DE_500
        print(f"Valor a Pagar: %.2f" % valor)
elif (tipo_intalação == "c") or (tipo_intalação == "C"):
    if (consumo_em_kwh > COMERCIAL_ABAIXO_1000):
        valor = consumo_em_kwh * COMERCIAL_ABAIXO_1000
        print(f"Valor a Pagar: %.2f" % valor)

    else : 
        valor = consumo_em_kwh * COMERCIAL_ACIMA_1000
        print("Valor a Pagar: " , valor)

elif (tipo_intalação == "i") or (tipo_intalação == "I"):
    if consumo_em_kwh > INDUSTRIAL_ABAIXO_5000:
        valor = consumo_em_kwh * INDUSTRIAL_ABAIXO_5000
        print(f"Valor a Pagar: %.2f" % valor)

    else:
        valor = consumo_em_kwh * INDUSTRIAL_ACIMA_5000
        print(f"Valor a Pagar: %.2f" % valor)

else:
    print("DIGITE UMA CATEGORIA VALIDA!!!")
