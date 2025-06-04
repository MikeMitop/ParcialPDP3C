# Tercer parcial Paradigmas de programación.

## Comparación de Rendimiento entre Enfoques Recursivo e Iterativo en el Cálculo de la Serie de Fourier

**Contexto**: la Serie de Fourier permite representar funciones periódicas como combinaciones de senos y cosenos. En programación científica, los métodos para calcular estos coeficientes pueden implementarse usando enfoques iterativos o recursivos. Cada uno presenta ventajas y desventajas en términos de claridad, eficiencia y consumo de memoria.

**Problema**: se desea comparar el rendimiento computacional de dos enfoques para calcular los coeficientes de la Serie de Fourier de una función periódica evaluada numéricamente:

* **Enfoque iterativo:** que calcula los coeficientes en un bucle **for**

* **Enfoque recursivo:** que calcula los coeficientes haciendo llamadas recursivas hasta alcanzar el armónico base.


## Realizar

1. **Definir una función periódica** `f(t)` evaluada sobre un conjunto de `M` puntos uniformemente espaciados en el intervalo `[0, T)`.

2. **Implementar dos funciones**:

   - `calcular_serie_fourier_iterativa(f, t, T, N)`: Calcula los coeficientes de la Serie de Fourier usando un bucle `for`.

   - `calcular_serie_fourier_recursiva(f, t, T, N)`: Calcula los coeficientes de forma recursiva, con una función auxiliar que se llama a sí misma.

3. **Calcular los coeficientes** `a₀`, `aₙ`, `bₙ` para `n = 1...N` usando integración numérica (por ejemplo, la **regla del trapecio**):

   $a_n = \frac{2}{T} \int_0^T f(t) \cos\left(\frac{2\pi n t}{T}\right)dt$
   $\quad \text{y} \quad$
   
   $b_n = \frac{2}{T} \int_0^T f(t) \sin\left(\frac{2\pi n t}{T}\right) dt$

4. **Comparar el rendimiento** de ambas funciones usando:

   - Tiempo de ejecución (`time` o `timeit`)
   - Consumo de memoria *(opcional, usando `memory_profiler`)*

5. **Graficar o tabular** los resultados de tiempo vs. número de armónicos `N` para ambos métodos.


## Ejemplo de uso:

```python
import numpy as np
T = 2 * np.pi
t = np.linspace(0, T, 1000, endpoint=False)
f = np.sign(np.sin(t))  # Onda cuadrada
# Comparación
coef_iter = calcular_serie_fourier_iterativa(f, t, T, 10)
coef_recur = calcular_serie_fourier_recursiva(f, t, T, 10)
```
## Entrega esperada

Al final del ejercicio, deberá entregar:

- **Las dos implementaciones**:
  - `calcular_serie_fourier_iterativa`
  - `calcular_serie_fourier_recursiva`

- **Gráficas o tablas de tiempo de ejecución** para distintos valores de `N` (por ejemplo: `N = 5`, `N = 10`, `N = 20`, `N = 50`).

- **Un breve análisis comparativo** que responda:
  - ¿Cuál método resulta más eficiente?
  - ¿Por qué? (Considera aspectos como la **complejidad temporal**, la **profundidad de recursión** y la **legibilidad del código**).


## Tiempo: 90 min