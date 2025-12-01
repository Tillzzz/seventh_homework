import threading
import queue
import time
import random

# Одна черга для чисел
q = queue.Queue()

# Функція споживача
def consumer(thread_id):
    while True:
        num = q.get()  # забираємо число з черги
        print(f"Thread {thread_id} отримав: {num}")
        time.sleep(num)  # очікування num секунд
        print(f"Thread {thread_id} завершив очікування {num} сек.")
        q.task_done()

# Функція генератора
def producer():
    for i in range(10):  # цикл на 10 ітерацій
        time.sleep(5)  # кожні 5 секунд
        num = random.randint(1, 10)
        print(f"Producer додав у чергу: {num}")
        q.put(num)

# Створення кількох робочих потоків
threads = []
for i in range(1, 4):  # 3 потоки
    t = threading.Thread(target=consumer, args=(i,))
    t.daemon = True
    t.start()
    threads.append(t)

# Потік керування
t_prod = threading.Thread(target=producer)

t_prod.start()   # запуск управляючого потоку
t_prod.join()    # чекаємо завершення генерації

q.join()         # чекаємо завершення усіх задач у черзі

print("End Main")