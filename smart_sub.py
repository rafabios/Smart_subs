import re, os, sys, itertools

str_avi = ''
split_avi = ''
global zzz
lista_avi = []
lista_srt = []
lista_final = []
os.chdir('.')
f1 = os.listdir(".")


for full in f1:
	avi = re.search(".*([Ss][0-9].[eE][0-9].)+.*(...$)", full )
	if avi:

		if avi.group(2) == 'avi':
			lista_avi.append(avi.group(0))
		elif avi.group(2) == 'srt':
			lista_srt.append(avi.group(0))
		else:
			pass
	else:
		print "Nenhum Arquivo localizado!"		

for f,b in itertools.izip(lista_avi,lista_srt): 
	data_avi = f.split('.')		
	data_srt = b.split('.')
	data_regx_avi = re.search(".*([Ss][0-9].[eE][0-9].)+.*(...$)", f )
	data_regx_srt = re.search(".*([Ss][0-9].[eE][0-9].)+.*(...$)", b )
	for x in lista_srt:
		data_regx_srt = re.search(".*([Ss][0-9].[eE][0-9].)+.*(...$)", x )
		if data_regx_avi.group(1) == data_regx_srt.group(1):
			print 'Arquivo video:', data_regx_avi.group(0)
			print 'Arquivo sub:  ', f.replace(data_avi[-1],data_srt[-1])
			#lista_final.append(f.replace(data_avi[-1],data_srt[-1])) 
			xx = f.replace(data_avi[-1],data_srt[-1])
			os.rename(x, xx)