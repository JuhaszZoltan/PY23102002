from module import *

x:int = int(input('x értéke: '))
y:int = int(input('y értéke: '))
print(abs_kulonbseg(x, y))

a:int = int(input('a értéke: '))
b:int = int(input('b értéke: '))
c:int = int(input('c értéke: '))
if szerkesztheto_e(a, b, c): print('szerkeszthető')
else: print('nem szerkeszthető')

fuggoleges_kiiras(input('írd be a neved: '))

valami:str = input('írj be valamit: ')
print(keretez(valami))