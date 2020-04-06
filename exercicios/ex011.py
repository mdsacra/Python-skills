num = int(input('Digite um número: '))
for n in range(1,11):
    print('{0} x {1} = \33[1;31m{2}\33[m'.format(num, n, num*n))