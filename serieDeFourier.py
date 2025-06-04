import numpy as np
import matplotlib.pyplot as plt
import time

def f(t, T):
    if t % T < T/2:
        return 1.0
    else:
        return -1.0

def calcular_serie_fourier_iterativa(f_valores, t, T, N):
    dt = T / len(t)
    a0 = 0
    for i in range(len(t)):
        a0 += f_valores[i]
    a0 = (2 / T) * dt * a0 / 2
    
    a_n = []
    b_n = []
    
    for n in range(1, N+1):
        suma_a = 0
        suma_b = 0
        for i in range(len(t)):
            suma_a += f_valores[i] * np.cos(2 * np.pi * n * t[i] / T)
            suma_b += f_valores[i] * np.sin(2 * np.pi * n * t[i] / T)
        a_n.append((2 / T) * dt * suma_a)
        b_n.append((2 / T) * dt * suma_b)
    
    return a0, a_n, b_n

def calcular_serie_fourier_recursiva(f_valores, t, T, N):
    dt = T / len(t)
    a0 = 0
    for i in range(len(t)):
        a0 += f_valores[i]
    a0 = (2 / T) * dt * a0 / 2
    
    a_n = [0] * N
    b_n = [0] * N
    
    def calcular_armonico(n):
        if n > N:
            return
        
        suma_a = 0
        suma_b = 0
        for i in range(len(t)):
            suma_a += f_valores[i] * np.cos(2 * np.pi * n * t[i] / T)
            suma_b += f_valores[i] * np.sin(2 * np.pi * n * t[i] / T)
        
        a_n[n-1] = (2 / T) * dt * suma_a
        b_n[n-1] = (2 / T) * dt * suma_b
        
        calcular_armonico(n + 1)
    
    calcular_armonico(1)
    return a0, a_n, b_n

def comparar_tiempos(valores_N):
    T = 2 * np.pi
    M = 1000
    t = np.linspace(0, T, M, endpoint=False)
    f_valores = [f(ti, T) for ti in t]
    
    tiempos_iter = []
    tiempos_rec = []
    
    for N in valores_N:
        #  iterativo
        inicio = time.time()
        calcular_serie_fourier_iterativa(f_valores, t, T, N)
        fin = time.time()
        tiempo_iter = fin - inicio
        tiempos_iter.append(tiempo_iter)
        
        #  recursivo
        inicio = time.time()
        calcular_serie_fourier_recursiva(f_valores, t, T, N)
        fin = time.time()
        tiempo_rec = fin - inicio
        tiempos_rec.append(tiempo_rec)
        
        print(f"N = {N}: Iterativo {tiempo_iter:.6f}s, Recursivo {tiempo_rec:.6f}s")
    
    return valores_N, tiempos_iter, tiempos_rec

def main():
    valores_N = [5, 10, 20, 50, 100]
    print("Comparando tiempo entre iterativo y recursivo:")
    valores_N, tiempos_iter, tiempos_rec = comparar_tiempos(valores_N)
if __name__ == "__main__":
    main()


