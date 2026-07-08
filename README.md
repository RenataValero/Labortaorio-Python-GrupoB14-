# Trabajo Final Integrador Python

**Integrantes del Grupo:** Valero Trenque, Renata - Vargas, Joaquín Nicolás - Gómez, Ramiro Daniel - Giménez Jorge Santiago
**Comisión: K1.2**

## Sistema de Biblioteca
#### Descripción General del Sistema:

Este proyecto es un Sistema de Gestión de Biblioteca desarrollado en Python. Su objetivo es administrar una biblioteca pequeña mediante una interfaz de consola, permitiendo registrar usuarios, libros y préstamos, además de mantener la información almacenada entre ejecuciones.
El sistema no utiliza una base de datos como MySQL o SQLite. En su lugar, implementa un mecanismo de persistencia sencillo mediante archivos de texto (.txt), lo que lo hace adecuado para este proyecto educativo.

##### Arquitectura del Sistema

**El proyecto está dividido en dos módulos principales:**

**1.**<span style="color:blue"> menu_principal.py</span>
Este módulo representa la capa de presentación, su única responsabilidad es interactuar con el usuario:
- **muestra el menú principal;**
- **solicita la opción elegida;**
- **llama a la función correspondiente del sistema;**
- **mantiene el programa ejecutándose hasta que el usuario decida salir.**

No contiene la lógica del negocio. En términos de arquitectura, actúa como un controlador del flujo principal.

**2.**<span style="color:blue"> sis_biblioteca.py</span>
Este archivo concentra prácticamente toda la funcionalidad del proyecto. Aquí se encuentran:
- **la carga de los datos;**
- **el guardado de la información;**
- **el registro de usuarios;**
- **el registro de libros;**
- **los préstamos;**
- **las devoluciones;**
- **el cálculo de multas;**
- **las estadísticas.**

Es decir, constituye la capa lógica del sistema.

**El sistema trabaja completamente en memoria utilizando tres diccionarios globales:** <span style="color:red">usuarios, libros y préstamos</span>**.**

------------

#### Funcionalidades Implementadas:
El sistema permite cinco operaciones principales:

##### Registro de usuarios
Permite incorporar un nuevo usuario utilizando:
- **DNI**
- **Nombre**

Antes de agregarlo verifica que el DNI no exista.

##### Registro de libros
Permite registrar nuevos libros indicando:
- **código**
- **título**
Inicialmente todos los libros quedan disponibles.

##### Registro de préstamos
Para prestar un libro el sistema verifica:
- **que el usuario exista;**
- **que el libro exista;**
- **que el libro esté disponible.**

Si todas las condiciones se cumplen:
- **marca el libro como no disponible;**
- **incrementa el contador histórico de préstamos;**
- **registra la fecha actual;**
- **guarda el préstamo.**

##### Devolución
Cuando un libro es devuelto:
- **verifica que realmente esté prestado;**
- **calcula cuántos días pasaron desde el préstamo;**
- **si superó siete días aplica una multa de: $10 por cada día de atraso;**

Finalmente:
- **elimina el préstamo;**
- **vuelve a marcar el libro como disponible.**

##### Estadísticas
El sistema calcula:
- **cantidad total de usuarios;**
- **cantidad total de libros;**
- **préstamos activos;**
- **libro más prestado históricamente.**

Estas estadísticas se calculan dinámicamente utilizando la información almacenada en memoria.

------------

# Requisitos

Para ejecutar el sistema es necesario contar con:

- Python 3.10 o superior.
- Sistema operativo Windows, Linux o macOS.
- Consola de comandos (CMD, PowerShell, Terminal, etc.).

No es necesario instalar librerías externas, ya que el proyecto utiliza únicamente módulos estándar de Python.

---

## Instrucciones de Ejecución

#### 1. Descargar el proyecto

Clonar el repositorio desde GitHub o descargar el archivo ZIP y descomprimirlo.

---

#### 2. Acceder a la carpeta del proyecto

Abrir una terminal y dirigirse a la carpeta donde se encuentra el archivo `menu_principal.py`.

Ejemplo:

```bash
cd C:\Users\Usuario\Downloads\Labortaorio-Python-GrupoB14--main\LAB_PYTHON
```

---

#### 3. Ejecutar el programa

Ejecutar alguno de los siguientes comandos:

```bash
python menu_principal.py
```

o

```bash
py menu_principal.py
```

---

#### 4. Inicio del sistema

Al iniciarse correctamente, el sistema cargará automáticamente los archivos:

- `usuarios.txt`
- `libros.txt`
- `prestamos.txt`

Posteriormente se mostrará el menú principal para comenzar a utilizar la aplicación.

---

## Persistencia

Toda la información ingresada durante la ejecución del programa se almacena automáticamente en los archivos de texto del proyecto.

No es necesario realizar ninguna acción adicional para guardar los cambios.

---

## Posibles inconvenientes

- Si Python no se encuentra instalado o agregado al PATH del sistema operativo, los comandos `python` o `py` no serán reconocidos.

- No deben eliminarse ni modificarse manualmente los archivos:

  - `usuarios.txt`
  - `libros.txt`
  - `prestamos.txt`

  ya que contienen la información utilizada por el sistema.

- Se recomienda ejecutar el programa desde la carpeta donde se encuentran dichos archivos para evitar errores de lectura o escritura.

---

## Características del Proyecto

- Desarrollado completamente en Python.
- Interfaz basada en consola.
- Persistencia mediante archivos de texto.
- Organización modular del código.
- Separación entre la interfaz y la lógica del sistema.
- No requiere base de datos.
- No requiere instalación de dependencias externas.

---
