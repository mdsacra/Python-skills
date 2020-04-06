cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
saque = int(input('Quanto você quer sacar? R$ '))
if saque % 2 != 0 and saque % 5 != 0:
    saque = int(input('Apenas notas de 2, 5, 10, 20 e 50. Tente novamente: R$ '))
if saque > 1500:
    saque = int(input('Saque máximo de R$ 1.000,00. Tente novamente: R$ '))
while saque >= 50:
    saque = saque - 50
    cont50 += 1
    if cont50 > 15:
        break
while saque >= 20:
    saque = saque - 20
    cont20 += 1
    if cont20 > 15:
        break
while saque >= 10:
    saque = saque - 10
    cont10 += 1
    if cont10 > 15:
        break
while saque >= 5:
    if saque % 5 == 0:
        saque = saque - 5
        cont5 += 1
        if cont5 > 15:
            break
    else:
        break
while saque >= 2:
    saque = saque - 2
    cont2 += 1
    if cont2 > 15:
        saque = -1
        break
if saque >= 0:
    print(f'{cont50} notas de 50.')
    if cont20 > 0:
        print(f'{cont20} notas de 20.')
    if cont10 > 0:
        print(f'{cont10} notas de 10.')
    if cont5 > 0:
        print(f'{cont5} notas de 5.')
    if cont2 > 0:
        print(f'{cont2} notas de 2.')
else:
    print('Saque Indisponível. Inicie novamente o processo.')




