contador = 0
tentedenovo = 'DIGITE SOMENTE NÚMEROS!!!'
while contador < 5:
    num = input('Digite um número de 0 a 9999: ')
    if num.isnumeric():
        compnum = len(num)
        if compnum == 4:
            print('Milhar: ', num[0])
            print('Centena: ', num[1])
            print('Dezena: ', num[2])
            print('Unidade: ', num[3])
        elif compnum == 3:
            print('Centena: ', num[0])
            print('Dezena: ', num[1])
            print('Unidade: ', num[2])
        elif compnum == 2:
            print('Dezena: ', num[0])
            print('Unidade: ', num[1])
        else:
            print('Unidade: ', num[0])
        break
    else:
        contador = contador + 1
        if contador == 5:
            tentedenovo = ' '
            print(tentedenovo)
            print('Você não conseguiu, OTÁRIO!!!')
        else:
            print(tentedenovo)