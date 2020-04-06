'''s = 0
for c in range(3, 501, 3):
    if c % 2 == 0:
        c = c*0
    s += c
print('A soma de todos é {}.'.format(s))'''

'''soma = 0
cont = 0
for c in range(0,6):
    num = int(input('Digite o {}° número: '.format(c+1)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números PARES e a soma deles é {}.'.format(cont, soma))'''

'''num = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão da PA: '))

print(num)
for c in range(0, 9):
    num = num+razao
    print(num)'''

'''cont = 0
num = int(input('Número: '))

for c in range(1, 10):
    div = num / c
    primo = num % c
    print('{} : {} = {:.2f}. Resto: {}.'.format(num, c, div, primo))
    if primo == 0:
        cont += 1
if cont > 2:
    print('Este número não é primo.')
else:
    print('Este número é primo.')'''


'''frase = str(input('Digite a frase: ')).lower().strip().split()
junto = ''.join(frase)
tamfrase = len(junto)
inverso = ''
for letra in range(tamfrase - 1, -1, -1):
    inverso = inverso+junto[letra]
if junto == inverso:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')'''

'''from datetime import date
atual = date.today().year
cont = 0
for pessoa in range(1, 8):
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa)))
    if atual-nasc > 18:
        cont += 1
print('{} pessoas são maiores de 18.'.format(cont))'''

'''maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg.'.format(maior))
print('O menor peso é {}Kg.'.format(menor))'''

'''somaid = 0
velho = 0
nomevelho = ''
nova = 0
for p in range(1, 5):
    print('{}ª PESSOA'.format(p))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [m/f]: ').lower()
    while sexo != 'm' and sexo != 'f':
        sexo = input('Digite apenas "M" para masculino e "F" para feminino: ')
    somaid += idade
    if sexo == 'm':
        if p == 1:
            velho = idade
            nomevelho = nome
        else:
            if idade > velho:
                velho = idade
                nomevelho = nome
    if sexo == 'f':
        if idade < 20:
            nova += 1

print('A média de idade do grupo é de {} anos.'.format(somaid/p))
print('O homem mais velho se chama {} e possui {} anos.'.format(nomevelho, velho))
if nova == 1:
    print('O grupo possui {} mulher com menos de 20 anos.'.format(nova))
else:
    print('O grupo possui {} mulheres com menos de 20 anos.'.format(nova))'''















