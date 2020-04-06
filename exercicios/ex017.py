'''valores = []
mai = 0
men = 0
for n in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if n == 0:
        mai = men = valores[n]
    else:
        if valores[n] > mai:
            mai = valores[n]
        if valores[n] < men:
            men = valores[n]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} e ele aparece nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}', end='...')
print()
print(f'O menor valor digitado foi {men} e ele aparece nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}', end='...')
print()'''

'''listanum = []
continuar = ''.upper()
while continuar != 'N':
    num = (int(input('Digite um número: ')))
    if num in listanum:
        print('Este valor já existe na lista e não pode ser adicionado.')
    else:
        listanum.append(num)
    continuar = input('Quer continuar [S/N]? ').upper()
print(f'Os valores que você acrescentou foram {sorted(listanum)}')'''

listanum = []
for c in range(0, 5):
    num = int(input(f'Digite o {c+1}° número: '))
    if c == 0 or num > listanum[-1]:
        listanum.append(num)
        print(f'Adicionado ao último índice.')
    else:
        pos = 0
        while pos < len(listanum):
            if num <= listanum[pos]:
                listanum.insert(pos, num)
                print(f'Adicionado ao índice {pos}.')
                break
            pos += 1
print(listanum)




