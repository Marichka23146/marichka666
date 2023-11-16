array=[5,3,-2.3,5,-6,4,5,-33,0]
print(array)
for x in range(len(array)):
    if array[x]<0:
        array[x]=abs(array[x])
print("Додатній список: ", array)