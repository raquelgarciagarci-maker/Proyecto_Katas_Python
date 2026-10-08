from functools import reduce # importamos la función reduce para poder utilizarla más adelante en el código.
import math

# NOTA: los ejercicios 8, 11, 31, 37, 38 y 40 tienen inputs, por lo que solicitarán al usuario que introduzca datos con el teclado.

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_letras(texto):
    """
    Cuenta la frecuencia de cada letra, ignorando los espacios
    Args:
        texto (str): cadena de texto que vamos a analizar
    Returns:
        dict: diccionario de cada letra y su frecuencia
    """
    dict_frecuencias = {} #diccionario vacío donde iremos guardando los resultados
    for letra in texto:
        if letra != " ":  #ignoramos los espacios
            dict_frecuencias[letra] = dict_frecuencias.get(letra, 0) +1   # con get conseguimos que nos dé el valor de cada letra y si no existe la letra, nos devuelva cero, evitando errores
    return dict_frecuencias

resultado = frecuencia_letras("Proyecto Katas Python")
print(resultado)


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def doble(x):
    """
    Calcularemos el doble de cada valor
    
    Args:
        x (int, float):  un número individual

    Returns:
        (int, float): el doble del número recibido.
    """
    return x * 2

lista = [1, 4, 9, 17, 182]
resultado = map(doble, lista)
print(list(resultado))


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def lista_objetivo(lista, objetivo):
    """
    Busca las palabras de una lista que contienen una palabra objetivo.

    Args:
        lista (list): lista de palabras a revisar.
        objetivo (str): palabra que buscamos dentro de cada palabra de la lista.

     Returns:
        list: lista con las palabras que contienen el objetivo.
    """
    resultado = []
    for palabra in lista:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado


lista_palabras = ["cacerola", "cuchillo", "tenedor", "colador", "sartén", "caracola"]
resultado = lista_objetivo(lista_palabras, "col")
print(resultado)


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia(lista1, lista2): 
    """
    Calcula la diferencia (resta) entre los valores de dos listas, elemento a elemento.

    Args:
        lista1 (list): primera lista de números.
        lista2 (list): segunda lista de números.

    Returns:
        list: lista con la diferencia entre listas para cada posición.
     """
    resultado = list(map(lambda x, y: x - y, lista1, lista2))
    return resultado

num_1 = [2, 29, 15, 667, 88]
num_2 = [15, 42, 89, 114, 667]
print(diferencia(num_1, num_2))


# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluacion(lista_notas, nota_aprobado=5):  #incluimos el valor por defecto para nota_aprobado, que será 5
    """
    Calcula la media y si esta es mayor o igual a un valor específico para darle entonces un estado.

    Args:
        lista_notas (list): lista de números.
        nota_aprobado (int, float): Es un valor de referencia, que en este caso es por defecto 5.

    Returns:
        tuple: la media y el estado como una tupla (media, estado)
    """
    media = sum(lista_notas)/len(lista_notas)
    
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (media, estado)

notas = [2.5, 9.75, 3.4, 6.7, 5.1, 4.8]
print(evaluacion(notas))


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(x):
    """
    Calcula el factorial de un número de manera recursiva

    Args:
        x (int, float): número
    
    Returns:
        int, float: número resultando de calcular el factorial de otro número de manera recursiva. 
    """
    if x<=1:   #caso base con el que paramos la función
        return 1
    else:
        return x*factorial(x-1)

print(factorial(5))


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tupla_a_string(tupla):
    """
    Convierte una tupla en su representación como string dentro de una lista.

    Args:
        tupla (tuple): una tupla individual.

    Returns:
        str: la tupla convertida a string.
    """
    return str(tupla)


lista_tuplas = [("Juan", 37), ("Raquel", 42), ("Chus", 51), ("Susana", 44)]
resultado = list(map(tupla_a_string, lista_tuplas))
print(resultado)


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:
    num1 = int(input("Indique un número: ")) # Solicitamos al usuario que indique un número y lo convertimos a entero.
    num2 = int(input("Indique otro número: ")) # Solicitamos al usuario que indique otro número y lo convertimos a entero.
    print("Los números elegidos por el usuario son:", num1, "y", num2) # Mostramos los números indicados por el usuario.
    resultado = num1/num2 # Dividimos el primer número indicado por el usuario entre el segundo.
