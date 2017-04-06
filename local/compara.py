from glob import glob
import os.path, time
import json
from ftplib import *

tmp = glob('*.mp3')
arquivos = sorted(tmp, reverse=True)

#print(arquivosL[0:30])

arquivosL = arquivos[0:30]

###################################################
ftp = FTP_TLS('endereco_do_ftp')
ftp.sendcmd('USER usuario')
ftp.sendcmd('PASS senha')
ftp.cwd('tertulias')

ls = []
saida = []
# Retorna lista de arquivos
def lista_arquivos(ls , saida):
	ftp.retrlines('MLSD', ls.append)
	for entry in ls:
		#print(entry)
		saida.append( entry.split(';')[7][1:] )
	#print(saida)
	return
	
def mp3( entrada):
	y = []
	for x in entrada:
		if x.find('mp3')>0:
			y.append(x)
	return sorted(y, reverse=True)

	
lista_arquivos(ls,saida)
#print(saida)
arquivosR = mp3 (saida)

apagar = list(set(arquivosR) - set(arquivosL))
enviar = list(set(arquivosL) - set(arquivosR))

print('Apagar')
print(apagar)
print('=====')
print('Enviar')
print(enviar)
print('=====')

## UPLOAD
if len(enviar)>0 :
	for x in enviar:
		file = open(x,'rb')                  # file to send
		print('Enviando => ' + x)
		ftp.storbinary('STOR ' + x , file)   # send the file
		file.close()                         # close file and FTP
else:
	print('Nada para enviar')

#Apagar Remoto
if len(apagar)>0 :
	for x in apagar:
		print('Apagando => ' + x)
		ftp.delete(x)
else:
	print('Nada para apagar')

ftp.quit()
