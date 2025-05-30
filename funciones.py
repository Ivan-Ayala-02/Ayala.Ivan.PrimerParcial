def imprimir_separacion_en_consola(longitud:int):
    '''
    imprime una en consola una serie de barras (-----). La longitud de esta debe ser
    especificada para funcionar.
    '''
    if longitud > 0:
        cadena_longitud = ""
        for i in range(longitud):
            cadena_longitud += "-"
        print(cadena_longitud)



def buscar_posicion_elemento_en_lista(elemento:str|int, lista:list) -> int|None:
    '''
    Busca en una lista un elemento del mismo nombre o valor. Si la funcion lo encuentra, 
    esta devolvera la posicion en la que esta ubicada, y en caso de que no exista dicho
    elemento en la lista, esta devolvera un None.
    '''
    posicion_elemento = None

    for i in range(len(lista)):
        if lista[i] == elemento:
            posicion_elemento = i
            break
    
    return posicion_elemento



def convertir_cadena(cadena_original:str, tipo_de_conversion:int) -> str:
    '''
    Toma una cadena y lo convierte segun el numero ingresado en el tipo de conversion:

    0 = Convierte la cadena completa en minusculas.
    1 = Convierte la cadena completa en mayusculas.
    2 = Convierte SOLO la primera letra en mayuscula, el resto se convierte en minusculas.
    '''
    cadena_convertida = ""

    for i in range(len(cadena_original)):

        caracter = cadena_original[i]
        orden_caracter = ord(caracter) # ord: devuelve numero de caracter ascii

        if tipo_de_conversion == 0:
        # rango caracteres mayusculas: 65-89
            if orden_caracter >= 65 and orden_caracter <= 89:
                caracter = chr(orden_caracter + 32) #chr: devuelve el caracter
        
        elif tipo_de_conversion == 1:
        # rango caracteres minusculas: 97-122
            if orden_caracter >= 97 and orden_caracter <= 122:
                caracter = chr(orden_caracter - 32)
        
        elif tipo_de_conversion == 2:
            if i == 0 and orden_caracter >= 97 and orden_caracter <= 122:
                caracter = chr(orden_caracter - 32)
            elif orden_caracter >= 65 and orden_caracter <= 89:
                caracter = chr(orden_caracter + 32)
            
        cadena_convertida += caracter
    
    return cadena_convertida



def convertir_cadenas_a_numeros(cadena_original:str) -> int|None:
    '''
    Convierte una cadena con numeros dentro (Ej: "123") a un int (123). Esta funcion devuelve 
    unicamente numeros, salteando cualquier otra cosa en la cadena. Esta devuelve el entero, o
    en su caso de que no encuentre nada, un None.
    '''
    cadena_numerica = ""

    for i in range(len(cadena_original)):

        caracter = cadena_original[i]
        orden_caracter = ord(caracter) # ord: devuelve numero de caracter ascii
        
        if orden_caracter >= 48 and orden_caracter <= 57:
            # rango caracteres numericos: 48-57
            cadena_numerica += caracter

    if cadena_numerica != "":    
        cadena_numerica = int(cadena_numerica)
        return cadena_numerica
    else:
        cadena_numerica = None



def swapear_listas(lista:list, elemento_i, elemento_j):
    '''
    Cambia de posicion elementos de una lista
    '''
    temporal = lista[elemento_i]
    lista[elemento_i] = lista[elemento_j]
    lista[elemento_j] = temporal




def ordenar_lista(lista:list, tipo_de_ordenamiento:int = 0):
    '''
    Toma una lista y la ordena segun el tipo especificado:
    0: Ordena de forma ascendente (default)
    1: Ordena de forma descendente
    '''

    for i in range(0, len(lista)-1, 1):
        
        for j in range(i+1, len(lista)):

            if tipo_de_ordenamiento == 0:
                if lista[i] > lista[j]:
                    # Ascendente (Menor a mayor)
                    swapear_listas(i, j) # -- Funcion --

            elif tipo_de_ordenamiento == 1:
                if lista[i] < lista[j]:
                    # Descendente (Mayor a menor)
                    swapear_listas(i, j) # -- Funcion --