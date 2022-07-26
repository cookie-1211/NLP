import os


def dop(s):
    return('0' * (4 - len(s)) + s)

path = r'C:\Users\kisel_bkz0lc5\OneDrive\Рабочий стол\проект\test'
 
for root, dirs, files in os.walk(path):
    for name in files:
        new_name = dop(name.replace('.txt', ''))
        new_name = new_name + '.txt'
        os.rename(f'C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\test\\{name}', f'C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\test\\{new_name}')

for root, dirs, files in os.walk(path):
    for name in files:
        new_name = dop(name.replace('.txt', ''))
        new_name = new_name + '.txt'
        os.rename(f'C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\learn\\{name}', f'C:\\Users\\kisel_bkz0lc5\\OneDrive\\Рабочий стол\\проект\\learn\\{new_name}')

