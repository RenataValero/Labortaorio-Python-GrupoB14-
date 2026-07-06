"""
Módulo menu_principal.py
Este archivo contiene el menú principal del sistema de biblioteca.
Permite al usuario registrar usuarios, libros, préstamos, devoluciones
y consultar estadísticas desde una interfaz interactiva en consola.
"""

from sis_biblioteca import (
    registrar_usuario,
    registrar_libro,
    registrar_prestamo,
    devolver_libro,
    mostrar_estadisticas,
    cargar_datos,
)


def menu_principal():
    """Menú principal del sistema de biblioteca."""
    cargar_datos()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar usuario")
        print("2. Registrar libro")
        print("3. Registrar préstamo")
        print("4. Devolver libro")
        print("5. Ver estadísticas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_libro()
        elif opcion == "3":
            registrar_prestamo()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
