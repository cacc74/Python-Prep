# %%
print('algo')

# %% [markdown]
# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# %%
a = 10
print(a)

# %% [markdown]
# 2. Imprimir el tipo de dato de la constante 8.5

# %%
print(type(8.5))

# %%
type(8.5)

# %% [markdown]
# 3. Imprimir el tipo de dato de la variable creada en el punto 1

# %%
type(a)
print(type(a))

# %% [markdown]
# 4. Crear una variable que contenga tu nombre

# %%
Mi_Nombre = 'César Cardona'

# %% [markdown]
# 5. Crear una variable que contenga un número complejo

# %%
Nro_Complejo = 1j

# %% [markdown]
# 6. Mostrar el tipo de dato de la variable crada en el punto 5

# %%
type(Nro_Complejo)

# %% [markdown]
# 7. Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# %%
Nro_Pi =  3.1416
print(round(Nro_Pi,4))

# %% [markdown]
# 8. Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
# 
# R/ No es lo mismo, una variable queda con un valor tipo cadena (por las comillas) y la otra variable con un valor tipo booleano.

# %%
Vlr_True_C = 'True'
Vlr_True_B = True

# %% [markdown]
# 9. Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# %%
print(type(Vlr_True_B))
print(type(Vlr_True_C))
print('La variable Vlr_True_B es del tipo', type(Vlr_True_B), 'La variable Vlr_True_C es del tipo', type(Vlr_True_C) )

# %% [markdown]
# 10. Asignar a una variable, la suma de un número entero y otro decimal

# %%
Var_Ent_mas_Dec = 10 + 10.5

# %% [markdown]
# 11. Realizar una operación de suma de números complejos

# %%
print(1j + 2j)
VC1 = 1 + 2j
VC2 = 5 + 3j
print(VC1 + VC2)

# %% [markdown]
# 12. Realizar una operación de suma de un número real y otro complejo

# %%
VC3 = Var_Ent_mas_Dec + VC1
print(VC3)

# %% [markdown]
# 13. Realizar una operación de multiplicación

# %%
print(10 * 8)

# %% [markdown]
# 14. Mostrar el resultado de elevar 2 a la octava potencia

# %%
print(2**8)

# %% [markdown]
# 15. Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# %%
Var_Cociente = 27 / 4
print(Var_Cociente)

# %% [markdown]
# 16. De la división anterior solamente mostrar la parte entera

# %%
print(27 // 4)

# %% [markdown]
# 17. De la división de 27 entre 4 mostrar solamente el resto

# %%
print(27 % 4)

# %% [markdown]
# 18. Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# %%
print(4 * (27 // 4) + (27 % 4))

# %% [markdown]
# 19. Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# %%
Nombre = 'César '
Apellido = 'Cardona'
print(Nombre + Apellido)

# %% [markdown]
# 20. Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
# 
# R/ El resultado da falso porque son variables de diferente tipo, una es una cadena y la otra un entero, al compararlas el resultado es false.

# %%
print('2' == 2)

# %% [markdown]
# 21. Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# %%
print(int('2') + 2)
print('2' + str(2))

# %% [markdown]
# 22 ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# 
# R/ Porque los decimales no se separan con (coma) sino con (punto)

# %%
a = float('3,8')

# %% [markdown]
# 23. Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# %%
Vlr_3 = 3
Vlr_3 -= 1
print(Vlr_3)

# %% [markdown]
# 24. Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# %%
1 << 2

# %% [markdown]
# ¿Por qué da ese resultado?
# Son operadores de desplazamiento de bits que existen en muchos lenguajes de programación principales, << es el desplazamiento a la izquierda y >> es el desplazamiento a la derecha.
# 
# Sistema Binario:
# El sistema binario, también llamado sistema diádico​ en ciencias de la computación, es un sistema de numeración en el que los números son representados utilizando únicamente dos cifras: 0 y 1.

# %% [markdown]
# 25. Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# 
# ¿Por qué no está permitido?
# No esta permitido porque no se pueden sumar dos constantes de diferente tipo, en este caso una es un entero y la otra na cadena
# 
# ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# Si arrojaria el mismo resultado en este caso, porque estaría sumando dos constantes.

# %%
2 + '2'

# %% [markdown]
# 26. Realizar una operación válida entre valores de tipo entero y string

# %%
print(2 + int('2'))


