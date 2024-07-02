menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = int(input("Digite um valor: "))
        valor += saldo
        print("Transdação completa")

    elif opcao == "s":
        print("Sacar")
        valor = int(input("Digite um valor: "))
        while valor <= saldo:
            saldo = saldo-valor
            numero_saques+1
            print("Transação completa")

        else:
            print("Saldo insuficiente")
            break
        if numero_saques > limite_saques:
            print("imite diario atingido")
            break

    elif opcao == "e":
        print("Exibir extrato")
        print("Saques: " + numero_saques)
        print("Saldo: " + saldo)
    elif opcao == "q":
        break
    else:
        print("Operação inválida")
        break
