# Código sem funções (def) usando while para selecionar a atividade

while True:
    print("\nMenu de Atividades:")
    print("1 - Imprimir numeros de 1 a 10")
    print("2 - Calcular soma de 1 a 100")
    print("3 - Exibir tabuada de um numero")
    print("4 - Imprimir numeros pares de 1 a 50")
    print("5 - Calcular fatorial")
    print("6 - Contagem regressiva de 10 a 1")
    print("7 - Pesquisa salarial")
    
    opcao = input("escolha uma atividade 0 a 7: ")
    
    if opcao == '1':
        print("\natividade 1: numeros de 1 a 10")
        for i in range(1, 11):
            print(i, end=' ')
        print()
    
    elif opcao == '2':
        print("\natividade 2: Soma de 1 a 100")
        soma = 0
        i = 1
        while i <= 100:
            soma += i
            i += 1
        print(f"a soma é: {soma}")
    
    elif opcao == '3':
        print("\natividade 3: tabuada usando for")
        num = int(input("digite um número para ver sua tabuada: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    
    elif opcao == '4':
        print("\nAtividade 4: Números pares de 1 a 50 usando for")
        for i in range(2, 51, 2):
            print(i, end=' ')
        print()
    
    elif opcao == '5':
        print("\nAtividade 5: Fatorial usando while")
        num = int(input("Digite um número para calcular seu fatorial: "))
        fatorial = 1
        i = num
        while i > 0:
            fatorial *= i
            i -= 1
        print(f"Fatorial de {num}: {fatorial}")
    
    elif opcao == '6':
        print("\nAtividade 6: Contagem regressiva usando while")
        i = 10
        while i > 0:
            print(i)
            i -= 1
        print("Fogo!")
    
    elif opcao == '7':
        print("\nAtividade 7: Pesquisa salarial")
        salarios = []
        filhos = []
        
        while True:
            salario = float(input("Digite o salário (negativo para encerrar): "))
            if salario < 0:
                break
            num_filhos = int(input("Digite o número de filhos: "))
            salarios.append(salario)
            filhos.append(num_filhos)
        
        if salarios:
            # a) Média do salário
            media_salario = sum(salarios) / len(salarios)
            # b) Média de filhos
            media_filhos = sum(filhos) / len(filhos)
            # c) Maior salário
            maior_salario = max(salarios)
            # d) Percentual com salário até R$100
            ate_100 = len([s for s in salarios if s <= 100])
            percentual = (ate_100 / len(salarios)) * 100
            
            print(f"\na) Média salarial: R${media_salario:.2f}")
            print(f"b) Média de filhos: {media_filhos:.1f}")
            print(f"c) Maior salário: R${maior_salario:.2f}")
            print(f"d) Percentual com salário até R$100: {percentual:.2f}%")
        else:
            print("Nenhum dado foi inserido.")
    
    else:
        print("Opção inválida. Tente novamente.")
