# Пользователь вводит число от 1 до 999.
# Используя операции с числами, сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

OUT_OF_RANGE = 1000
num = OUT_OF_RANGE
while True:
    if num < 0 or num > 999:
        num = int(input('Enter a number from 1 to 999: '))
    else: break
print(num)    

if num // 100:
    info = 'This is three-digit number'
    result = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
elif num // 10:
    info = 'This is two-digit number'
    result = (num % 10) * (num // 10)    
else:
    info = 'This is one-digit number'
    result = num**2

print(info, result)