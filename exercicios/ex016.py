'''tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 a 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Número de 0 a 20: '))
print(tupla[n])'''

'''cb = ('fla', 'san', 'pal', 'gre', 'cap', 'spo', 'cor', 'int', 'for', 'goi', 'bah', 'vas', 'cam', 'flu', 'bot', 'cea',
      'cru', 'csa', 'cha', 'ava')
print(cb[:6])
print(cb[-4:])
print(sorted(cb))
print('A posição da Chapecoense é {}º'.format(cb.index('cha')+1))'''

'''from random import randint

m = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
ms = sorted(m)
print(f'Os números sorteados foram {m[0]}, {m[1]}, {m[2]}, {m[3]}, {m[4]}, {m[5]}')
print(f'O menor número sorteado é {ms[0]}.\nO maior número sorteado é {ms[-1]}.')'''

'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tupla = (n1, n2, n3, n4)
v9 = tupla.count(9)
if v9 == 0:
    print('Nenhum valor 9 foi digitado.')
else:
    print(f'O 9 foi digitado {v9} vezes.')
v3 = tupla.count(3)
if v3 == 0:
    print('Nenhum valor 3 foi digitado.')
else:
    v3 = tupla.index(3)
    print(f'O 3 foi digitado na posição {v3+1}.')

print('Os valor pares digitados foram', end=' ')
for p in tupla:
    if p % 2 == 0:
        print(p, end=' ')'''

'''lista = ('mesa', 249.90, 'porta', 89.90, 'cadeira', 65.90, 'balcão', 99.90, 'marreta', 24.90, 'biscuit', 5.90, 'arrumadeira', 129.90)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for p in range(0, len(lista)):
    if p % 2 == 0:
        print(f'{lista[p]:.<30}'.upper(), end='')
    else:
        print(f'R${lista[p]:>7.2f}')
print('-'*40)'''

'''palavras = ('cachorro', 'gato', 'galinha', 'marreco', 'bizão', 'hiena', 'zebra', 'zebu')
for p in palavras:
    print(f'\nA palavra {p.upper()} possui as vogais ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')'''














