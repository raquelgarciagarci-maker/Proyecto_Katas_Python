# Katas de Python

Conjunto de 40 ejercicios que repasan los fundamentos de Python: funciones, estructuras de datos, programación funcional, recursividad, manejo de excepciones y programación orientada a objetos. Todas las soluciones se encuentran en el archivo [`Proyecto_Katas_Python.py`](./Proyecto_Katas_Python.py), ordenadas según la numeración del enunciado.

## Contenidos trabajados

- Variables, tipos de datos y estructuras: listas, tuplas, diccionarios y conjuntos (`set`).
- Funciones, parámetros opcionales, `*args` y funciones `lambda`.
- Programación funcional con `map()`, `filter()` y `reduce()`.
- Recursividad (factorial).
- Condicionales (`if / elif / else`) y validación de datos de entrada.
- Manejo de excepciones: `try / except / else`, `raise` y excepciones personalizadas.
- Clases y objetos: atributos, métodos y relación entre objetos.
- Operaciones con cadenas: *slicing*, `split()`, `join()`, `replace()` y f-strings.

## Requisitos

- Python 3.6 o superior (por el uso de f-strings).
- No se necesita instalar ninguna librería externa. Solo se utilizan `functools` y `math`, que vienen incluidas con Python.

## Ejecución

1. Instalar Python 3.6 o superior, si no lo está ya (descarga en [python.org](https://www.python.org/downloads/)). Para comprobarlo, basta con ejecutar `python --version` en una terminal.
2. Descargar el proyecto desde GitHub, con el botón *Code → Download ZIP* (y descomprimir la carpeta), o bien clonando el repositorio:

```bash
git clone https://github.com/raquelgarciagarci-maker/Proyecto_Katas_Python.git
```

3. Abrir una terminal en la carpeta del proyecto, que es la que contiene el archivo `Proyecto_Katas_Python.py`.
4. Ejecutar el programa (en algunos sistemas el comando es `python3`):

```bash
python Proyecto_Katas_Python.py
```

También es posible abrir el archivo en un editor como Visual Studio Code y ejecutarlo desde allí.

El programa se ejecuta de principio a fin, en el orden de los ejercicios, y muestra cada resultado por pantalla.

### Ejercicios que solicitan datos por teclado

Seis ejercicios utilizan `input()`, por lo que el programa se detendrá a esperar una respuesta en cada uno de ellos. Como referencia, estos valores recorren el camino habitual de cada ejercicio:

| Ejercicio | Qué solicita | Valores de ejemplo |
|---|---|---|
| 8 | Dos números para dividirlos | `10` y `2` |
| 11 | Edad | `30` |
| 31 | Lista de nombres y nombre a buscar | `Ana, Luis, Marta` y `Luis` |
| 37 | Hora en formato `hh:mm` | `15:30` |
| 38 | Calificación numérica (0-100) | `85` |
| 40 | Precio, cupón (sí/no) e importe del cupón | `50`, `sí` y `15` |

Los demás ejercicios no requieren ninguna intervención: incluyen sus propios datos de prueba y su `print()` correspondiente.

## Índice de ejercicios

| N.º | Descripción | Conceptos principales |
|---|---|---|
| 1 | Frecuencia de cada letra de un texto, sin contar espacios | Diccionarios, `get()` |
| 2 | Doble de cada valor de una lista | `map()` |
| 3 | Palabras que contienen una palabra objetivo | Bucle `for`, operador `in` |
| 4 | Diferencia entre los valores de dos listas | `map()`, `lambda` |
| 5 | Media de notas y estado (aprobado/suspenso) | Parámetro opcional, tuplas |
| 6 | Factorial de un número | Recursividad |
| 7 | Conversión de una lista de tuplas a strings | `map()`, `str()` |
| 8 | División de dos números con control de errores | `try / except / else` |
| 9 | Exclusión de mascotas prohibidas en España | `filter()` |
| 10 | Promedio con excepción si la lista está vacía | Excepción personalizada, `raise` |
| 11 | Edad con validación de valor y rango | `raise ValueError` |
| 12 | Longitud de cada palabra de una frase | `map()`, `len()` |
| 13 | Tuplas (mayúscula, minúscula) sin letras repetidas | `set`, `map()` |
| 14 | Palabras que empiezan por una letra concreta | `filter()`, `startswith()` |
| 15 | Suma de 3 a cada número de una lista | `lambda`, `map()` |
| 16 | Palabras más largas que `n` | `filter()` |
| 17 | Conversión de una lista de dígitos en un número | `reduce()` |
| 18 | Estudiantes con calificación mayor o igual a 90 | Lista de diccionarios, `filter()` |
| 19 | Números impares de una lista | `lambda`, `filter()` |
| 20 | Valores de tipo `int` de una lista mixta | `filter()`, `type()` |
| 21 | Cubo de un número | `lambda` |
| 22 | Producto de todos los valores de una lista | `reduce()` |
| 23 | Concatenación de una lista de palabras | `reduce()` |
| 24 | Diferencia total de los valores de una lista | `reduce()` |
| 25 | Número de caracteres de una cadena | `len()` |
| 26 | Resto de la división de dos números | `lambda`, operador `%` |
| 27 | Promedio de una lista de números | `sum()`, `len()` |
| 28 | Primer elemento duplicado de una lista | `set` |
| 29 | Enmascarado de un valor, dejando los últimos cuatro caracteres | *Slicing* |
| 30 | Comprobación de anagramas | `sorted()` |
| 31 | Búsqueda de un nombre en una lista introducida por el usuario | `input()`, excepciones |
| 32 | Puesto de un empleado a partir de su nombre | Lista de diccionarios |
| 33 | Suma de elementos correspondientes de dos listas | `lambda`, `map()` |
| 34 | Clase `Arbol` con tronco y ramas | Clases, métodos, listas |
| 35 | Clase `UsuarioBanco` con retirada, transferencia e ingreso | Clases, excepciones |
| 36 | Procesado de texto: contar, reemplazar y eliminar palabras | Funciones, `*args` |
| 37 | Momento del día según la hora (`hh:mm`) | Condicionales, excepciones |
| 38 | Calificación en texto según la nota numérica | Condicionales |
| 39 | Área de un rectángulo, círculo o triángulo | Desempaquetado de tuplas, `math` |
| 40 | Precio final de una compra con cupón de descuento | Condicionales, validación |

## Notas

- La numeración del enunciado original salta del 34 al 36. En este proyecto se ha unificado para que los ejercicios queden numerados del 1 al 40.
- Las funciones están documentadas con *docstrings* en formato Google (`Args`, `Returns` y `Raises`).
- El código sigue, en lo posible, las convenciones de estilo de PEP 8.

## Autoría

Raquel García García - [LinkedIn](https://linkedin.com/in/raquel-g-a64784159)
