import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
lam = 1.0  # длина волны 
k = 2*np.pi/lam  # волновое число
U0 = 1.0  # амплитуда падающей волны
z = 8*lam  # расстояние от метаповерхности до плоскости наблюдения

# Задаем метаповерхность в виде фазовой маски
N = 256
x = np.linspace(-10*lam, 10*lam, N)
y = np.linspace(-10*lam, 10*lam, N)
X, Y = np.meshgrid(x, y)

T = np.exp(1j*np.sin(X/lam)*np.sin(Y/lam))  # пример фазовой маски

# Падающая волна
U1 = U0 * T

# Расчет дифракции методом Рэлея-Зоммерфельда
dx = x[1] - x[0]
dy = y[1] - y[0]
xs = np.linspace(-15*lam, 15*lam, 2*N)  
ys = np.linspace(-15*lam, 15*lam, 2*N)
Xs, Ys = np.meshgrid(xs, ys)

U = np.zeros_like(Xs, dtype=complex)

for i in range(2*N):
    for j in range(2*N):
        r = np.sqrt((Xs[i,j]-X)**2 + (Ys[i,j]-Y)**2 + z**2) 
        U[i,j] = np.sum(U1 * z/r**2 * (1/r - 1j*k) * np.exp(1j*k*r) * dx*dy)

U /= 2*np.pi

# Визуализация
plt.figure(figsize=(8,6), facecolor='white')
plt.pcolormesh(xs/lam, ys/lam, np.abs(U), cmap='jet', shading='auto')
plt.colorbar(label='Амплитуда')
plt.xlabel('x/$\lambda$')
plt.ylabel('y/$\lambda$')
plt.title(f'Дифракция на метаповерхности, z = {z/lam:.1f}$\lambda$')
plt.tight_layout()
plt.savefig('metasurface_diffraction.png', dpi=150)
plt.show()

print('Расчет дифракции на метаповерхности выполнен. График волнового фронта на расстоянии z = {:.1f}λ от метаповерхности сохранен в файл metasurface_diffraction.png'.format(z/lam))