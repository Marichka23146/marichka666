import math

def data(file_path='input.txt'):
    with open(file_path, 'r') as file:
        numbers = file.readline().split()
        x = float(numbers[0])
        y = math.tan(x) * (x / 2.65)
        z = 1 + math.log(abs(y))/3
    return x, y, z
result = data()
result_str = f"x: {result[0]:.2f}\n y: {result[1]:.2f}\n m: {result[2]:.2f}"  # Виправлено result[3] на result[2]
with open("output.txt", 'w') as f:
    f.write(result_str)
print(result_str)
