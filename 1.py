# list_1 = ["H", "e", "l", "l", "o"]
# print('  '.join(list_1))


stroka = 'Hello world Moscow Name'
print(len(stroka.split(" ")))

# 2  вариант

stroka = 'Hello world Moscow Name'
list_1 = []
for i in stroka:
    list_1.append(i)
print(list_1)

# 3 вариант

str = 'wefwef'
print(list(str))