if __name__ == '__main__':
    x = int(input("x:"))
    y = int(input("y:"))
    z = int(input("z:"))
    n = int(input("n:"))

x_values = [g for g in range(x+1)]
y_values = [g for g in range(y+1)]
z_values = [g for g in range(z+1)]

result  = [[i, j, k] for i in x_values for j in y_values for k in z_values if i + j + k != n]
print(result)