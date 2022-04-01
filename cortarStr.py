strings = '012345678901234567890123456789012346578901234567890123465789'
n = 10
l1 = [strings[i:i+n] for i in range(0,len(strings), n)]
retorno = '.'.join(l1)
print(l1)
print(retorno)

