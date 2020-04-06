n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
raiz = s**(1/2)

print(' A soma dos números é {}, já a múltiplicação é {}. \n A divisão deles, resulta em {:.2f}. '
      'A divisão inteira é {}. A potência é {} e a raiz da soma é {:.2f}.'.format(s,m,d,di,p,raiz) )
