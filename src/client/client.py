import requests
import getpass

BASE_URL = "http://localhost:5000"
session = requests.Session()  # Mantener sesión entre peticiones



def mostrar_cookies():
    """Función para depuración: muestra las cookies actuales"""
    cookies = session.cookies.get_dict()
    print(f"Cookies actuales: {cookies}")



def main():
    print("Cliente del Sistema de Gestión de Tareas")
    while True:
        print("\nOpciones:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver tareas")
        print("4. Agregar tarea")
        print("5. Cerrar sesión")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                usuario = input("Usuario: ")
                contraseña = getpass.getpass("Contraseña: ")
                respuesta = session.post(f"{BASE_URL}/registro", json={"usuario": usuario, "contraseña": contraseña})
                print(respuesta.json().get('mensaje') or respuesta.json().get('error'))

            elif opcion == "2":
                usuario = input("Usuario: ")
                contraseña = getpass.getpass("Contraseña: ")
                # Limpiar sesión previa
                session.cookies.clear()  

                respuesta = session.post(f"{BASE_URL}/login", json={"usuario": usuario, "contraseña": contraseña})
                resultado = respuesta.json()
                print(resultado.get('mensaje') or resultado.get('error'))
                mostrar_cookies()  # Verifica las cookies después de login
                
                # Si el login fue exitoso, la cookie ahora estará en 'session.cookies'
                if respuesta.status_code == 200:
                    mostrar_cookies()

            elif opcion == "3":
                mostrar_cookies()  # Verifica las cookies antes de pedir tareas
                respuesta = session.get(f"{BASE_URL}/tareas")
                if respuesta.status_code == 200:
                    print("\n--- Tus tareas ---")
                    print(respuesta.text)
                else:
                    error = respuesta.json().get('error', 'Error desconocido')
                    print(f"\nError: {error} (Código: {respuesta.status_code})")

            elif opcion == "4":  
                titulo = input("Título: ")
                descripcion = input("Descripción: ")
                respuesta = session.post(f"{BASE_URL}/tareas", json={
                    "titulo": titulo,
                    "descripcion": descripcion
                })
                print(respuesta.json().get('mensaje') or respuesta.json().get('error'))

            elif opcion == "5":
                respuesta = session.post(f"{BASE_URL}/logout")
                print(respuesta.json().get('mensaje') or respuesta.json().get('error'))
                # Limpiar cookies al cerrar sesión
                session.cookies.clear()
                
            elif opcion == "6":
                print("Saliendo...")
                break

            else:
                print("Opción inválida")
                
        except requests.exceptions.ConnectionError:
            print("\nError: No se pudo conectar al servidor. ¿Está ejecutándose?")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario")
            break
        except Exception as e:
            print(f"\nError inesperado: {str(e)}")

if __name__ == "__main__":
    main()