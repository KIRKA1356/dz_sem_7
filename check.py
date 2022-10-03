import logger


def get_number_int(input_string: str) -> int:
    '''
    Проверка целого числа
    '''
    while True:
        try:
            num = input(input_string)
            num = int(num)
            return num
        except ValueError:
            logger.log(num, 'ValueError')
            print('Это не то ...')


def get_number_float(input_string: str) -> float:
    '''
    Проверка числа с плавающей точкой
    '''
    while True:
        try:
            num = input(input_string)
            num = float(num)
            return num
        except ValueError:
            logger.log(num, 'ValueError')
            print('Это не то ...')


def get_symbol(input_string: str) -> str:
    '''
    Проверка символа для действий
    '''
    while True:
        try:
            char = input(input_string)
            if char not in '+-/*':
                print('Не правильно!')
                continue
            logger.log(char, 'ValueError')
            return char

        except ValueError:
            logger.log(char, 'ValueError')
            print('Это не то ...')


def get_selection(input_string: str) -> int:
    '''
    Проверка числа для выбора результата
    '''
    while True:
        try:
            char = input(input_string)
            if char in '123':
                return int(char)
            logger.log(char, 'ValueError')
            print('Не правильно!')
            continue
        except ValueError:
            logger.log(char, 'ValueError')
            print('Это не то ...')


def get_zero_division_error(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if num2 == 0.0:
        return False
    else:
        return True


def complex_get_zero_division_error(a_re, a_im, b_re, b_im):
    x = 0
    y = 0
    x = complex(a_re, a_im)
    y = complex(b_re, b_im)
    if y == 0:
        return False
    else:
        return True


'''
Нумератор для удобства отображения чисел в контроллере
'''


def num_to_word(num: str) -> str:

    if num == 1:
        return 'первого'
    elif num == 2:
        return 'второго'
    else:
        print('Метод может принимать только 1 или 2, проверьте что приходит в метод num_to_word ')
        logger.log(
            num, 'Метод может принимать только 1 или 2, проверьте что приходит в метод num_to_word ')
        exit()


def zero_division_check(def_part):
    try:
        def_part
    except ZeroDivisionError:
        if ZeroDivisionError:
            print('') 