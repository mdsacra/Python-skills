'''frase = str(input('Digite uma frase qualquer: '))
frase = frase.lower()
letraa1 = frase.find('a')
letraaend = frase.rfind('a')
print(letraa1, letraaend)'''

'''nome = input('Digite seu nome: ')
nome = nome.lower()
primeiroespaco = nome.find(' ')
ultimoespaco = nome.rfind(' ')
primeironome = nome[:primeiroespaco]
ultimonome = nome[(ultimoespaco+1):]
print('Seu primeiro nome é {} e seu último nome é {}'.format(primeironome.title(), ultimonome.title()))'''

nome = input('Digite seu nome: ').lower().strip()
nomefatiado = nome.split()
print(len(nomefatiado))
