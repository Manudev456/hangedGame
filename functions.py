def acierto(palabra, palabra_oculta, caracter):
    if caracter in palabra:
        for i in palabra:
            for j in caracter:
                if i != j:
                    continue
                else:
                    palabra_oculta[palabra.index(i)] = j
    
    return palabra_oculta


def hidenList(palabra):
    list = []
    for i in palabra:
        list.append("_")
    return list

def hidenStrings(palabra):
    string = ""
    for i in palabra:
        string += "_"
    return string

def main():
    live = 8
    score = 0
    caracter = ""
    palabra = "polar"
    plabra_oculta = hidenList(palabra)
    while live > 0:
        a = input("intruduzca una letra: ")
        caracter += a
        print(plabra_oculta)
        jugada = acierto(palabra, plabra_oculta, caracter)
        print(jugada)
        if caracter in palabra:
            score += 1
        else: 
            live -= 1


if __name__ == "__main__":
    main()

