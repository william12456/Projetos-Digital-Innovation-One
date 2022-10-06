menu = """

[d] depósito
[e] extrato
[s] saque
[q] quit

"""

numero_saque = 0
SAQUE_DIA = 3
LIMITE_SAQUE = 500
saldo = 0
saldo_deposito = 0
saldo_saque = 0

while True:
    opcao = input()
    if opcao == 'd':
        print('Depósito')
        saldo_deposito = float(input())
        saldo+=saldo_deposito
    
    elif opcao == 'e':
        print('Extrato')
        print(f'{saldo:.2f}')
        
    elif opcao == 's':
        print('Saque')
        if numero_saque < SAQUE_DIA:
            saldo_saque = float(input())
            if saldo_saque <= LIMITE_SAQUE:
                if saldo_saque <= saldo:
                    saldo-=saldo_saque
                    numero_saque+=1
                else:
                    print('Você não tem limite')
            else:
                print(f'O limite máximo de saque é {LIMITE_SAQUE:.2f}')
        else:
            print(f'Só pode {SAQUE_DIA} saques por dia')
        
    elif opcao == 'q':
        break