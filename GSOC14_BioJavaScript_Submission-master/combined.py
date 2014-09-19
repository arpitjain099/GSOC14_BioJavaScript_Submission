import codecs
number_of_characters_per_line=60
fi=codecs.open("ADCAPI0762.pir", 'r', encoding='utf-8')
f=fi.read()
fi.close()
f=f.split(">")
var=''
for index,i in enumerate(f):
	#i=i.split("\n")
	if index>0:
		i=i.split("\n")
		for index2,k in enumerate(i):
			if index2>1:
				list_temp=k.strip()
				len_list=len(list_temp)
				for index3,l in enumerate(list_temp):
					var=var+(l)
		var=var+("\n")
final_output=codecs.open("output.txt", 'w', encoding='utf-8')
f=var.split("\n")
lent=len(f)
gen_length=0
arr=[]
for index,i in enumerate(f):
	if index<lent-1:	
		gen_length=len(i)
		arr.append(i)
val=gen_length/number_of_characters_per_line + 1
for k in range(0,val-1):
	for i in range(len(arr)):
		for l in range(number_of_characters_per_line*k,number_of_characters_per_line*(k+1)):
			final_output.write(arr[i][l])
		final_output.write("\n")

	final_output.write("\n")

#last case
for i in range(len(arr)):
	for l in range(number_of_characters_per_line*(val-1),gen_length):
		final_output.write(arr[i][l])
	final_output.write("\n")

fi=codecs.open("output.txt", 'r', encoding='utf-8')
f=fi.read()
fi.close()
f=f.replace('-','<font family="monospace" style="background-color: #b0c4de">-</font>')
f=f.replace('A','<font style="background-color: #deb887">A</font>')
f=f.replace('T','<font style="background-color: #7fff00">T</font>')
f=f.replace('Y','<font style="background-color: #b8860b">Y</font>')
f=f.replace('K','<font style="background-color: #8d2be2">K</font>')
f=f.replace('V','<font style="background-color: #deb887">V</font>')
f=f.replace('L','<font style="background-color: #deb887">L</font>')
f=f.replace('I','<font style="background-color: #deb887">I</font>')
f=f.replace('P','<font style="background-color: #deb887">P</font>')
f=f.replace('G','<font style="background-color: #deb887">G</font>')
f=f.replace('A','<font style="background-color: #deb887">A</font>')
f=f.replace('Q','<font style="background-color: #7fff00">Q</font>')
f=f.replace('S','<font style="background-color: #7fff00">S</font>')
f=f.replace('E','<font style="background-color: #8b0000">E</font>')
f=f.replace('D','<font style="background-color: #8b0000">D</font>')
f=f.replace('F','<font style="background-color: #daa520">F</font>')
f=f.replace('C','<font style="background-color: #daa520">C</font>')
f=f.replace('R','<font style="background-color: #8b0000">R</font>')
f=f.replace('H','<font style="background-color: #8b0000">H</font>')
f=f.replace('N','<font style="background-color: #8b0000">N</font>')
f=f.replace('W','<font style="background-color: #8b0000">W</font>')
f=f.replace('M','<font style="background-color: #8b0000">M</font>')
f=f.replace('*','<font style="background-color: #ff69b4">*</font>')
f=f.replace('\n','<br>')
fi=codecs.open("sample.html", 'w', encoding='utf-8')
fi.write("<p>")
fi.write('<style>p{font-family:monospace;}</style></head>')
fi.write(f)
fi.write("</p>")
fi.close()
