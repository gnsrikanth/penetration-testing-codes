import requests as rr
import sys
fi='/usr/share/dirb/wordlists/common.txt'

URL= sys.argv[1]

f=open(fi,'r')
dirs=f.read()
dirs=dirs.split('\n')

for i in dirs:
	data=rr.get(URL+i)
	if data.status_code != 404:
		print('[+]'+str(URL+i)+'  ->  '+str(data.status_code))
	else:
		pass
		#print(URL+i,end='\r')
