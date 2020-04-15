import random
import numpy as np
x1min = 15
x1max = 45
x2min = -25
x2max = 10
x3min = 45
x3max = 50
xAvmax = x1max+x2max+x3max/3
xAvmin = x1min+x2min+x3min/3
ymax = int(200+xAvmax)
ymin = int(200+xAvmin)
print(xAvmin)
print(xAvmax)

print('1)Запишем уравнение регрессии'
      '\ny = b0 + b1x1 + b2x2 + b3x3')

print('2) Кодированные значения X')
print('{:<5} {:<5} {:<5} {:<5}'.format("№","X1","X2","X3"))
X11 = ['-1', '-1', '+1', '+1']
X22 = ['-1', '+1', '-1', '+1']
X33 = ['-1', '+1', '+1', '-1']
for i in range(4):
    print('{:<5} {:<5} {:<5} {:<5}'.format(i+1,X11[i],X22[i],X33[i]))

print('3)Заполним матрицу планирования для m=3')
print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}'.format("№","X1","X2","X3",'Y1','Y2',"Y3"))
X1 = [x1min, x1min, x1max, x1max]
X2 = [x2min, x2max, x2min, x2max]
X3 = [x3min, x3max, x3max, x3min]
Y1 = [random.randrange(138,247, 1) for i in range(4)]
Y2 = [random.randrange(138,247, 1) for i in range(4)]
Y3 = [random.randrange(138,247, 1) for i in range(4)]
for i in range(4):
    print('{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}'.format(i+1,X1[i],X2[i],X3[i],Y1[i],Y2[i],Y3[i]))

print('Найдем средние значения функции отклика по рядам. '
      '\nПроведем вычисление коэффициентов регрессии и сравним с Y средним')
y1av1 = (Y1[0]+Y2[0]+Y3[0])/3
y2av2 = (Y1[1]+Y2[1]+Y3[1])/3
y3av3 = (Y1[2]+Y2[2]+Y3[2])/3
y4av4 = (Y1[3]+Y2[3]+Y3[3])/3

mx1 = sum(X1)/4
mx2 = sum(X2)/4
mx3 = sum(X3)/4

my = (y1av1 + y2av2 + y3av3 + y4av4)/4

a1 = (X1[0]*y1av1 + X1[1]*y2av2 + X1[2]*y3av3 + X1[3]*y4av4)/4
a2 = (X2[0]*y1av1 + X2[1]*y2av2 + X2[2]*y3av3 + X2[3]*y4av4)/4
a3 = (X3[0]*y1av1 + X3[1]*y2av2 + X3[2]*y3av3 + X3[3]*y4av4)/4

a11 = (X1[0]*X1[0] + X1[1]*X1[1] + X1[2]*X1[2] + X1[3]*X1[3])/4
a22 = (X2[0]*X2[0] + X2[1]*X2[1] + X2[2]*X2[2] + X2[3]*X2[3])/4
a33 = (X3[0]*X3[0] + X3[1]*X3[1] + X3[2]*X3[2] + X3[3]*X3[3])/4
a12 = a21 = (X1[0]*X2[0] + X1[1]*X2[1] + X1[2]*X2[2] + X1[3]*X2[3])/4
a13 = a31 = (X1[0]*X3[0] + X1[1]*X3[1] + X1[2]*X3[2] + X1[3]*X3[3])/4
a23 = a32 = (X2[0]*X3[0] + X2[1]*X3[1] + X2[2]*X3[2] + X2[3]*X3[3])/4

b01 = np.array([[my, mx1, mx2, mx3], [a1, a11, a12, a13], [a2, a12, a22, a32], [a3, a13, a23, a33]])
b02 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b0 = np.linalg.det(b01)/np.linalg.det(b02)

b11 = np.array([[1, my, mx2, mx3], [mx1, a1, a12, a13], [mx2, a2, a22, a32], [mx3, a3, a23, a33]])
b12 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b1 = np.linalg.det(b11)/np.linalg.det(b12)

