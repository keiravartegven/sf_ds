"""Game - guess the number"""
import numpy as np

number = np.random.randint(1, 101) # загадываем число

#счетчик попыток
count = 0

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100! Введи число: '))
    
    if predict_number > number:
        print('загаданое число меньше')
    elif predict_number < number:
        print('загаданое число больше')
    else:
        print(f'Вы угадали число за {count} попыток! Это число {number}')
        break #остановка игры если угадали