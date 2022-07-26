import os


def clean_text(text):
    new_text = text.split(".|,|!| |")   
    new_text = ' '.join(text)
    return new_text



file = open('0028.txt')
text  = file.read()
file.close()

file = open('0028.txt', 'w')
new_text = clean_text(text)
print(new_text, file)






# счет "неправильных по ." продложений
# count1 = 0
# arr1 = []
# path = r'C:\Users\kisel_bkz0lc5\OneDrive\Рабочий стол\проект\test'
# for root, dirs, files in os.walk(path):
#     for name in files:
#         text = open(path + '\\' + name).read().replace('. ', '')
#         if '.' in text:
#             count1 += 1
#             arr1.append(name)


# count2 = 0
# arr2 = []
# path = r'C:\Users\kisel_bkz0lc5\OneDrive\Рабочий стол\проект\learn'
# for root, dirs, files in os.walk(path):
#     for name in files:
#         text = open(path + '\\' + name).read().replace('. ', '')
#         if '.' in text:
#             count2 += 1
#             arr2.append(name)

# print(count1)
# print(count2)
