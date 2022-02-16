import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    
        Args:
            number (int, optional): Загаданное число. Defaults to 1.
    
        Returns:
            int: Число попыток
        """
    
    count = 0
    min_predict_number = 1   # минимальнае число
    max_predict_number = 101  # максимальное число
    predict_number = np.random.randint(min_predict_number, max_predict_number)  # предполагаемое число
    while True:
        if number == predict_number:
            count += 1
            break  # выход из цикла, если угадали
        elif predict_number > number:
            count += 1
            max_predict_number = predict_number
            predict_number = np.random.randint(min_predict_number, max_predict_number)
        else:
            count += 1
            min_predict_number = predict_number
            predict_number = np.random.randint(min_predict_number, max_predict_number)
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    
        Args:
            random_predict ([type]): функция угадывания
    
        Returns:
            int: среднее количество попыток
        """
    
    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)
