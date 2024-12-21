# 1.
'''
_num1 = int(input("выведите число 1"))
_num2 = int(input("выведите число 2"))

print(_num1,_num2)
'''

'''
# 2.

_name1 = 'Hello'
_name2 = 'world'

K_1 = _name1 + " " + _name2
print(K_1)

K_2 = _name1 * 4
print(K_2)

print(_name1, end='\n' + _name2)
'''

# 3.

# Задача: Написать программу, которая принимает число от пользователя и проверяет, является ли оно простым числом.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ввод числа
number = int(input("Введите число: "))

# Проверка и вывод результата
if is_prime(number):
    print(f"{number} — простое число.")
else:
    print(f"{number} — составное число.")

