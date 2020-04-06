cidade = str(input('Qual a sua cidade? ')).lower()
if 'santo' in cidade:
    cidade = cidade.replace('santo', 'demonho')
    print('O novo nome desta cidade é {}.'.format(cidade.title()))
else:
    print('Não há a palavra "SANTO" no nome da sua cidade!')