"""Game - guess the number"""
"""Computer make and guess the number"""

#Импортируем библиотеку, которая пригодится для генерации случайных чисел.
import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Задаем минимальное и максимальное числа, устанавливаем число, которое будем сравнивать с загаданным,
    оно равно среднему значению суммы максимального и минимального чисел. Если число больше загаданного, то
    минимальное значение приравниваем к этому числу, и задаем число, как новое среднее значение
    суммы максимального и минимального чисел. Если число меньше загаданного, то заменяем максимальное значение и 
    задаем число, как новое среднее значение суммы максимального и минимального чисел, до тех пор пока не угадаем число.
    Функция возвращает число попыток.
      
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 1
    max = 101
    predict = (min+max)//2

    while number != predict:
        count += 1
        if number > predict:
          min = predict
          predict = (min+max)//2
        elif number < predict:
          max = predict
          predict = (min+max)//2
          
    return count      
          
          
#Запишем функцию, которая определяет за какое количество попыток программа угадывает число.
def score_game(random_predict) -> int:
    """за какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    

if __name__ == '__main__':
    # RUN - оценка качества работы алгоритма
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)
    