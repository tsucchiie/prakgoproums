get=open('L200190065','a')
readln=open('L200190065','r')

kota=input('Masukkan Nama Kota Asal: ')

get.writelines('\n{}'.format(kota))

string=''

#convert
ttl=open('L200190065',"r").readlines()[0]
tanggal=ttl[3:5]+'/'+ttl[0:2]+'/'+ttl[6:10]

nama=open('L200190065',"r").readlines()[2]
nim=open('L200190065',"r").readlines()[1]

print('''
Nama: {}
{},{}
{}
'''.format(nama,kota,tanggal,nim))


get.close()
