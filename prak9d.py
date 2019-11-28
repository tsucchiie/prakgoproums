import shelve

get=shelve.open('Arindra')

print('Nama:',get['nama'])
print('Nim:',get['nim'])
print('Tanggal Lahir:',get['ttl'])
print('Kota Asal:',get['kota'])
