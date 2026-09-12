meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso"
            }
while True:
    print("-------------------MENÚ-------------------")
    print("1. Buscar palabra")
    print("2. Agregar palabra")
    print("3. Salir")
    eleccion = int(input("Ingrese el numero de su elección"))
    if eleccion == 1:
        word = input("Escribe una palabra que no entiendas:")
        if word in meme_dict.keys():
           print(meme_dict[word])
        else:
            print("No se encontró tu palabra.")
    elif eleccion == 2:
        palabra = input("Ingrese su palabra")
        significado = input("Ingrese el significado de su palabra")
        meme_dict[palabra] = significado
    elif eleccion == 3:
        break
    else:
        print("Elije una opción correcta")
