from datos import *
from opciones import *
from funciones import *
from validaciones import *

continuar_menu = "si"

while continuar_menu == "si":
    
    mostrar_menu()
    opcion = input("Ingrese opcion a elegir: ")
    opcion = convertir_cadenas_a_numeros(opcion)
    while validar_numero_dentro_de_rango(opcion, 1, 9) == False:
        opcion = input("[ERROR] Ingrese opcion valida a elegir: ")
        opcion = convertir_cadenas_a_numeros(opcion)
    print()

    match opcion:

        case 1:
            usuario = input("Ingrese usuario: ")
            usuario = convertir_cadena(usuario, 2)

            while validar_elemento_dentro_de_lista(usuario, usuarios_vip) == False:
                usuario = input("[ERROR] Ingrese un usuario valido: ")
                usuario = convertir_cadena(usuario, 2)
            
            empresa_elegida = input("Ingrese empresa (APPLE, TESLA, NVIDIA): ")
            empresa_elegida = convertir_cadena(empresa_elegida, 1)

            while validar_elemento_dentro_de_lista(empresa_elegida, empresas) == False:
                empresa_elegida = input("[ERROR] Ingrese empresa valida (APPLE, TESLA, NVIDIA): ")
                empresa_elegida = convertir_cadena(empresa_elegida, 2)

            cantidad_acciones = input("Ingrese la cantidad de acciones a comprar (0-500): ")
            cantidad_acciones = convertir_cadenas_a_numeros(cantidad_acciones)
            rango_acciones = validar_numero_dentro_de_rango(cantidad_acciones, 0, 500)

            while (cantidad_acciones == None) or (rango_acciones == False):
                cantidad_acciones = input("[ERROR] Ingrese la cantidad valida de acciones a comprar (Solo numeros y en un rango de 0 a 500): ")
                cantidad_acciones = convertir_cadenas_a_numeros(cantidad_acciones)
                rango_acciones = validar_numero_dentro_de_rango(cantidad_acciones, 0, 500)

            registrar_transaccion(usuario, empresa_elegida, cantidad_acciones, usuarios_vip, valor_acciones, acciones_usuarios_vip)

        case 2:   
            mostrar_cantidad_de_acciones_por_usuario(usuarios_vip, empresas, acciones_usuarios_vip)

        case 3:
            promedio_acciones_adquiridas(empresas, acciones_usuarios_vip)

        case 4:
            ordenar_usuarios_descendiente(usuarios_vip, empresas, valor_acciones, acciones_usuarios_vip)

        case 5:
            inversion_total(valor_acciones, acciones_usuarios_vip)

        case 6:
            empresa_comrpo_mas_acciones(usuarios_vip, empresas, acciones_usuarios_vip)

        case 7:
            accion_con_mayor_inversion(empresas, valor_acciones, acciones_usuarios_vip)

        case 8:
            porcentaje_inversion_usuario_comparado_al_total(usuarios_vip, valor_acciones, acciones_usuarios_vip)

        case 9:
            usuarios_superan_inversion_promedio(usuarios_vip, valor_acciones, acciones_usuarios_vip)
    
    continuar_menu = input("Desea continuar en el menu (si/no): ")
    continuar_menu = convertir_cadena(continuar_menu, 0)
    while validar_continuar_menu(continuar_menu) == False:
        continuar_menu = input("[ERROR] Seleccione una opcion valida para continuar en el menu (si/no): ")
        continuar_menu = convertir_cadena(continuar_menu, 0)
