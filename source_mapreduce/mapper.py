import sys
#Aqui para los input de entrada
for line in sys.stdin:
    # eliminas los espacion iniciales y finales
    line = line.strip()
    # aqui utiliza un filtro para dividir
    words = line.split()
    # Contador
    for word in words:
        # Escribe los resultado de la salida
        # Aqui sera la entrada para el paso de 
        # Reduce es decir la entrada para reducer.py
        #
        print '%s\t%s' % (word, 1)
