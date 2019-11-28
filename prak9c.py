import shelve

get=shelve.open('Arindra')

get['ttl']=open('L200190065',"r").readlines()[0]
get['nim']=open('L200190065',"r").readlines()[1]
get['nama']=open('L200190065',"r").readlines()[2]
get['kota']=open('L200190065',"r").readlines()[3]

