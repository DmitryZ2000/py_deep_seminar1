# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1001)

count = 1
ATTEMPS = 10

while count <= ATTEMPS:
    print('Попытка номер: ', count)
    your_number = int(input('Угадайте число от 0 до 1000: '))
    if your_number < num:
        print('Введите большее число')
        count +=1
    elif your_number > num:
        print('Введите меньшее число')
        count +=1
    else:
        print('Вы угадали число ', num)
        break # Выход из цикла while
else:
    print('Вы исчерпали количество попыток')
    print('Было загадано число: ', num)