except ValueError: # Capturamos el error en caso de que el usuario ingrese un valor no válido (por ejemplo, una letra).
    print("Debe indicar un número válido.")
except ZeroDivisionError: # Capturamos el error en caso de que el usuario ingrese 0 como divisor, lo cual es inválido.
    print("No se puede dividir entre cero.")
else:
    print("El resultado de la división es:", round(resultado, 2)) # Si el try tiene éxito, mostramos el resultado de la división, la cual redondearemos a dos decimales. 
 
 
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista):
    """
    Filtraremos las mascotas que sí están permitidas, excluyendo las que no lo están y las devolveremos en una lista.

    Args:
        lista (list): lista de mascotas

    Returns: 
        list: lista de mascotas permitidas (no incluye las prohibidas).
    """
    mascotas_prohibidas =  ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    resultado = list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista))
    return resultado

mascotas = ["León", "Cacatúa", "Tigre", "Tortuga", "Serpiente", "Oso"]
print(filtrar_mascotas(mascotas))


# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    """
    Se trata de una excepción personalizada para el caso de una lista vacía
    """
    pass

def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.

    Args:
        lista (list): lista de números.

    Returns:
        float: el promedio de los números de la lista.

    Raises:
        ListaVaciaError: si la lista está vacía.
    """
    if len(lista)==0:
        raise ListaVaciaError("La lista está vacía y no se puede calcular el promedio") # lanzamos nuestra excepción personalizada si la lista está vacía.
    return sum(lista)/len(lista)

try:
    numeros = [2,0,8]
    resultado = round(calcular_promedio(numeros), 2)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as error:
    print(f"Error: {error}")


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.

try:
    edad = int(input("Indique su edad:"))  # Solicitamos al usuario que indique su edad y la convertimos a entero.
    if edad < 0 or edad > 120:  # Comprobamos si la edad indicada por el usuario está fuera del rango esperado.
        raise ValueError("La edad debe estar entre 0 y 120.") # Si la edad está fuera del rango, lanzamos una excepción ValueError con un mensaje personalizado.
    print(f"Su edad es: {edad}") # Si la edad está dentro del rango, mostramos la edad indicada por el usuario.
except ValueError as error: # Capturamos el error en caso de que el usuario ingrese un valor no válido (por ejemplo, una letra o un número fuera del rango).
    print(f"Error: {error}")


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    """
    Calcula la longitud de cada palabra de una frase.

    Args:
        frase (str): Cadena de texto que vamos a analizar.

    Returns:
        list: Lista con la longitud de cada palabra.
    """
    palabras = frase.split(" ") # Dividimos la frase en palabras usando el espacio como separador.
    resultado = list(map(len, palabras)) # Calculamos la longitud de cada palabra usando la función map() y la función len().
    return resultado

print(longitud_palabras("Python me da dolor de cabeza"))


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(texto):
    """
    Genera una lista de tuplas con cada letra en mayúsculas y minúsculas de un texto sin repetidos.

    Args:
        texto (str): Cadena de texto que vamos a analizar.

    Returns:
        list: Lista de tuplas con cada letra en mayúsculas y minúsculas sin repetir.
    """
    letras_unicas = set(texto.lower().replace(" ", ""))  # Eliminamos espacios y pasamos a minúsculas para evitar duplicados.
    resultado = list(map(lambda x: (x.upper(), x.lower()), letras_unicas))
    return resultado


print(letras_mayus_minus("Python Sigue Siendo Un Dolor De Cabeza"))


# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrar_por_letra(lista, letra):
    """
    Filtra las palabras de una lista que comienzan con una letra específica.

    Args:
        lista (list): Lista de palabras a revisar.
        letra (str): Letra con la que deben comenzar las palabras.

    Returns:
        list: Lista con las palabras que comienzan con la letra especificada.
    """
    resultado = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista)) # Usamos lower() para hacer la comparación insensible a mayúsculas/minúsculas.
    return resultado


palabras = ["patatas", "cacahuetes", "pistachos", "aceitunas", "pipas", "anacardos"]
print(filtrar_por_letra(palabras, "p"))


# 15. Crea una función lambda que  sume 3 a cada número de una lista dada.

