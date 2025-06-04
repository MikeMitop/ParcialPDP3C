# Tercer parcial Paradigmas de programación.

## Comparación de Rendimiento entre Enfoques Recursivo e Iterativo en el Cálculo de la Serie de Fourier

# Objetivo
 Implementar y validar dos funciones para el cálculo de los coeficientes de la Serie de Fourier de una función periódica:

 calcular_serie_fourier_iterativa(f, t, T, N) (enfoque iterativo).

 calcular_serie_fourier_recursiva(f, t, T, N) (enfoque recursivo).


# Resultados

| N   | Iterativo (segundos en 0.) | Recursivo (segundos en 0.) |
| --- | -------------------------- | -------------------------- |
| 5   | 34671                      | 34345                      |
| 10  | 75927                      | 76125                      |
| 20  | 143882                     | 156445                     |
| 50  | 362229                     | 231296                     |
| 100 | 329182                     | 285516                     |


# Respuesta a las preguntas

* El enfoque iterativo resulta más eficiente que el recursivo para el cálculo de los coeficientes de la Serie de Fourier.

* ¿Por qué?: La recursión consume espacio en la pila conforme crece el número de armónicos (N), lo que puede provocar desbordamientos cuando N es alto. En cambio, un bucle for itera sin restricciones de profundidad. Por otro lado, un bucle for es directo y fácil de seguir, mientras que la versión recursiva requiere definir casos base y entender el flujo de llamadas, haciéndola menos intuitiva y más propensa a errores en la depuración. 
