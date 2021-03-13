import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plot

n = 4.4
s = 16.6 # начальное расстояние от лодки до катера
fi = 3 * math.pi / 4

# функция, описывающая движения катера береговой охраны
def f(r, tetha):
    dr = r/math.sqrt(n*n - 1)
    return dr

# начальные условия:
    
# начальные для 1го случая:
#r0 = s/(n+1)

# начальные для 2го случая:
r0 = s/(n-1)

# для 1го случая:
#tetha = np.arange(0,2*math.pi, 0.01)

# для 2го случая:
tetha = np.arange(-math.pi,math.pi, 0.01)

r = odeint(f, r0, tetha)

# функция, описывающая движение лодки браконьеров
def f2(t):
    xt = math.tan(fi) * t
    return xt

t = np.arange(0,20,1)

r1 = np.sqrt(t * t + f2(t) * f2(t))

tetha1 = np.arctan(f2(t)/t)

#Построение графиков функций
plot.polar(tetha, r, 'b') #движение катера охраников
plot.polar(tetha1, r1, 'r') #движение лодки браконьеров

tmp = 0
for i in range(len(tetha)):
    #if round(tetha[i],2) == round(fi + math.pi, 2): #для 1го случая
    if round(tetha[i],2) == round(fi - math.pi, 2): #для 2го случая
        tmp = i
#Координаты точки пересечения графиков движения охраников и браконьеров
#в полярных координатах
print("tetha = ", tetha[tmp], "and r = ", r[tmp][0])
#в декартовых координатах
print("x = ", r[tmp][0]/math.sqrt(2), "y = ", -r[tmp][0]/math.sqrt(2))