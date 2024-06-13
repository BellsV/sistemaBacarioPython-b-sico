saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("Digite uma opção: \n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair")
    opcao = input().lower()
    
    if opcao == "d":
        print("Digite o valor a depositar: ")
        deposito = int(input())
        saldo += deposito
        print(f"Valor de {deposito} depositado com sucesso! Saldo de {saldo}")
        
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
            continue
        
        print("Digite o valor a sacar: ")
        saque = int(input())
        
        if saque > limite:
            print("Você pode fazer um saque de até R$500,00 por vez.")
            continue
        
        if saldo >= saque:
            saldo -= saque
            numero_saques += 1
            print(f"O valor de {saque} foi sacado, seu saldo atual é de {saldo}.")
            print(f"Você pode realizar mais {LIMITE_SAQUES - numero_saques} saques hoje.")
        else:
            print("Saldo insuficiente para saque.")
    elif opcao == "e":
        print(f"Seu extrato é de {saldo}")
        
    elif opcao == "q":
        print("Saindo do sistema...")
        break