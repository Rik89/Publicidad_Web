words = [z for z in open("file.txt").read().split(' ')] #CREACION LISTAS DE PALABRAS
width = 15 #tamaño de la columna max, suponemos que es mayor que la longitud de cualquier palabra dada;
            #podría tomar esto como entrada, así
print (words[0]),
space = width - len(words[0])
for x in range(1, len(words)):
	l = len(words[x])
	if l <= space:
		space -= l+1
		print (" " + words[x]),
	else:
		print ("\n" + words[x]),
		space = width - l
