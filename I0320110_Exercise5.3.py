# Penggunaan if untuk tiga kasua dan selebihnya
# input bilangan
print('Masukkan kooordinat!')

x = int(input('Masukkan nilai x: '))
y = int(input('Masukkan nilai y: '))

info = 'Koordinat (' + str(x) + ',' + str(y) + ') berada pada kuadran'

# Memerikasa nilai x dan y
if x>0 and y>0:
    print (info + 'I')
elif x<0 and y>0:
    print(info + 'II')
elif x<0 and y<0 :
    print(info + 'III')
elif x>0 and y<0:
    print( info+ 'IV')
else:
    pass
print()