from datetime import datetime

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
            dni = input("Hola, Ingrese su DNI (o escriba 'salir'): ").strip()
            
            if dni.lower() == 'salir':
                print("[Bot]: Programa finalizado.")
                break
    
            if dni in base_datos_empleados:
                print("DNI encontrado")
                dni_usuario = dni
                estado = 2
            else:
                print("El DNI no existe. Intente de nuevo.")

        elif estado == 2:
            dias_totales = base_datos_empleados[dni_usuario]["Dias_disponibles"]
            nombre_empleado = base_datos_empleados[dni_usuario]["Nombre"]

            print(f"{nombre_empleado}, tenes {dias_totales} dias disponibles")
            entrada_dias = input("Cuantos dias te queres tomar?: ")
            
            try:
                dias_pedidos = int(entrada_dias)

                if dias_pedidos <= 0:
                    print("Por favor, ingrese una cantidad mayor a 0.")
                elif dias_pedidos <= dias_totales:
                    estado = 3
                else:
                    print("No tenes dias suficientes. Intenta otra cantidad.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif estado == 3: 
            fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/aaaa): ").strip()

            
            try:
                fecha_validada = datetime.strptime(fecha_inicio, "%d/%m/%Y")
                
                #
                if fecha_validada.year < 2026:
                    print("[Bot]: El año debe ser 2026 o posterior.")
                    continue
                    
            except ValueError:
                print("[Bot]: Fecha inválida o formato incorrecto. Use dd/mm/aaaa (Ej: 15/07/2026).")
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
            print("\n[Bot]: Gracias por usar el sistema de vacaciones.")
            opcion = input("¿Desea realizar otro trámite? (s/n): ").strip().lower()
            
            if opcion == 's':
                dni_usuario = ""
                estado = 1
            else:
                print("\n[Bot]: Cerrando sesión. ¡Hasta luego!\n")
                break

if __name__ == "__main__":
    iniciar_bot()