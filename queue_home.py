import threading
import queue
import time

# Створюємо 3 черги для робочих потоків
q1 = queue.Queue()
q2 = queue.Queue()
q3 = queue.Queue()

# Функція споживача
def consumer(q, thread_id):
    while True:
        msg = q.get()  # отримуємо словник із черги
        print(f"Thread {thread_id}: {msg}")
        q.task_done()  # повідомляємо що задача виконана

# Функція генератора
def producer():
    while True:
        try:
            n = int(input("Введіть номер потоку (1-3): "))
            if n not in (1, 2, 3):
                print("Невірний номер потоку!")
                continue

            text = input("Введіть повідомлення: ")
            msg = {"n": n, "t": text}

            # Кладемо повідомлення у потрібну чергу
            if n == 1:
                q1.put(msg)
            elif n == 2:
                q2.put(msg)
            else:
                q3.put(msg)

        except ValueError:
            print("Введіть число для номера потоку!")

# Створення робочих потоків
t1 = threading.Thread(target=consumer, args=(q1, 1), daemon=True)
t2 = threading.Thread(target=consumer, args=(q2, 2), daemon=True)
t3 = threading.Thread(target=consumer, args=(q3, 3), daemon=True)

# Створення управляючого потоку
t_prod = threading.Thread(target=producer, daemon=True)

# Запуск потоків
t1.start()
t2.start()
t3.start()
t_prod.start()

# Очікування управляючого потоку (вічний цикл)
t_prod.join()
