
import random
from prettytable import PrettyTable

print("Y = a0 + a1*X1 + a2*X2 + a3*X3")
try:
    limit = float(input("Введіть ліміт для генерації факторів: "))
    a0 = float(input("Enter a0: "))
    a1 = float(input("Enter a1: "))
    a2 = float(input("Enter a2: "))
    a3 = float(input("Enter a3: "))
except ValueError:
    print("Помилка. Дані введені некоректно.")
else:
    x_table = PrettyTable()

    column_names = ["№", "X1", "X2", "X3", "Y", "Xn1", "Xn2", "Xn3"]

    num_columns = 3
    num_rows = 8

    X1 = [random.randint(0, limit) for m in range(num_rows)]
    X2 = [random.randint(0, limit) for n in range(num_rows)]
    X3 = [random.randint(0, limit) for l in range(num_rows)]

    x_table.add_column(column_names[0], [num for num in range(1, num_rows+1)])
    x_table.add_column(column_names[1], X1)
    x_table.add_column(column_names[2], X2)
    x_table.add_column(column_names[3], X3)

    Y = []
    for i in range(len(X1)):
        y = a0 + a1*X1[i] + a2*X2[i] + a3*X3[i]
        Y.append(y)

    x_table.add_column(column_names[4], Y)

    X01 = (max(X1) + min(X1))/2
    X02 = (max(X2) + min(X2))/2
    X03 = (max(X3) + min(X3))/2

    DX1 = max(X1)-X01
    DX2 = max(X2)-X02
    DX3 = max(X3)-X03

    Xn1 = []
    Xn2 = []
    Xn3 = []
    for i in range(len(X1)):
        Xn1.append((X1[i]-X01)/DX1)
        Xn2.append((X2[i]-X02)/DX2)
        Xn3.append((X3[i]-X03)/DX3)

    x_table.add_column(column_names[5], Xn1)
    x_table.add_column(column_names[6], Xn2)
    x_table.add_column(column_names[7], Xn3)

    x_table.add_row(["X0", X01, X02, X03, " ", " ", " ", " "])
    x_table.add_row(["DX", DX1, DX2, DX3, " ", " ", " ", " "])

    Y_et = a0 + a1*X01 + a2*X02 + a3*X03
    ostatok = -Y_et
    for i in range(len(Y)):
        if Y_et - Y[i] < 0 and Y_et - Y[i] > ostatok:
            ostatok = Y_et - Y[i]

    print(x_table.get_string())
    print("Y эталон = ", a0 + a1*X01 + a2*X02 + a3*X03)
    print("\nY = ", Y_et - ostatok)
