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
        valor = float(input("Digite um valor: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("Transação completa")
        else:
            print("Valor inválido")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite um valor: "))
        if valor > 0:
            if valor <= saldo and numero_saques < limite_saques:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R${valor:.2f}\n"
                print("Transação completa")
            elif valor > saldo:
                print("Saldo insuficiente")
            elif numero_saques >= limite_saques:
                print("Limite diário de saques atingido")
        else:
            print("Valor inválido")

    elif opcao == "e":
        print("Exibir extrato")
        print(extrato if extrato else "Nenhuma transação realizada.")
        print(f"Saques: {numero_saques}")
        print(f"Saldo: R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida")
