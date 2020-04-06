diasaluguel = int(input('Por quantos dias você ficou com o carro? '))
kmrodados = float(input('Quantos quilômetros você rodou com o carro? '))
diarias = diasaluguel*60
kmreal = kmrodados*0.15
aluguel = diarias+kmreal
print('O valor total do seu aluguel é de R$ {:.2f}!'.format(aluguel))

