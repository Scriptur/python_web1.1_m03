import time
from multiprocessing import  Pool, cpu_count


def factorize(number):
    number_list = []
    for num in range(1, number+1):
        if number % num == 0:
            number_list.append(num)
    print(f'Список чисел без остачі {number_list}')

#  Синхронний запуск
def synchron_factorize(*numbers):  
    start = time.time()
    result = []
    for num in numbers:
        print(f'Для числа: {num}')
        for i in range(1, num+1):
            if num % i == 0:
                result.append(i)
        print(f'Список чисел що діляться без остачі {result}')
        result = []
    return print(f'Час роботи функции {time.time() - start}')

# Багатопроцесорний запуск
def factorize_pool(*numbers):  
    start = time.time()
    print(f'Кількість процесорів {cpu_count()}')
    with Pool(cpu_count()) as pool:
        for i in numbers:
            print(f'Для числа: {i}')
            pool.apply_async(factorize(i))

    pool.close()
    pool.join()
    return print(f'Час роботи функції {time.time() - start}')


if __name__ == '__main__':
    print('=========================================================')
    print('Синхронний запуск:')
    synchron_factorize(128, 255, 99999, 10651060)
    print('=========================================================')
    print('Багатопроцесорний запуск:')
    factorize_pool(128, 255, 99999, 10651060)
    