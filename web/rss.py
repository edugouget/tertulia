#!/usr/bin/python
from glob import glob
import os.path, time
import json


def modificado(file):
	data = time.strptime(time.ctime(os.path.getmtime(file)))
	dia = ('00'+ str(data.tm_mday))[-2:]
	mes = ('00'+ str(data.tm_mon))[-2:]
	return dia + '/' + mes + '/' + str(data.tm_year)
	#return str(data.tm_year) + '/' + mes + '/' + dia
	
def numero(file):
	x = file.find('-')
	return file[0:x-1].strip()

def parentesis(file):
	return (file.find('(') , file.find(')')) 
	
def titulo(file):
	x = parentesis(file)
	y = file.find('-')
	if x[0]>0 and x[1] >0:
		return file[y+1:x[0]-1].strip()
	else:
		return ''

def especialidade(file):
	x = parentesis(file)
	if x[0]>0 and x[1] >0:
		return file[x[0]+1:x[1]].strip()
	else:
		return ''

def main():
	tmp = glob('*.mp3')
	arquivos = sorted(tmp, reverse=True)
	data = {}
	for x in arquivos:
		#print (modificado(x) +' == Tertulia ' + numero(x) + ' == ' + titulo(x))
		#data={'tertulia':numero(x),'titulo':titulo(x),'data':modificado(x),'arquivo':arquivos[x]}
		data[numero(x)]= [titulo(x) , especialidade(x) , x , modificado(x)]
		#print ( [numero(x), titulo(x) , especialidade(x) , x , modificado(x)])

	print(json.dumps(data, ensure_ascii=False))

if __name__ == '__main__':
    main()
