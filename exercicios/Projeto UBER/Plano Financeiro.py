#Seus dinheiros
dincart = float(input('Dinheiro na carteira: R$ '))
dinguard = float(input('Dinheiro guardado: R$ '))
dincaixa = float(input('Dinheiro na Caixa: R$ '))
dinUBER = float(input('Dinheiro na UBER: R$ '))
din99 = float(input('Dinheiro na 99: R$ '))
outrodin = float(input('Outros dinheiros (se houver): R$ '))

totaldindin = dincart + dinguard + dincaixa + dinUBER + din99 + outrodin

#Suas contas
carro = float(input('Valor do carro (parcela ou aluguel): R$ '))
empr = float(input('Empréstimos a vencer: R$ '))
casa = float(input('Previsão de gastos residenciais: R$ '))
cel = float(input('Gastos com celular: R$ '))
outros1 = float(input('Outros gastos: R$ '))
outros2 = float(input('Outros mais: R$ '))

totalcontas = carro + empr + casa + cel + outros1 + outros2

#Cálculo
dia = int(input('Digite o seu próximo dia de trabalho do mês: '))
tempo = 25 - dia + 1
falta = totalcontas-totaldindin
diaria = (((falta)/tempo)*100)/70

#Respostas
print('Você possui no momento R$ {:.2f}.'.format(totaldindin))
print('O total das suas contas é de R$ {:.2f}.'.format(totalcontas))
print('Você ainda tem {} dias para juntar R$ {:.2f}.'.format(tempo, falta))
print('Sua META DIÁRIA é de R$ {:.2f}.'.format(diaria))
