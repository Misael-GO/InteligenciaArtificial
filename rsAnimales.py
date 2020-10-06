#Esquivel Macías Erick Xavier   16590461
#Gómez Olvera Jacob Misael      16590474
import json
conocimiento = False

with open("rsAnimales.json", "r") as read_file:
    data = json.load(read_file)
    conocimiento = data['Conocimiento']

def valida(A, B, C, Con):
    if B == "Es":
        return valida2(A, B, C, Con)
    if B == "Vive":
        return valida2(A, B, C, Con)
    if B == "Tiene":
        return valida2(A, B, C, Con)

def valida2(A, B, C, Con):
    o = 0
    while o < len(Con):
        if Con[o][0] == A:
            if Con[o][1] == B:
                if Con[o][2] == C:
                    return True
        o = o + 1
    return False

def buscar(A, B, C):
    return valida(A, B, C, conocimiento)

def main():
    print('Usar la nomenclatura buscar("<Animal>","<Es o Vive o Tiene>","<Clasif o Lugar oCaract>")')
    print('Ejemplo buscar("<Delfin>","<Vive>","<Tierra>")')
    print("Escribe 'quit()' para salir")
    r = False
    while not r:
        Entrada = input("> ")
        if Entrada == 'q':
            return
        if Entrada == '':
            print("No es válido")
        else:
            mostrar = eval(Entrada)
            print(mostrar)

if __name__ == "__main__":
    main()