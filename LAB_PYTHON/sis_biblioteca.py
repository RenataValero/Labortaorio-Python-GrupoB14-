"""
Sistema de gestión de biblioteca - Escenario 7
Trabajo Final Integrador Python
"""

import os
from datetime import datetime

ARCHIVO_USUARIOS = "usuarios.txt"
ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"

usuarios = {}
libros = {}
prestamos = {}
# Inicialización del proyecto - commit 1

# ------------------ Funciones de persistencia ------------------


def cargar_datos():
    """Carga usuarios, libros y préstamos desde archivos .txt."""
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as f:
            for linea in f:
                dni, nombre = linea.strip().split(";")
                usuarios[dni] = {"nombre": nombre}

    if os.path.exists(ARCHIVO_LIBROS):
        with open(ARCHIVO_LIBROS, "r", encoding="utf-8") as f:
            for linea in f:
                # Se asegura el correcto espaciado pos-coma
                codigo, titulo, disponible, prestamos_count = (
                    linea.strip().split(";")
                )
                libros[codigo] = {
                    "titulo": titulo,
                    "disponible": disponible == "True",
                    "prestamos": int(prestamos_count),
                }

    if os.path.exists(ARCHIVO_PRESTAMOS):
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
            for linea in f:
                dni, codigo, fecha = linea.strip().split(";")
                if dni not in prestamos:
                    prestamos[dni] = []
                prestamos[dni].append({
                    "codigo": codigo,
                    "fecha": fecha
                })


def guardar_datos():
    """Guarda usuarios, libros y préstamos en archivos .txt."""
    with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as f:
        for dni, datos in usuarios.items():
            f.write(f"{dni};{datos['nombre']}\n")

    with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as f:
        for codigo, datos in libros.items():
            f.write(
                f"{codigo};{datos['titulo']};{datos['disponible']};"
                f"{datos['prestamos']}\n"
            )

    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as f:
        for dni, lista in prestamos.items():
            for p in lista:
                f.write(f"{dni};{p['codigo']};{p['fecha']}\n")

# ----------------- Funciones del sistema -----------------


def registrar_usuario():
    """Registra un nuevo usuario en el sistema."""
    dni = input("Ingrese DNI: ")
    nombre = input("Ingrese nombre: ")
    if dni in usuarios:
        print("⚠️ Usuario ya registrado.")
    else:
        usuarios[dni] = {"nombre": nombre}
        print("✅ Usuario registrado.")
        guardar_datos()


def registrar_libro():
    """Registra un nuevo libro en el sistema."""
    codigo = input("Ingrese código del libro: ")
    titulo = input("Ingrese título del libro: ")
    if codigo in libros:
        print("⚠️ Libro ya registrado.")
    else:
        libros[codigo] = {
            "titulo": titulo,
            "disponible": True,
            "prestamos": 0,
        }
        print("✅ Libro registrado.")
        guardar_datos()


def registrar_prestamo():
    """Registra un préstamo de un libro a un usuario."""
    dni = input("Ingrese DNI del usuario: ")
    codigo = input("Ingrese código del libro: ")

    if dni not in usuarios:
        print("⚠️ Usuario no registrado.")
        return

    if codigo not in libros:
        print("⚠️ Libro no registrado.")
        return

    if not libros[codigo]["disponible"]:
        print("⚠️ Libro no disponible.")
        return

    # Registrar préstamo
    libros[codigo]["disponible"] = False
    libros[codigo]["prestamos"] += 1

    if dni not in prestamos:
        prestamos[dni] = []

    prestamos[dni].append({
        "codigo": codigo,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    })

    print("✅ Préstamo registrado.")
    guardar_datos()


def devolver_libro():
    """Registra la devolución de un libro y calcula multa si corresponde."""
    dni = input("Ingrese DNI del usuario: ")
    codigo = input("Ingrese código del libro: ")

    if dni not in prestamos:
        print("⚠️ El usuario no tiene préstamos registrados.")
        return

    # Buscar el préstamo correspondiente
    prestamo_encontrado = None
    for p in prestamos[dni]:
        if p["codigo"] == codigo:
            prestamo_encontrado = p
            break

    if not prestamo_encontrado:
        print("⚠️ Ese libro no figura como prestado a este usuario.")
        return

    # Calcular días de préstamo
    fecha_prestamo = (
        datetime.strptime(prestamo_encontrado["fecha"], "%Y-%m-%d")
    )
    fecha_devolucion = datetime.now()
    dias_transcurridos = (fecha_devolucion - fecha_prestamo).days

    # Definir política de multa (ejemplo: más de 7 días)
    if dias_transcurridos > 7:
        multa = (dias_transcurridos - 7) * 10  # $10 por día extra
        print(f"⚠️ Devolución tardía. Multa: ${multa}")
    else:
        print("✅ Devolución en tiempo. No hay multa.")

    # Actualizar estado del libro
    libros[codigo]["disponible"] = True

    # Eliminar el préstamo de la lista del usuario
    prestamos[dni].remove(prestamo_encontrado)
    if not prestamos[dni]:
        del prestamos[dni]  # si ya no tiene préstamos, borramos la clave

    guardar_datos()


def mostrar_estadisticas():
    """Muestra estadísticas generales del sistema de biblioteca."""
    total_usuarios = len(usuarios)
    total_libros = len(libros)
    total_prestamos = sum(len(lista) for lista in prestamos.values())

    # Libro más prestado
    libro_mas_prestado = None
    max_prestamos = -1
    for _, datos in libros.items():
        if datos["prestamos"] > max_prestamos:
            max_prestamos = datos["prestamos"]
            libro_mas_prestado = datos["titulo"]

    print("\n📊 Estadísticas de la biblioteca:")
    print(f"👥 Total de usuarios: {total_usuarios}")
    print(f"📚 Total de libros: {total_libros}")
    print(f"📖 Préstamos activos: {total_prestamos}")
    if libro_mas_prestado:
        print(
            f"⭐ Libro más prestado: {libro_mas_prestado} "
            f"({max_prestamos} veces)"
        )
