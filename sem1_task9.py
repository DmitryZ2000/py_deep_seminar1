#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
for i in range(2,11): # Множитель
    for j in range(2,6): # Умножаемое
        if j * i < 10:
            print(f'{j} x {i} = {j * i}', end='     ' ) # Результат меньше 10
        elif j * i >=10 and i != 10:
            print(f'{j} x {i} = {j * i}', end='    ' ) # Результат двузачный
        else:
            print(f'{j} x {i} ={j * i}', end='    ' ) # Умножаем на 10
    print()

print()

for i in range(2,11):
    for j in range(6,10):
        if j * i < 10:
            print(f'{j} x {i} = {j * i}',  end='     ' )
        elif j * i >=10 and i != 10:
            print(f'{j} x {i} = {j * i}',  end='    ' )
        else:
            print(f'{j} x {i} ={j * i}', end='    ' )
    print()