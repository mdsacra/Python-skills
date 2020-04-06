from random import randint

numero = randint(1, 10)
adivinha = int(input('Adivinhe que número escolhi, de 1 a 10: '))
vezes = 1
while adivinha != numero:
    adivinha = int(input('Errou, quer tentar de novo? '))
    vezes += 1
print('Parabéns, você acertou!!!')
print('Você precisou de {} tentativas para acertar.'.format(vezes))



'''vel = float(input('A que velocidade você passou? '))
if vel > 80:
    print('Você passou acima da velocidade permitida')
    input('Calculando o valor da multa...Tecle algo...')
    multa = (vel-80)*7
    print('O valor da sua multa será de R$ {:.2f}.'.format(multa))
else:
    print('UFA!!! Você escapou!')'''


'''num = int(input('Digite um número: '))
numpar = num%2
if numpar == 0:
    print('Você escolheu o número {} e ele é PAR.'.format(num))
else:
    print('Você escolheu o número {} e ele é IMPAR.'.format(num))'''

'''dist = int(input('Qual a distância da sua viagem? '))
print(dist,'KM')
if dist <= 200:
    valor1 = dist * 0.5
    print('O valor da sua passagem é de R$ {:.2f}.'.format(valor1))
else:
    valor2 = dist * 0.45
    print('O valor da sua passagem é de R$ {:.2f}.'.format(valor2))'''

'''ano = int(input('Digite um ano: '))
biss = ano%4
if biss == 0:
    print('Este ano é bissexto!')
else:
    print('Este ano não é bissexto!')'''

'''n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
n3 = int(input('3° Número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor é {}.'.format(menor))
print('O maior valor é {}.'.format(maior))'''

'''salario = float(input('Qual o salário? '))
if salario > 1250:
    novosal = salario+(salario*0.1)
    print('O novo salário é de R$', novosal)
else:
    novopsal = salario+(salario*0.15)
    print('O novo salário é de R$', novopsal)'''

'''a = int(input('Lado 1: '))
b = int(input('Lado 2: '))
c = int(input('Lado 3: '))
if (a-b)<c and c<(a+b) and (a-c)<b and b<(a+c) and (b-c)<a and a<(b+c):
    print('Estas medidas podem formar um triângulo.')
else:
    print('Estas medidas não podem formar um triângulo.')'''






