import requests
import getpass

BASE_URL = "http://localhost:5000"

def main():
    print("Cliente del Sistema de Gestión de Tareas")
    while True:
        print("\nOpciones:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver tareas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                usuario = input("Usuario: ")
                contraseña = getpass.getpass("Contraseña: ")
                respuesta = requests.post(f"{BASE_URL}/registro", json={"usuario": usuario, "contraseña": contraseña})
                print(respuesta.json().get('mensaje') or respuesta.json().get('error'))

            elif opcion == "2":
                usuario = input("Usuario: ")
                contraseña = getpass.getpass("Contraseña: ")
                respuesta = requests.post(f"{BASE_URL}/login", json={"usuario": usuario, "contraseña": contraseña})
                print(respuesta.json().get('mensaje') or respuesta.json().get('error'))

            elif opcion == "3":
                respuesta = requests.get(f"{BASE_URL}/tareas")
                print("\n--- Página de bienvenida ---")
                print(respuesta.text)
                
            elif opcion == "4":
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