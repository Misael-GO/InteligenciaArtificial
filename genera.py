"""
#Esquivel Macías Erick Xavier   16590461
#Gómez Olvera Jacob Misael      16590474

En el comentario del archivo anterior, hice varias cosas, 
para poder sacar la matriz_json de probabilidades, 
ahora hay que hacer un programa que a partir de 10 tweets genere la misma 
matriz_json de probabilidades
sabiendo de ante mano cuales son los de stream

Sugiero esta estructura, para lo tweets

{
	"Tweets" : [
		{"Stream":true, "texto":"Vamos a darle a Among Us con famosos"},
		{"Stream":false, "texto":"El Fugitivo: La Historia en 1 Video"},
	]
}

y debe generar el  json compatible con el programa de clasificacion
"""

import json
tweets = False
i = 0
pclave = ["=)",",","el","y","con","Ya","ando","el","para","este","si","la","al","mas","que","a","un","en","le","ya","es","Que","van","los","sí","bueno"]

with open("fedewolf.json","r") as read_file:
	data = json.load(read_file)
	tweets = data['Tweets']

def genera_json(matriz_json):
	print()
	print("JSON Generado")
	i = 0
	data = {}
	data["Probabilidades"] = []
	while i < len(matriz_json):
		data["Probabilidades"].append([matriz_json[i][0],matriz_json[i][4]])
		i = i + 1
	with open('genera.json', 'w') as file:
		json.dump(data, file, indent=1)
	with open("genera.json","r") as read_file:
		data = json.load(read_file)
		tw = data["Probabilidades"]
	return(tw)

def matriz_json(tweets,palabra,numero_tweets):
	i = 0
	s = 0
	n = 0
	matr = []
	print("Probabilidades")
	while i < len(palabra):
		j = 0
		while j < len(tweets):
			if tweets[j] == palabra[i]:
				s = s + 1
			n = numero_tweets - s
			j = j + 1
		t = s + n
		matr.append([palabra[i], n, s, t, s/t, n/t])
		s = 0
		n = 0
		i = i + 1
	print(matr)
	return genera_json(matr)

def pclaves(tweet,pclave):
	j = 0
	k = []
	C = []
	while j < len(tweet):
		i = 0
		while i < len(tweet[j]):
			if not tweet[j][i] in pclave:
				s = tweet[j][i]
				k = k + [s]
			i = i + 1
		j = j + 1
	j = 0
	while j < len(k):
		if not k[j] in C:
			C = C + [k[j]]
		j = j + 1 
	return matriz_json(k,C, len(tweet))

def matriz(tweets,pclave,t = []):
	i = 0
	while i < len(tweets):
		tw = tweets[i]
		Stream = tw['Stream']
		texto = tw['texto']
		if Stream == True:
			texto = texto.split()
			t = t + [texto]
		i = i +1
	return pclaves(t,pclave)

print(matriz(tweets,pclave))