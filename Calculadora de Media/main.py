situacao = dict()
dados = list()

while True:
    o = int(input('CALCULAR NOTAS? [ 1 - INICIAR | 0 - ENCERRAR ]: '))

    if o == 1 :
        situacao['nome'] = str(input("Nome: "))
        situacao['nota'] = int(input("Nota: "))
        dados.append(situacao.copy())
        
    elif o == 0:
        print("\nINFORMAÇÕES")
        for i in dados:
            # Determina a situação do aluno
            if i['nota'] >= 60:
                i['info'] = "Aprovado"
            else:
                i['info'] = "Reprovado"
                
            # Imprime as informações do aluno
            print(f"Aluno(a)= {i['nome']} | Nota= {i['nota']} | Status= {i['info']}")
        
        break
        