lista_numeros = [20, 105, 2, 85, 99]
suma_tres = map(lambda x: x+3, lista_numeros) # Aplicamos la función lambda a cada elemento de la lista gracias a map()
print(list(suma_tres))


# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas_que(texto, n):
    """
    Devuelve una lista de palabras que son más largas que un número dado.

    Args:
        texto (str): Cadena de texto que vamos a analizar.
        n (int): Longitud mínima que deben tener las palabras.

    Returns:
        list: Lista con las palabras que son más largas que n.
    """
    palabras = texto.split(" ") # Dividimos la cadena de texto en palabras usando el espacio como separador.
    resultado = list(filter(lambda palabra: len(palabra) > n, palabras))
    return resultado


print(palabras_mas_largas_que("A mi perro le encantaba jugar con la pelota", 4))


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

#no es necesario incluir la función reduce() en el código, ya que la hemos importado al principio del archivo.

def digitos_a_numero(lista_digitos):
    """
    Calcula el número correspondiente a una lista de dígitos.

    Args:
        lista_digitos (list): lista de dígitos que vamos a convertir en un número.

    Returns:
        int: el número correspondiente a la lista de dígitos.
    """
    resultado = reduce(lambda acumulado, actual: acumulado * 10 + actual, lista_digitos) # Usamos reduce() para ir acumulando el resultado, multiplicando el acumulado por 10 y sumando el dígito actual.
    return resultado

print(digitos_a_numero([5, 7, 2]))
print(digitos_a_numero([1, 8, 4, 6,]))


# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter

estudiantes = [
    {"nombre": "Luis", "edad": 26, "calificacion": 86},
    {"nombre": "Leire", "edad": 35, "calificacion": 92},
    {"nombre": "Alberto", "edad": 24, "calificacion": 54},
    {"nombre": "Lucía", "edad": 42, "calificacion": 98}
]
aprobados_alto = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)) # Usamos la función filter() para filtrar los estudiantes con calificación mayor o igual a 90, usando una función lambda que verifica la calificación de cada estudiante.
print(aprobados_alto)


# 19. Crea una función lambda que filtre los números impares de una lista dada.
lista_numeros = [4, 268, 451, 79, 66, 333254]
impares = list(filter(lambda x: x % 2 != 0, lista_numeros)) # Usamos la función filter() para filtrar los números impares de la lista, usando una función lambda que verifica si cada número es impar.
print(impares)


#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista_elementos = [82, "Python", "dolor", 1000, "cabeza", 4.869, 2]
enteros = list(filter(lambda elemento: type(elemento) == int, lista_elementos)) # Usamos la función filter() para filtrar los elementos de la lista que son de tipo int, usando una función lambda que verifica el tipo de cada elemento.
print(enteros)


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3
print(cubo(3))


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

def producto_valores(lista_valores):
    """
    Calcula el producto de todos los valores de una lista.

    Args:
        lista_valores (list): lista de números.

    Returns:
        int, float: el producto de todos los valores de la lista.
    """
    resultado = reduce(lambda acumulado, actual: acumulado * actual, lista_valores) # Usamos reduce() para ir acumulando el resultado, multiplicando el acumulado por el valor actual.
    return resultado

print(producto_valores([2, 3, 6]))


# 23. Concatena una lista de palabras.Usa la función reduce() .

def concatenar_palabras(lista_palabras):
    """
    Concatena todas las palabras de una lista en una sola cadena de texto.

    Args:
        lista_palabras (list): lista de palabras.

    Returns:
        str: cadena de texto resultante de concatenar todas las palabras.
    """
    resultado = reduce(lambda acumulado, actual: acumulado + " " + actual, lista_palabras) # Usamos reduce() para ir acumulando el resultado, concatenando el acumulado con la palabra actual, separadas por un espacio.
    return resultado

palabras = ["Mi", "perro", "se", "llamaba", "Ludo"]
print(concatenar_palabras(palabras))


# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

def resta_valores(lista_valores):
    """
    Calcula la resta de todos los valores de una lista, restando el valor actual al acumulado.

    Args:
        lista_valores (list): lista de números.

    Returns:
        int, float: la resta de todos los valores de la lista.
    """
    resultado = reduce(lambda acumulado, actual: acumulado - actual, lista_valores) # Usamos reduce() para ir acumulando el resultado, restando el valor actual al acumulado.
    return resultado

