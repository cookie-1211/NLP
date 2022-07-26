import os
import shutil
# import pathlib

# arr = []

# for i in range(1, 6153):
#     f = open(f"review_{i}.txt", "r")
#     text = f.readlines()
#     arr.append(int(text[1].strip()))

# for i in set(arr):
#     print(i, arr.count(i))



a1 = 175
a2 = 169
a3 = 499
a4 = 1818
a5 = 3491


b1 = 175 // 2
b2 = 169 // 2
b3 = 499 // 2
b4 = 1818 // 2
b5 = 3491 // 2

arr1 = []
arr2 = []


# получения списков имен файлов для разделения по директориям
for i in range(1, 6153):
    f = open(f"review_{i}.txt", "r")
    text = f.readlines()
    b = int(text[1].strip())

    if b == 1:
        if b1 != 0:
            arr1.append(f"review_{i}.txt")
            b1 -= 1
        else:
            arr2.append(f"review_{i}.txt")

    if b == 2:
        if b2 != 0:
            arr1.append(f"review_{i}.txt")
            b2 -= 1
        else:
            arr2.append(f"review_{i}.txt")

    if b == 3:
        if b3 != 0:
            arr1.append(f"review_{i}.txt")
            b3 -= 1
        else:
            arr2.append(f"review_{i}.txt")
    
    if b == 4:
        if b4 != 0:
            arr1.append(f"review_{i}.txt")
            b4 -= 1
        else:
            arr2.append(f"review_{i}.txt")

    if b == 5:
        if b5!= 0:
            arr1.append(f"review_{i}.txt")
            b5 -= 1
        else:
            arr2.append(f"review_{i}.txt")

print(arr1)
print(arr2)
    
    
# разделение файлов по директориям
 
# os.mkdir("test")
# os.mkdir("learn")

# for i in arr1:
#     os.replace(f"C:\Users\kisel_bkz0lc5\OneDrive\Рабочий стол\проект\{i}", f"C:\Users\kisel_bkz0lc5\OneDrive\Рабочий стол\проект\\test\{i}")

# for i in arr2:
#     os.replace(f"C:\Users\kisel_bkz0lc5\OneDrive\Рабочий стол\проект\{i}", f"C:\Users\kisel_bkz0lc5\OneDrive\Рабочий стол\проект\learn\{i}")

# for i in arr1:
#     shutil.move(f"C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\{i}", f"C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\test\\{i}")

# for i in arr2:
#     shutil.move(f"C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\{i}", f"C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\learn\\{i}")

