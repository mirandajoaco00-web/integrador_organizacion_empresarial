
## ====================================================================
## Base de datos simulada
## ====================================================================

base_datos_empleados = {
    "1234567": {"Nombre": "Joaquin Miranda", "Dias_disponibles": 14},
    "7891011": {"Nombre": "Maria Juana", "Dias_disponibles": 21}
}

tramites = []

def iniciar_bot():
    estado = 1
    dni_usuario = ""
    dias_pedidos = 0

    while True:
        if estado == 1:
            dni = input("Hola, Ingrese su dni: ")
    
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
            fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")

            partes = fecha_inicio.split("/")

           
            if len(partes) != 3:
                print("[Bot]: Formato incorrecto. Debe usar barras para separar (dd/mm/aaaa).")
                continue

          
            try: 
                dia = int(partes[0])
                mes = int(partes[1])
                anio = int(partes[2])

                if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 2026:
                    print("[Bot]: Fecha lógica inválida. Revise los números.")
                    continue
        
            except ValueError:
                print("[Bot]: La fecha debe contener solo números enteros. No se permiten letras.")
                continue
            
            
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


if __name__ == "__main__":
    iniciar_bot()