'''n = 0
cont = 0
s = 0
while True:
    n = int(input('Digite um número (999 p/ parar): '))
    cont += 1
    if n == 999:
        break
    s += n
print(f'Você digitou {cont} valor(es) e eles somam {s}.')'''

'''n = 0
while True:
    n = int(input('Quer ver a tabuada de: '))
    if n < 0:
        break
    else:
        print('---------------')
        for x in range(1, 11):
            print(f'{n} X {x} = {n*x}')
        print('---------------')
print('Encerrou!')'''

'''from random import randint
neu = 0
npc = randint(0, 101)
vit = 0
while True:
    parimpar = str(input('[P] Par; [I] Ímpar: ')).strip().upper()
    neu = int(input('Digite o número: '))
    res = neu + npc
    print(f'Número do PC: {npc}')
    print(f'Resultado: {res}')
    if res % 2 == 0:
       if parimpar == 'P':
           print(f'{res} é PAR. \33[1;36mVocê ganhou!\33[m')
           vit += 1
       else:
           print(f'{res} é PAR. \33[1;31mVocê perdeu!\33[m')
           break
    if res % 2 != 0:
        if parimpar == 'I':
            print(f'{res} é ÍMPAR. \33[1;36mVocê ganhou!\33[m')
            vit += 1
        else:
            print(f'{res} é ÍMPAR. \33[1;31mVocê perdeu!\33[m')
            break
print(f'Você ganhou {vit} partidas consecutivas.')'''

'''print('-------------------\n'
      'CADASTRO DE PESSOAL\n'
      '-------------------')
maior = 0
homem = 0
nova = 0
while True:
    print('CADASTRE ALGUÉM')
    idade = int(input('Idade: '))
    if idade > 120:
        idade = int(input('Digite um valor entre 0 e 120: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite "M" para masculino e "F" para feminino: ')).strip().upper()
    if sexo == 'M':
        homem += 1
    if idade < 20:
        if sexo == 'F':
            nova += 1
    seguir = str(input('Deseja continuar? ')).strip().upper()
    if seguir != 'S' and seguir != 'N':
        seguir = str(input('Digite "S" para continuar ou "N" para parar: '))
    if seguir == 'N':
        break

print('FIM DO PROGRAMA')
print(f'Você cadastrou:\n-> {maior} pessoas maiores de 18 anos\n-> {homem} homens\n-> {nova} mulheres com menos de 20 anos')'''




