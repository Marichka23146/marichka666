m = 5
x = [3, 4, 0, 2, 22, 16, 7, 19, 11, 665, 144, 8, 1]
y = [x for x in x if abs(x) >= m]
print("Число M:", m)
print("Масив X:", x)
print("Масив Y:", y)