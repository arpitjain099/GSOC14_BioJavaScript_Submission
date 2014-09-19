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

