

def problema(solucion,fila,n):
	if fila>=n:                             # si la fila es mayor que n, entonces devolvemos falso
		return False
	exito = False                            # inicializamos exito a False
	
	while True:
            if (solucion[fila] < n):                       # si el valor de la columna para la fila es mayor o igual que n, entonces no seguimos incrementando, con esto evitamos indices fuera del array.
                solucion[fila] = solucion[fila] + 1       # incrementamos el valor de columna para la reina i-esima de la fila i-esima.

            if (Valido(solucion,fila)):                    # si la reina i-esima de la fila i-esima de la columna j en la fila k no entra en conflicto con otra reina, proseguimos.

                if fila != n-1:                            # si aun no hemos acabado todas las filas, procedemos a la siguiente fila.
                    exito = problema(solucion, fila+1,n)
                    if exito==False:                        # si del valor devuelto de problema tenemos falso, ponemos a 0 el valor de la fila + 1 para asi descartar los nodos fracaso.
                        solucion[fila+1] = 0

                else:
                    print solucion                          # si ya hemos acabado, imprimimos la disposicion de las fichas en el tablero y devolvemos True.
                    for x in range(n):
                        for i in range(n):
                            if solucion[x] == i+1:
                                print "X",
                            else:
                                print "- ",

                        print "\n"
                    exito = True
            if (solucion[fila]==n or exito==True):         # si el valor de la columna j de la fila k es igual a n o exito es igual a True, salimos del bucle y devolvemos exito.
                break

	return exito


def Valido(solucion,fila):
	# Comprueba si el vector solucion construido hasta la fila es 
	# prometedor, es decir, si la reina se puede situar en la columna de la fila

	for i in range(fila):
		if(solucion[i] == solucion[fila]) or (ValAbs(solucion[i],solucion[fila])==ValAbs(i,fila)):
			return False

	return True

def ValAbs(x,y):
	if x>y:
		return x - y
	else:
		return y - x	



###############################


print "PEC 1 IA 8 REINAS By Dani"
print "#"*26
print "\n"

n = 8
solucion = []
for i in range(n):
	solucion.append(0)
fila = 0
for j in range(n):
    for e in range(n):
        solucion[e] = j
        print problema(solucion, fila, n)



