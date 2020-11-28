#Esquivel Macías Erick Xavier   16590461
#Gómez OnAntera Jacob Misael      16590474

import json
import random
Arbol = False

with open ("colina.json","r") as read_file:
	data = json.load(read_file)
	Arbol = data['Arbol']

def subirColina(nodoi,nodof):
	Posible = []
	nAnt = []
	nSig = []
	for e in Arbol:
		if (e["nodo"]==nodoi):
			Posible = e["Rutas"]
	m = Posible[0][0]
	for i in Posible:
		if m > i[0]:
			nAnt = i[0]
			nSig = i[1]
			m = i[0]
		elif (m == i[0]):
			nAnt += i[0]
			nSig += i[1]
	for k in Posible:
		if (len(nSig)>1):
			L = random.choice(nSig)
			if(L == nodof):
				print (m,L)
				return True
			else:
				print (m,L)
				return subirColina(L, nodof)
		if k[0] == m:
			if k[1] == nodof:
				print (m,k[1])
				return True
			else:
				print (m,k[1])
				return subirColina(k[1],nodof)

R = subirColina("A","K")
if (R):
	print ("Búsqueda Exitosa")
else:
    print ("No Existe El Nodo")