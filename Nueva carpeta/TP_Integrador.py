

## Base De datos simulada

base_datos_empleados = {
    "1234577": {"Nombre": "Joaquin Miranda", "Dias_disponibles": 14},
    "156768": {"Nombre": "Maria Juana", "Dias_disponibles": 21}
}

tramites = []

def iniciar_bot():
    estado = 1
    dni_usuario = ""

    while True:
        if estado == 1:
            dni = input("Ingrese su dni: ")
    
            if dni in base_datos_empleados:
                print("DNI encontrado")
                dni_usuario = dni
                estado = 2
            else:
                print("El dni no existe. Intente de nuevo")

        elif estado == 2:
            dias_totales = base_datos_empleados[dni_usuario]["Dias_disponibles"]
            nombre_empleado = base_datos_empleados[dni_usuario]["Nombre"]

            print(f"{nombre_empleado}, tenes {dias_totales} dias disponibles")
            entrada_dias = input("Cuantos dias te queres tomar?: ")

            
            try:
                dias_pedidos = int(entrada_dias)

                if dias_pedidos <= dias_totales:
                    estado = 3
                else:
                    print("No tenes dias suficientes. Intenta otra cantidad")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif estado == 3: 
            fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/aa): ")
            
            base_datos_empleados[dni_usuario]["Dias_disponibles"] -= dias_pedidos
            
            tramites.append({
                "dni": dni_usuario,
                "dias_pedidos": dias_pedidos,
                "fecha_inicio": fecha_inicio,
                "estado": "aprobado"
            })

            print("\n[Bot]: ¡Trámite guardado con éxito!")
            print(f"Te quedan {base_datos_empleados[dni_usuario]['Dias_disponibles']} días de vacaciones.")
            estado = 4

        elif estado == 4:
            print("\n[Bot]: Gracias por usar el sistema de vacaciones. Cerrando sesión...\n")
            dni_usuario = ""
            estado = 1