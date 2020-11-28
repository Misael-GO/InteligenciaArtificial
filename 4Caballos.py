#Esquivel Macías Erick Xavier   16590461
#Gómez Olvera Jacob Misael      16590474

import json
with open ("caballos.json","r") as read_file:
	data = json.load(read_file)
	Arbol = data['Arbol']
	TableroI = data['TableroI']
	TableroF = data['TableroF']

def caballos(Mat,fin,op):
	Tablero=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
	l = 0
	while(l < 3):
		a = 0
		while(a < 3):
			if (Mat[l][a] != 0):
				valor = Mat[l][a]
				Mat[l][a] = 0
				busqueda(l,a,valor,Tablero,op)
			a +=1
		l +=1
	for e in Tablero:
		print (e)
	print ("")
	if (Tablero != TableroF):
		return caballos(Tablero,fin,op)

def busqueda(pos_l,pos_a,valor,Tablero,op):
	elemento = M[pos_l][pos_a]
	for e in Arbol:
		if (elemento == e[0]):
			l = 0
			while(l <= 2):
				a = 0
				while(a <= 2):
					if (M[l][a] == e[op]):
						Tablero[l][a] = valor
						return Tablero
					a += 1
				l += 1

M=[
    [0,1,2],
    [3,4,5],
    [6,7,8]
    ]
    
op = int(input("Ingresa 1 Para Recorrido por Derecha o 2 Para Recorrido por Izquierda "))
if (op < 1 or op > 2):
	print ("Ingresa Solo 1 o 2")
	quit()
caballos(TableroI,TableroF,op)