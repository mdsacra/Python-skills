'''lista = []
mai = men = 0
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}º número: '))
    lista.append(num)
    if c == 0:
        mai = men = num
    else:
        if num > mai: mai = num
        if num < men: men = num

print(f'O maior número da lista é {mai} e está na(s) posição(ões) ', end='')
for i, c in enumerate(lista):
    if c == mai:
        print(i, end=' ')
print()
print(f'O menor número da lista é {men} e está na(s) posição(ões) ', end='')
for i, c in enumerate(lista):
    if c == men:
        print(i, end=' ')
print()'''

lista = []
seguir = ''
while seguir != 'N':
    num = int(input('Digite um número: '))
    if num in lista:
        print('Este número já existe na lista.')
    else:
        lista.append(num)
        print('Adicionado à lista!')
    seguir = str(input('Quer continuar [S/N]? ')).upper()
    while seguir != 'S' and seguir != 'N':
        seguir = str(input('Digite "S" para continuar ou "N" para encerrar: ')).upper()

print(f'Os valores da sua lista são {lista}.')



