x:int = int(input('x értéke: '))
y:int = int(input('y értéke: '))
print(f'különbség: {abs(x-y)}')
# --------------
a:int = int(input('a értéke: '))
b:int = int(input('b értéke: '))
c:int = int(input('c értéke: '))
if a+b>c and a+c>b and b+c>a:
    print('szerkeszthető')
else:
    print('nem szerkeszthető')
# --------------
nev:str = input('írd be a neved: ')
for k in nev: print(k)
# --------------
vlmi:str = input('írj be valamit: ')
print((len(vlmi)+2) * '*')
print(f'*{vlmi}*')
print((len(vlmi)+2) * '*')
