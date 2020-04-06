'''from random import randint

numero = randint(1, 10)
adivinha = int(input('Adivinhe que número escolhi, de 1 a 10: '))
vezes = 1
while adivinha != numero:
    adivinha = int(input('Errou, quer tentar de novo? '))
    vezes += 1
print('Parabéns, você acertou!!!')
print('Você precisou de {} tentativas para acertar.'.format(vezes))'''

'''desejo = 1
while desejo != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro: '))
    print('O que você quer fazer com eles?\n'
          '[1] Somar\n'
        '[2] Multiplicar\n'
        '[3] Saber o maior\n'
        '[4] Digitar novos números\n'
        '[5] Sair do programa\n')
    desejo = int(input('>>> '))
    if desejo == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    if desejo == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    if desejo == 3:
        teste = n1-n2
        if teste < 0:
            print('O maior número é {}.'.format(n2))
        else:
            print('O maior número é {}.'.format(n1))
print('Obrigado! Tchau!')'''

'''num1 = int(input('Digite um número: '))
numfat = fat = num1

while numfat > 1:
    fat = fat*(numfat-1)
    numfat -= 1
print('O fatorial de {} é {}.'.format(num1, fat))'''

'''num = int(input('Digite um número: '))
razao = int(input('Qual a razão da PA? '))
cont = 1
print(num)
while cont < 10:
    num += razao
    cont += 1
    print(num)
mais = 1
while mais != 0:
    mais = int(input('Quantos termos mais você quer ver? '))
    for x in range(1, (mais+1)):
        num += razao
        print(num)
print('Fechou!')'''

'''n1 = int(input('Digite um número: '))
n2 = n1
seq = int(input('Quantos elementos você quer ver da Sequência de Fibonacci? '))
if n1 == 0:
    print(n1)
    n1 += 1
else:
    print(n1)
while seq > 0:
    n1 = n1 + n2
    n2 = n1 - n2
    seq -= 1
    print(n1)'''

'''num = int(input('Digite um número: '))
num2 = 0
cont = 0
while num2 != 999:
    num2 = int(input('Digite outro: '))
    num3 = num2
    num += num3
    cont += 1
num -= 999
print('Você digitou {} números e a soma deles resulta em {}.'.format(cont, num))'''

'''n1 = 0
n2 = 0
cont = 0
maior = 0
menor = 0
continuar = ''

while continuar != 'n':
    n1 = int(input('Digite um número: '))
    n2 = n2 + n1
    cont += 1
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    continuar = str(input('Quer continuar? ')).lower().strip()


print('A média dos números que você digitou é {}.'.format(n2/cont))
print('O maior número que você digitou foi {}. O menor foi {}.'.format(maior, menor))'''