print(resta_valores([60, 8, 2]))


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena_texto):
    """
    Cuenta el número de caracteres en una cadena de texto.

    Args:
        cadena_texto (str): cadena de texto que vamos a analizar.

    Returns:
        int: número de caracteres en la cadena de texto.
    """
    return len(cadena_texto)

print(contar_caracteres("Hoy ha llovido durante todo el día y me he quedado en casa estudiando Python."))


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y
print(resto(20, 6)) 


# 27. Crea una función que calcule el promedio de una lista de números.

def promedio_lista(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros (list): lista de números

    Returns:
        float: el promedio de los números en la lista.
    """
    return sum(lista_numeros)/len(lista_numeros)


print(promedio_lista([4, 8, 15, 16, 23, 42]))


# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    """
    Busca y devuelve el primer elemento duplicado en una lista.

    Args:
        lista (list): lista de elementos a revisar.

    Returns:
        str: un mensaje indicando cuál es el primer elemento duplicado, o que no hay duplicados.
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return f"El elemento {elemento} está duplicado"
        else:
            vistos.add(elemento)
    return "No hay elementos duplicados"   # si no hay ningún duplicado


print(primer_duplicado([2, 5, 8, 5, 3, 8]))   
print(primer_duplicado([6, 9, 32, 45]))  


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

def enmascarar(valor):
    """
    Convierte una variable en una cadena de texto y enmascara todos los caracteres con el carácter '#', excepto los últimos cuatro.

    Args:
        valor (any): variable que vamos a convertir en cadena de texto y enmascarar.
    
    Returns:
        str: cadena de texto enmascarada.
    """
    
    texto = str(valor) # convertimos la variable en una cadena de texto
    parte_a_enmascarar = texto[:-4] # obtenemos todos los caracteres excepto los últimos cuatro
    ultimos_cuatro = texto[-4:] # obtenemos los últimos cuatro caracteres
    mascara = "#" * len(parte_a_enmascarar) # creamos la máscara con el mismo número de caracteres que la parte a enmascarar
    return mascara + ultimos_cuatro 

print(enmascarar(448255136547))


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """
    Comprueba si dos palabras son anagramas entre sí.

    Args:
        palabra1 (str): primera palabra a comparar.
        palabra2 (str): segunda palabra a comparar.

    Returns:
        bool: True si son anagramas, False en caso contrario.
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower()) # Comparamos las palabras ordenadas alfabéticamente y en minúsculas para ignorar mayúsculas/minúsculas.

print(son_anagramas("ROSA", "raso"))


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    """
    Solicita al usuario una lista de nombres y un nombre a buscar, e indica si se encuentra en la lista.

    El usuario introduce los nombres separados por comas, y después un nombre concreto a localizar.
    Si el nombre está en la lista, se imprime un mensaje de confirmación. 
    Si no está, se lanza una excepción con un mensaje indicando que no se ha encontrado.
    La búsqueda no distingue entre mayúsculas y minúsculas.

    Raises:
        ValueError: si el nombre buscado no se encuentra en la lista introducida.
    """
    texto = input("Introduce varios nombres separados por comas: ").lower() # Solicitamos al usuario que indique varios nombres separados por comas y los guardamos en una variable, incluyendo lower() para transformarlos a minúsculas.
    nombres = [nombre.strip() for nombre in texto.split(",")] # Dividimos la cadena de texto en una lista de nombres usando la coma como separador y eliminamos los espacios en blanco al principio y al final de cada nombre.

    nombre_buscado = input("Indique el nombre que desea buscar en la lista: ").strip() # Solicitamos al usuario que indique un nombre a buscar en la lista y eliminamos los espacios en blanco al principio y al final del nombre con strip().

    if nombre_buscado.lower() in nombres: # Comprobamos si el nombre indicado por el usuario está en la lista usando lower() para transformarlo a minúsculas como hicimos con el texto.
        print(f"El nombre '{nombre_buscado}' fue encontrado en la lista.")
    else:
        raise ValueError(f"'{nombre_buscado}' no está en la lista.") # Si el nombre no está en la lista, lanzamos una excepción ValueError con un mensaje personalizado.

try:
    buscar_nombre() # Llamamos a la función buscar_nombre() para ejecutar el programa.
except ValueError as error:
    print(f"Error: {error}") # Si se lanza una excepción ValueError, capturamos el error y mostramos el mensaje de error correspondiente.



# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def puesto_empleado(lista_empleados, nombre_empleado):
    """
    Busca un empleado en una lista de empleados y devuelve su puesto o un mensaje en el caso de que no se encuentre en la lista.

    Args:
        lista_empleados (list): lista de diccionarios con información de empleados.
        nombre_empleado (str): nombre del empleado a buscar.

    Returns:
        str: el puesto del empleado si se encuentra, o un mensaje indicando que no se encontró.
    """
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_empleado:
            return f'El puesto de {nombre_empleado} es: {empleado["puesto"]}'
    return f'El empleado {nombre_empleado} no trabaja aquí.'

empleados = [{"nombre": "Luis", "puesto": "Analista de datos"}, {"nombre": "Arturo", "puesto": "Científico de datos"}, {"nombre": "Eva", "puesto": "Ingeniera de datos"}]
print(puesto_empleado(empleados, "Pedro"))


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [2, 4, 6, 8]
lista2 = [1, 3, 5, 7]
suma_listas = list(map(lambda x, y: x + y, lista1, lista2)) # Usamos la función map() para sumar los elementos de dos listas, usando una función lambda que suma cada par de elementos correspondientes de las listas.
print(suma_listas)


# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    """
    Clase que representa un árbol con sus características básicas.
    """
    def __init__(self):  
        """
        Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        """
        self.tronco = 1  
        self.ramas = []
    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco del árbol en una unidad. 
        """
        self.tronco += 1
    def nueva_rama(self):
        """
        Agrega una nueva rama de longitud 1 a la lista de ramas.
        """
        self.ramas.append(1) 
    def crecer_ramas(self):
        """
        Aumenta en una unidad la longitud de todas las ramas existentes.
        """
        for i in range(len(self.ramas)):
            self.ramas[i] += 1  # usamos el índice para modificar cada rama dentro de la lista.
    def quitar_rama(self, posicion):
        """
        Elimina una rama en una posición específica.

        Args:
            posicion (int): índice de la rama a eliminar.
        """
        self.ramas.pop(posicion)
    def info_arbol(self):
        """
        Devuelve la información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
        """
        print(f"Tronco: {self.tronco}")
        print(f"Número de ramas: {len(self.ramas)}")
        print(f"Longitud de las ramas: {self.ramas}")

# Caso de uso
mi_arbol = Arbol()                   # 1. Crear un árbol.
mi_arbol.crecer_tronco()       # 2. Hacer crecer el tronco del árbol una unidad.
mi_arbol.nueva_rama()          # 3. Añadir una nueva rama al árbol.
mi_arbol.crecer_ramas()        # 4. Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.nueva_rama()          # 5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)        # 6. Retirar la rama situada en la posición 2.
mi_arbol.info_arbol()              # 7. Obtener información sobre el árbol.


# 35. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    """
    Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
    """ 
    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Inicializa un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    def retirar_dinero(self, retirada_saldo):
        """
        Permite al usuario retirar dinero de su saldo si tiene suficiente saldo disponible.

        Args:
            retirada_saldo (float): cantidad de dinero a retirar.
        
        Raises: 
            ValueError: si el saldo es insuficiente para la retirada.
        """
        if retirada_saldo > self.saldo:
            raise ValueError(f'{self.nombre} no tiene suficiente saldo para retirar {retirada_saldo}. Saldo disponible: {self.saldo}')
        self.saldo -= retirada_saldo
        print(f'{self.nombre} ha retirado {retirada_saldo}. Saldo restante: {self.saldo}')
    
    def transferir_dinero(self, otro_usuario, cantidad):
        """
         Permite realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.

         Args:
            otro_usuario (UsuarioBanco): Usuario que envía el dinero.
            cantidad (float): Cantidad de dinero a transferir.
        
        Raises:
            ValueError: si el saldo del otro_usuario es insuficiente para la transferencia.
         """
        if cantidad > otro_usuario.saldo: # comprobamos el saldo antes de mover dinero; si no es suficiente, lanzamos el error.
            raise ValueError(f'{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}. Saldo disponible: {otro_usuario.saldo}')
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f'{self.nombre} ha recibido {cantidad} de {otro_usuario.nombre}. Saldo actual: {self.saldo}')

    def agregar_dinero(self, cantidad):
        """
        Permite agregar dinero al saldo del usuario.
        """
        self.saldo += cantidad
        print(f'{self.nombre} ha agregado {cantidad} a su saldo. Saldo actual: {self.saldo}')

# Caso de uso:
usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)

# Agregar 20 unidades de saldo de "Bob".
usuario2.agregar_dinero(20)    
# Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
try:
    usuario1.transferir_dinero(usuario2, 80)
except ValueError as error:
    print(f'Error: {error}')
# Retirar 50 unidades de saldo a "Alicia".    
usuario1.retirar_dinero(50) 


#36. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .

def contar_palabras(texto):
    """
    Cuenta el número de veces que aparece cada palabra en el texto y devuelve un diccionario
    
    Args:
        texto (str): texto que vamos a procesar.
    Returns:
        dict: diccionario de cada palabra con su frecuencia.
    """
    palabras = texto.split(" ")
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia: # si la palabra ya está en el diccionario
            frecuencia[palabra] += 1 # le sumamos 1
        else: # si la palabra no está en el diccionario
            frecuencia[palabra] = 1 # la añadimos con valor 1
    return frecuencia

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra por otra.
    
    Args:
        texto (str): texto que vamos a procesar.
        palabra_original (str): palabra que vamos a reemplazar.
        palabra_nueva (str): palabra por la que vamos a reemplazar la palabra original
    
    Returns:
        str: texto con el reemplazo de palabras.
    """
    return texto.replace(palabra_original, palabra_nueva) 

def eliminar_palabra(texto, palabra):
    """
    Elimina una palabra del texto.
    
    Args:
        texto (str): texto que vamos a procesar.
        palabra (str): palabra que vamos a eliminar del texto.
    
    Returns:
        str: texto sin la palabra eliminada y sin espacios dobles resultantes.
        """
    texto_sin_palabra = texto.replace(palabra, "") #eliminamos la palabra que queramos reemplazándola por una cadena vacía.
    return " ".join(texto_sin_palabra.split()) #split() separa el texto en palabras ignorando espacios múltiples; join() las vuelve a unir con un solo espacio, evitando los dobles espacios que deja el replace().
    
def procesar_texto(texto, opcion, *args):  
    """
    Procesa un texto según la opción indicada, llamando a la función correspondiente.

    Args:
        texto (str): texto que vamos a procesar.
        opcion (str): operación a realizar ("contar", "reemplazar" o "eliminar").
        *args: argumentos adicionales según la opción:
            - "reemplazar": palabra_original (str), palabra_nueva (str)
            - "eliminar": palabra (str)
            - "contar": no requiere argumentos adicionales

    Returns:
        dict or str: el resultado de la operación (diccionario si es "contar", texto si es "reemplazar" o "eliminar").

    Raises:
        ValueError: si la opción indicada no es reconocida.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(f"Opción '{opcion}' no reconocida.")


texto = "El perro está en la orilla del río con un palo en la boca"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "perro", "lobo"))
print(procesar_texto(texto, "eliminar", "en la boca"))


# 37. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

try:
    texto_hora = input("Indica qué hora es (formato hh:mm): ")
    partes = texto_hora.split(":") # dividimos la hora en dos partes (horas y minutos) utilizando ':' como separador
    hora = int(partes[0])  #convertimos de texto a número 
    minutos = int(partes[1]) 

    if not (hora >= 0 and hora <= 23 and minutos >= 0 and minutos <= 59):
        print("Hora no válida.")
    elif hora >= 0 and hora <= 6 or hora >= 21 and hora <=23:
        print("Es de noche")
    elif hora >= 7 and hora <= 13:
        print("Es de día")
    elif hora >= 14 and hora <= 20:
        print("Es de tarde")

except ValueError:
    print("Formato no válido. Usa hh:mm, por ejemplo 15:30.")  #Si el usuario indica algo que no es un número, por ejemplo una letra.
except IndexError:
    print("Formato no válido. Asegúrate de incluir los dos puntos, ej: 16:00.") #Si el usuario indica una hora sin el separador de los dos puntos


# 38. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
    # 0 - 69 insuficiente
    # 70 - 79 bien
    # 80 - 89 muy bien
    # 90 -100 excelente

try:
    calificacion = int(input("Indica tu calificación (0-100): "))

    if not (calificacion >= 0 and calificacion <= 100):
        print("Calificación no válida.")
    elif calificacion >= 0 and calificacion <= 69:
        print("Insuficiente")
    elif calificacion >= 70 and calificacion <= 79:
        print("Bien")
    elif calificacion >= 80 and calificacion <= 89:
        print("Muy bien")
    elif calificacion >= 90 and calificacion <= 100:
        print("Excelente")

except ValueError:
    print("Debes introducir un número válido.")


# 39. Escribe una función que tome dos parámetros:  figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    """
    Calcula el área de una figura.

    Args:
        figura (str): una cadena de texto que puede ser "rectangulo" , "circulo" o "triangulo".
        datos (tuple): tupla con los datos necesarios para calcular el área de la figura.

    Raises:
        ValueError: si la figura indicada no se reconoce.

    Returns:
        int, float: resultado de calcular el área de la figura.
    """
    if figura == "rectangulo":
        base, altura = datos  # Desempaquetamos la tupla en base y altura.
        return round(base * altura, 2)  
    elif figura == "circulo":
        radio = datos[0]  # Para el círculo solo necesitamos el radio.
        return round(math.pi * radio**2, 2)
    elif figura == "triangulo":
        base, altura = datos  # Desempaquetamos la tupla en base y altura.
        return round((base * altura) / 2, 2)
    else:
        raise ValueError(f"Figura '{figura}' no reconocida.")  # Si la figura no es ninguna de las esperadas, lanzamos un error.

print(calcular_area("circulo", (3,)))  # la coma en (3,) es lo que crea una tupla de un solo elemento
print(calcular_area("rectangulo", (2, 4)))
print(calcular_area("triangulo", (3, 6)))

try:
    print(calcular_area("cuadrado", (2, 6)))  # probamos con una figura que no está definida en la función
except ValueError as error:
    print(f"Error: {error}")


# 40. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
    # 1. Solicita al usuario que ingrese el precio original de un artículo.
    # 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    # 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    # 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
    # 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
    # 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

try:
    precio_original = float(input("Indique el precio original del artículo que desea adquirir: "))  # Solicitamos al usuario el precio original y lo convertimos a float.
    cupon_descuento = input("¿Tienes cupón de descuento? (sí/no): ").lower()  # Solicitamos al usuario que indique si posee un cupón de descuento y transformamos a minúsculas.
    
    if cupon_descuento == "sí" or cupon_descuento == "si" :  # Con esto contemplamos que el usuario haya puesto o no tilde en el 'Sí'.
        importe_cupon = float(input("Por favor, indíquenos el valor de su cupón de descuento: "))   # Solicitamos al usuario el importe del cupón y lo convertimos a float.
        if importe_cupon > 0:  # Si el cupón es válido (que sea mayor que cero).
            precio_final = round(max(0.0, (precio_original - importe_cupon)), 2)  #  Redondearemos el resultado a dos decimales y para el caso en que el cupón sea superior al precio original, usaremos 'max' para que el precio sea cero en vez de un valor negativo.
            print(f'El importe de su compra tras el descuento es: {precio_final}€') 
        else:  # Si el cupón no es válido, se lo indicaremos con un mensaje al usuario y le devolveremos el precio final, que será igual al precio original.
            print("El cupón no es válido por lo que se aplicará el precio sin descuento")  
            precio_final = precio_original
            print(f'El importe final es: {precio_final}€')
    elif cupon_descuento == "no":   # Si el usuario indica que no posee un cupón de descuento, devolveremos el precio final, que será igual al precio original.
        precio_final = precio_original
        print(f'El importe final es: {precio_final}€')
    else:  # En el caso de que el usuario indique una respuesta diferente a sí o no, se le indicará por mensaje y le devolverá el importe final, que será igual al precio original.
        print("Respuesta no reconocida. Se asumirá que no tienes un cupón de descuento")
        precio_final = precio_original
        print(f'El importe final es: {precio_final}€')

except ValueError:
    print("Debe indicar un valor numérico")  # Se devuelve este error en el caso de que el usuario indique un valor no numérico en precio_original o en importe_cupon.