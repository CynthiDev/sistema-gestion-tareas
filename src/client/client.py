import requests
import getpass

BASE_URL = "http://localhost:5000"
session = requests.Session()  # Mantener sesión entre peticiones



def mostrar_cookies():
    """Función para depuración: muestra las cookies actuales"""
    cookies = session.cookies.get_dict()
    print(f"Depuracion - Cookies actuales: {cookies}")



def main():
    print("Cliente del Sistema de Gestión de Tareas")
    autenticado = False  # Estado de autenticación

    try:

        while True:
            # Menú para usuarios NO autenticados
            if not autenticado:
                print("\n=== Menú Principal ===")
                print("1. Registrarse")
                print("2. Iniciar sesión")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")


                if opcion == "1":
                    usuario = input("Usuario: ")
                    contrasenia = getpass.getpass("Contraseña: ")
                    respuesta = session.post(f"{BASE_URL}/registro", json={"usuario": usuario, "contrasenia": contrasenia})
                    resultado = respuesta.json()
                    print(resultado.get('mensaje') or resultado.get('error'))
                            

                elif opcion == "2":
                    usuario = input("Usuario: ")
                    contrasenia = getpass.getpass("Contraseña: ")
                    # Limpiar sesión previa
                    session.cookies.clear()  

                    respuesta = session.post(f"{BASE_URL}/login", json={"usuario": usuario, "contrasenia": contrasenia})
                    resultado = respuesta.json()
                    print(resultado.get('mensaje') or resultado.get('error'))
                    mostrar_cookies()  # Verifica las cookies después de login
                        
                    if respuesta.status_code == 200:
                        autenticado = True  # Cambiar estado a autenticado
                            
                elif opcion == "3":
                    print("Saliendo...")
                    break
                        
                else:
                    print("Opción inválida")

            
            # Menú para usuarios autenticados
            else:
                print("\n=== Menú de Usuario ===")
                print("1. Ver tareas")
                print("2. Agregar tarea")
                print("3. Cerrar sesión")
                opcion = input("Seleccione una opción: ")


                if opcion == "1":
                    respuesta = session.get(f"{BASE_URL}/tareas")
                    if respuesta.status_code == 200:
                        print("\n--- Tus tareas ---")
                        print(respuesta.text)
                    else:
                        error = respuesta.json().get('error', 'Error desconocido')
                        print(f"\nError: {error} (Código: {respuesta.status_code})")

                    
                elif opcion == "2":
                    titulo = input("Título de la tarea: ")
                    descripcion = input("Descripción: ")
                    respuesta = session.post(f"{BASE_URL}/tareas", json={
                        "titulo": titulo, "descripcion": descripcion
                    })
                    resultado = respuesta.json()
                    print(resultado.get('mensaje') or resultado.get('error'))
                    

                elif opcion == "3":
                    respuesta = session.post(f"{BASE_URL}/logout")
                    print(respuesta.json().get('mensaje') or respuesta.json().get('error'))
                    # Limpiar cookies y cambiar estado
                    session.cookies.clear()
                    autenticado = False
                    print("La Sesión fue cerrada")

                    
                else:
                    print("Opción inválida")


    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario")
        # Cerrar sesión si estaba autenticado
        if autenticado:
            try:
                session.post(f"{BASE_URL}/logout")
                print("Sesión cerrada automáticamente")
            except:
                print("No se pudo cerrar sesión en el servidor")                    
    except requests.exceptions.ConnectionError:
        print("\nError: No se pudo conectar al servidor. ¿Está ejecutándose?")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")



if __name__ == "__main__":
    main()
