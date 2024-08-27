"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def game_core_v3(number: int = 1) -> int:
    """
    Каждый раз уменьшаем диапазон поиска вдвое и сравниваем с серединой диапазона пока не найдем число.
    Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    #  определяем количество попыток, нижнюю и верхнюю границу диапазона
    сount = 0
    min_predict = 1
    max_predict = 100

    # пока минимальное значение диапазона меньше или равно максимальному
    while min_predict <=  max_predict:
        # находим середину диапазона
        avg_predict = (min_predict + max_predict) // 2
        сount += 1
        if avg_predict == number:
            return сount
        # если загаданное число больше середины диапазона, то сдвигаем нижнюю границу диапазона
        elif avg_predict < number:
            min_predict = avg_predict + 1
        # если загаданное число меньше середины диапазона, то сдвигаем верхнюю границу диапазона
        else:
            max_predict = avg_predict - 1
            
    # Ваш код заканчивается здесь


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
