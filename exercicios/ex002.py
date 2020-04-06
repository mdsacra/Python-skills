salario = float(input('Qual o seu salário atual? R$ '))
aumento = (salario/100)*15
novosal = aumento+salario
print('O seu novo salário será de R$ {:.2f}!'.format(novosal))
print('Você recebeu um aumento de R$ {:.2f}! Parabéns!'.format(aumento))