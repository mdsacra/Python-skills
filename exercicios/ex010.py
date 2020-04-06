'''valor = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos você quer pagar? '))

parcela = (valor/tempo)/12
print('A parcela do imóvel terá o valor de R${:.2f}'.format(parcela))
if parcela > salario*0.3:
    print('Infelizmente o seu salário não é suficiente para comprar esta casa em {} anos.'.format(tempo))'''

'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Os dois valores são iguais!')'''

'''idade = int(input('Digite o seu ano de nascimento: '))
if idade > 18:
    idade = idade-18
    print('Você já passou a {} anos da idade do alistamento militar.'.format(idade))
elif idade == 18:
    print('Está na hora de você se alistar no exército.')
else:
    idade = 18-idade
    print('Faltam {} anos para seu alistamento militar.'.format(idade))'''

'''n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
n3 = float(input('3ª nota: '))
n4 = float(input('4ª nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5:
    print('Sua média é {}, você foi \33[1;31mREPROVADO\33[m!!!'.format(media))
elif 5 < media < 7:
    print('Sua média é {}, você está em \33[1;32mRECUPERAÇÃO\33[m!!!'.format(media))
else:
    print('Sua média é {}, você foi \33[1;36mAPROVADO\33[m!!!'.format(media))'''

'''ano = int(input('Digite o ano de nascimento do atleta para saber sua categoria: '))
if 2020 - ano <= 9:
    print('MIRIM')
elif 9 < 2020 - ano < 14:
    print('INFANTIL')
elif 14 < 2020 - ano < 17:
    print('JUNIOR')
elif 17 < 2020 - ano < 20:
    print('SEMIPRO')
elif 20 < 2020 - ano < 30:
    print('PRO')
else:
    print('MASTER')'''

'''l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Estas linhas não formam um triângulo.')
else:
    if l1 == l2 == l3:
        print('Estas linhas formam um triângulo EQUILÁTERO!')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Estas linhas formam um triângulo ISÓSCELES!')
    elif l1 != l2 != l3:
        print('Estas linhas formam um triângulo ESCALENO!')'''

'''peso = float(input('Digite seu peso em kg: '))
altura = int(input('Digite sua altura em cm: '))
altura = altura/100
imc = peso/altura**2

if imc < 18.5:
    print('Seu IMC é \33[1m{:.2f}\33[m'.format(imc))
    print('Você está \33[4mabaixo do peso\33[m!')
elif 18.5 <= imc < 25:
    print('Seu IMC é \33[1m{:.2f}\33[m'.format(imc))
    print('Seu peso é o \33[4mideal\33[m!')
elif 25 <= imc < 30:
    print('Seu IMC é \33[1m{:.2f}\33[m'.format(imc))
    print('Você está com \33[4msobrepeso\33[m!')
elif 30 <= imc < 40:
    print('Seu IMC é \33[1m{:.2f}\33[m'.format(imc))
    print('Você está \33[4mobeso\33[m!')
else:
    print('Seu IMC é \33[1m{:.2f}\33[m'.format(imc))
    print('Você está com \33[1mOBESIDADE MÓRBIDA\33[m!')'''


'''valor = float(input('Qual o valor do produto? '))
pgto = int(input('Escolha a forma de pagamento \n'
                 '1) À vista no dinheiro (10% de desconto) \n'
                 '2) À vista no Cartão de Crédito \n'
                 '3) Em 2x no Cartão de Crédito (1,5% de acréscimo na parcela) \n'
                 '4) 3x ou mais no cartão (5% de acréscimo no total) \n'
                 '>>> '))
print('Valor total:')
if pgto == 1:
    valor = valor-(valor*0.1)
    print('R$ {:.2f}'.format(valor))
elif pgto == 2:
    print('R$ {:.2f}'.format(valor))
elif pgto == 3:
    valor = valor+(((valor/2)*0.015)*2)
    print('R$ {:.2f}'.format(valor))
elif pgto == 4:
    valor = valor + (valor * 0.05)
    print('R$ {:.2f}'.format(valor))

contador = 0
while contador < 100:
    confirma = input('Deseja confirmar a forma de pagamento? (S ou N) ').upper()
    if confirma == 'S':
        print('Obrigado! Você acaba de realizar a compra no valor total de R$ {:.2f}.'.format(valor))
        input('Pressione qualquer tecla para encerrar.')
        break
    elif confirma == 'N':
        print('Você cancelou sua compra! Até mais tarde!')
        input('Pressione qualquer tecla para encerrar.')
        break
    else:
        print('Digite apenas "S", para \33[1;36mSIM\33[m, ou "N", para \33[1;31mNÃO\33[m!')
        contador = contador + 1'''

print('='*20, 'JOKEN-PÔ', '='*20)
print('='*50)
from random import randint
contador = 0

while contador < 100:
    jokpc = randint(1,3)

    print(' Escolha seu instrumento: \n (1) Pedra (2) Papel (3) Tesoura')
    jokusu = int(input('>>> '))

    if jokusu == 1:
        print('VOCÊ: \33[1mPedra\33[m')
    elif jokusu == 2:
        print('VOCÊ: \33[1mPapel\33[m')
    else:
        print('VOCÊ: \33[1mTesoura\33[m')

    if jokpc == 1:
        print('PC: \33[1mPedra\33[m')
        if jokusu == jokpc:
            print('Empatamos!')
        elif jokusu == 2:
            print('Você ganhou!')
        else:
            print('Eu ganhei!')
    elif jokpc == 2:
        print('PC: \33[1mPapel\33[m')
        if jokusu == jokpc:
            print('Empatamos!')
        elif jokusu == 3:
            print('Você ganhou!')
        else:
            print('Eu ganhei!')
    else:
        print('PC: \33[1mTesoura\33[m')
        if jokusu == jokpc:
            print('Empatamos!')
        elif jokusu == 1:
            print('Você ganhou!')
        else:
            print('Eu ganhei!')
    continuar = input('Jogar novamente? (S ou N) ').upper()
    if continuar == 'N':
        break
    else:
        contador = contador + 1
print('\n Obrigado por jogar comigo!!!\n\n'
      '    ---------\n'
      '    | <   > |  MDS GAMES \n'
      '    |   ;   |\n'
      '    | [___] |  PRODUCERS \n'
      '    ---------\n')





