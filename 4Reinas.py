#Esquivel Macías Erick Xavier   16590461
#Gómez Olvera Jacob Misael      16590474

def Queens(fl,cl):
	Tablero = [
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]
	]
	xD = 0
	while (xD != 4 and fl < 4):
		while (Tablero[fl][cl] != 0):
			if(cl != 3):
				cl += 1
			elif(fl != 3):
				fl += 1
				cl = 0
		Tablero[fl][cl] = 1
		hor(fl,0,Tablero)
		ver(0,cl,Tablero)
		diaDer(fl,cl,Tablero)
		diaIzq(fl,cl,Tablero)
		fl +=1
		cl = 0
		xD += 1
	if (xD < 4):
		Queens(0,1)
	print ("# Reinas:",xD)
	for e in Tablero:
		print (e)
	print ("")

def hor(l,a,Tablero):
	while(a <= 3):
		if (Tablero[l][a] == 0):
			Tablero[l][a] = 2
		a += 1

def ver(l,a,Tablero):
	while(l <= 3):
		if (Tablero[l][a] == 0):
			Tablero[l][a] = 2
		l += 1

def diaDer(l,a,Tablero):
	while(l <= 3 and a <= 3):
		if (Tablero[l][a] == 0):
			Tablero[l][a] = 2
		l += 1
		a += 1

def diaIzq(l,a,Tablero):
	while(l <= 3 and a >= 0):
		if (Tablero[l][a] == 0):
			Tablero[l][a] = 2
		l += 1
		a -= 1

Queens (0,0)