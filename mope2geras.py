import math
from random import randint
import numpy as np

p_list = (0.99, 0.98, 0.95, 0.90)
rkr_table = {2: (1.73, 1.72, 1.71, 1.69),
             6: (2.16, 2.13, 2.10, 2.00),
             8: (2.43, 4.37, 2.27, 2.17),
             10: (2.62, 2.54, 2.41, 2.29),
             12: (2.75, 2.66, 2.52, 2.39),
             15: (2.9, 2.8, 2.64, 2.49),
             20: (3.08, 2.96, 2.78, 2.62)}

# вставить текст
MIN_Y_LIMIT, MAX_Y_LIMIT, M = 110, 210, 5
X1_min, X1_min_n = 15, 1
X1_max, X1_max_n = 45, 1
X2_min, X2_min_n = -25, -1
X2_max, X2_max_n = 10, 1

Y_MATRIX = [[randint(MIN_Y_LIMIT, MAX_Y_LIMIT) for i in range(M)] for j in range(3)]

AVG_Y = [sum(Y_MATRIX[i][j] for j in range(M)) / M for i in range(3)]

SIGMA2_1 = sum([(j - AVG_Y[0]) ** 2 for j in Y_MATRIX[0]]) / M
SIGMA2_2 = sum([(j - AVG_Y[1]) ** 2 for j in Y_MATRIX[1]]) / M
SIGMA2_3 = sum([(j - AVG_Y[2]) ** 2 for j in Y_MATRIX[2]]) / M

SIGMA_TETA = math.sqrt((2 * (2 * M - 2)) / (M * (M - 4)))

FUV_1 = SIGMA2_1 / SIGMA2_2
FUV_2 = SIGMA2_3 / SIGMA2_1
FUV_3 = SIGMA2_3 / SIGMA2_2

TETA_UV_1 = (M - 2 / M) * FUV_1
TETA_UV_2 = (M - 2 / M) * FUV_2
TETA_UV_3 = (M - 2 / M) * FUV_3

RUV1 = abs(TETA_UV_1 - 1) / SIGMA_TETA
RUV2 = abs(TETA_UV_2 - 1) / SIGMA_TETA
RUV3 = abs(TETA_UV_3 - 1) / SIGMA_TETA

MX1 = (-1 + 1 - 1) / 3
MX2 = (-1 - 1 + 1) / 3
MY = sum(AVG_Y) / 3
A1 = (1 + 1 + 1) / 3
A2 = (1 - 1 - 1) / 3
A3 = (1 + 1 + 1) / 3
A11 = (-1 * AVG_Y[0] + 1 * AVG_Y[1] - 1 * AVG_Y[2]) / 3
A22 = (-1 * AVG_Y[0] - 1 * AVG_Y[1] + 1 * AVG_Y[2]) / 3

B0 = np.linalg.det(np.dot([[MY, MX1, MX2],
                           [A11, A1, A2],
                           [A22, A2, A3]],
                          np.linalg.inv([[1, MX1, MX2],
                                         [MX1, A1, A2],
                                         [MX2, A2, A3]])))

B1 = np.linalg.det(np.dot([[1, MY, MX2],
                           [MX1, A11, A2],
                           [MX2, A22, A3]],
                          np.linalg.inv([[1, MX1, MX2],
                                         [MX1, A1, A2],
                                         [MX2, A2, A3]])))

B2 = np.linalg.det(np.dot([[1, MX1, MY],
                           [MX1, A1, A11],
                           [MX2, A2, A22]],
                          np.linalg.inv([[1, MX1, MX2],
                                         [MX1, A1, A2],
                                         [MX2, A2, A3]])))

NORM_Y = B0 - B1 + B2

DX1 = math.fabs(X1_max - X1_min) / 2
DX2 = math.fabs(X2_max - X2_min) / 2
X10 = (X1_max + X1_min) / 2
X20 = (X2_max + X2_min) / 2

AA0 = B0 - B1 * X10 / DX1 - B2 * X20 / DX2
AA1 = B1 / DX1
AA2 = B2 / DX2


def odnoridna_dispersion():
    m = min(rkr_table, key=lambda x: abs(x - M))
    p = 0
    for ruv in (RUV1, RUV2, RUV3):
        if ruv > rkr_table[m][0]:
            return False
        for rkr in range(len(rkr_table[m])):
            if ruv < rkr_table[m][rkr]:
                p = rkr
    return p_list[p]


def naturalized_regression(x1, x2):
    return AA0 + AA1 * x1 + AA2 * x2


# output
for i in range(3):
    print("Y{}: {}, Average: {}".format(i + 1, Y_MATRIX[i], AVG_Y[i]))
print()
print("σ² y1:", SIGMA2_1)
print("σ² y2:", SIGMA2_2)
print("σ² y3:", SIGMA2_2)
print("σθ =", SIGMA_TETA)
print()
print("Fuv1 =", FUV_1)
print("Fuv2 =", FUV_2)
print("Fuv3 =", FUV_3)
print()
print("θuv1 =", TETA_UV_1)
print("θuv2 =", TETA_UV_2)
print("θuv3 =", TETA_UV_3)
print()
print("Ruv1 =", RUV1)
print("Ruv2 =", RUV2)
print("Ruv3 =", RUV3)
print()
print("Однорідна дисперсія:", odnoridna_dispersion())
print()
print("mx1:", MX1)
print("mx2:", MX2)
print("my:", MY)
print("a1:", A1)
print("a2:", A2)
print("a3:", A3)
print("a11:", A11)
print("a22:", A22)
print("b0:", B0)
print("b1:", B1)
print("b2:", B2)
print("Натуралізація коефіцієнтів:")
print("Δx1:", DX1)
print("Δx2:", DX2)
print("x10:", X10)
print("x20:", X20)
print("a0:", AA0)
print("a1:", AA1)
print("a2:", AA2)
print()
print("Натуралізоване рівняння регресії:")

NR_Y = [round(naturalized_regression(X1_min, X2_min), 2),
        round(naturalized_regression(X1_max, X2_min), 2),
        round(naturalized_regression(X1_min, X2_max), 2)]
print(NR_Y)
if NR_Y == AVG_Y:
    print("Коефіцієнти натуралізованого рівняння регресії вірні")
else:
    print("Коефіцієнти натуралізованого рівняння регресії НЕ вірні")