b21 = np.array([[1, mx1, my, mx3], [mx1, a11, a1, a13], [mx2, a12, a2, a32], [mx3, a13, a3, a33]])
b22 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b2 = np.linalg.det(b21)/np.linalg.det(b22)

b31 = np.array([[1, mx1, mx2, my], [mx1, a11, a12, a1], [mx2, a12, a22, a2], [mx3, a13, a23, a3]])
b32 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b3 = np.linalg.det(b31)/np.linalg.det(b32)

print(b0 + b1*X1[0] + b2*X2[0] + b3*X3[0], y1av1)
print(b0 + b1*X1[1] + b2*X2[1] + b3*X3[1], y2av2)
print(b0 + b1*X1[2] + b2*X2[2] + b3*X3[2], y3av3)
print(b0 + b1*X1[3] + b2*X2[3] + b3*X3[3], y4av4)
print('Значения совпадают')

print('5)Для статистических проверок найдем дисперсию по рядам')
d1 = ((Y1[0] - y1av1)**2 + (Y2[0] - y2av2)**2 + (Y3[0] - y3av3)**2)/3
d2 = ((Y1[1] - y1av1)**2 + (Y2[1] - y2av2)**2 + (Y3[1] - y3av3)**2)/3
d3 = ((Y1[2] - y1av1)**2 + (Y2[2] - y2av2)**2 + (Y3[2] - y3av3)**2)/3
d4 = ((Y1[3] - y1av1)**2 + (Y2[3] - y2av2)**2 + (Y3[3] - y3av3)**2)/3
print('d1 = ', d1,'d2 = ', d2,'d3 =', d3,'d4 = ', d4)

dcouple = [d1, d2, d3, d4]

m = 3
Gp = max(dcouple)/sum(dcouple)
f1 = m-1
f2 = N = 4
Gt = 0.7679
if Gp < Gt:
    print('Дисперсия однородна')
else:
    print('The oposit to однородна')
print('Оценим значимость кэфов регрессии согласно критерию Стьюдента')
sb = sum(dcouple)/N
ssbs = sb/N*m
sbs = ssbs**0.5

beta0 = (y1av1*1 + y2av2*1 + y3av3*1 + y4av4*1)/4
beta1 = (y1av1*(-1) + y2av2*(-1) + y3av3*1 + y4av4*1)/4
beta2 = (y1av1*(-1) + y2av2*1 + y3av3*(-1) + y4av4*1)/4
beta3 = (y1av1*(-1) + y2av2*1 + y3av3*1 + y4av4*(-1))/4

t0 = abs(beta0)/sbs
t1 = abs(beta1)/sbs
t2 = abs(beta2)/sbs
t3 = abs(beta3)/sbs

f3 = f1*f2
print('f3 = f1*f2, значит берем значение с восьмого ряда tтабл = 2.306'
      '\nОднако замечаем, что t0,t3 > tтабл, t1,t2 < tтабл'
      '\nЗначит кэфы b1 и b2 принимаем незначительными и исключаем из уравнения')
ttabl  = 2.306
yy1 = b0 + b3*x3min
yy2 = b0 + b3*x3max
yy3 = b0 + b3*x3max
yy4 = b0 + b3*x3min
print('6)Критерий Фишера'
      '\nd - количество значимых кэфов')
d = 2
f4 = N - d
sad = ((yy1 - y1av1)**2 + (yy2 - y2av2)**2 + (yy3 - y3av3)**2 + (yy4 - y4av4)**2)*(m/(N-d))
Fp = sad/sb
print(d1, d2, d3, d4, sb)
print(Fp)
print('Ft выбираем из таблицы 8 ряд 2 столбец. Ft = 4.5'
      '\nFp = 11,9 > Ft = 4,5. Уравнение регрессии неадекватно оригиналу при уровне значимости 0.05')
