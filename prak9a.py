get=open('L200190065','w')

nim=input('Masukkan NIM: ')
ttl=input('Masukkan Tanggal Lahir (DD-MM-YY): ')
nama=input('Masukkan Nama Lengkap: ')
get.writelines('{}\n{}\n{}'.format(ttl,nim,nama))

get.close()
