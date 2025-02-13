from src.core import chek, calk, random_primer

def consol_version():
    random_example = random_primer()
    print(random_example)
    try:
        user_input = float(input('Введите ответ - '))
    except ValueError:
        print('вы ввели не число')
    else:
        answer = calk(random_example)
        result = chek(answer, user_input)
        print(result)


