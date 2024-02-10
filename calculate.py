def factorial(n):
    """
    Функція для обчислення факторіалу числа.

    Параметри:
    - n (int): Ціле число, для якого обчислюється факторіал.

    Повертає:
    int: Факторіал введеного числа.
    """
    # Реалізація обчислення факторіалу
    if n == 1 or n == 0:
        return 1
    else:
        return  factorial(n-1)*n


# Приклад використання функції:
number = 5
result = factorial(number)
print(f"Факторіал числа {number} дорівнює {result}")