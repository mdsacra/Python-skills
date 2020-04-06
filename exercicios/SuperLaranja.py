print('''
=================
   SUPERMERCADO
    LARANJINHA
=================''')

cont = 0
caros = 0
baratovlr = 0
baratoprd = ''
total = 0
while True:
    print('INSIRA AS INFORMAÇÕES DO PRODUTO')
    prod = str(input('Produto: ')).strip().upper()
    valor = float(input('Valor: R$ '))
    total += valor
    cont += 1
    if valor > 20:
        caros += 1
    if cont == 1:
        baratovlr = valor
        baratoprd = prod
    else:
        if valor < baratovlr:
            baratovlr = valor
            baratoprd = prod
    seguir = str(input('Quer continuar? ')).strip().upper()
    if seguir != 'S' and seguir != 'N':
        seguir = str(input('Tente "S" para SEGUIR ou "N" para ENCERRAR: '))
    if seguir == 'N':
        break
print(f'O total gasto na sua compra é de R$ {total:.2f}.')
print(f'Você comprou {caros} produto(s) acima de R$ 20.00')
print(f'O produto mais barato foi o/a {baratoprd}, no valor de R$ {baratovlr:.2f}.')