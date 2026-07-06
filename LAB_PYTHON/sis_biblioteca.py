"""
Sistema de gestión de biblioteca - Escenario 7
Trabajo Final Integrador Python
"""

import datetime
import os

ARCHIVO_USUARIOS = "usuarios.txt"
ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"

usuarios = {}
libros = {}
prestamos = []
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
                codigo, dni, fecha = linea.strip().split(";")
                prestamos.append({
                    "codigo": codigo,
                    "dni": dni,
                    "fecha": datetime.datetime.strptime(
                        fecha, "%Y-%m-%d"
                    ).date(),
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
        for p in prestamos:
            f.write(f"{p['codigo']};{p['dni']};{p['fecha']}\n")

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
