from moduls.sort_func import insertion_sort, merge_sort
from timeit import timeit
import random

#2500 - оптимальна кількість щоб побачити різницю
random_date = [random.randint(0, 1000) for _ in range(2500)]

#Вимірювання з виведенням в термінал
print("Час сортування вставкою:", timeit(lambda: insertion_sort(random_date.copy()), globals=globals(), number=10))
print("Час сортування злиттям: ", timeit(lambda: merge_sort(random_date.copy()), globals=globals(), number=10))
print("Вбудована функція: ", timeit(lambda: sorted(random_date.copy()), globals=globals(), number=10))