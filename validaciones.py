def validar_continuar_menu(opcion:str) -> bool:
    validacion = False

    if opcion == "si" or opcion == "no":
         validacion = True

    return validacion



def validar_elemento_dentro_de_lista(elemento:str|int, lista:list) -> bool:
    encontro_elemento = False

    for i in range(len(lista)):
        if lista[i] == elemento:
            encontro_elemento = True
            break
    
    return encontro_elemento



def validar_numero_dentro_de_rango(numero:int, rango_inicio:int, rango_final:int) -> bool:

    if numero >= rango_inicio and numero <= rango_final:
        numero_validado = True
    else:
        numero_validado = False
        
    return numero_validado



