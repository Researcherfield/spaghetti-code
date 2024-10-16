import matplotlib.pyplot as plt

# Функція для перевірки, чи введені дані є числами
def is_valid_number(s):
    try:
        return int(s)
    except ValueError:
        return None

# Вводимо номери шкарпеток і перетворюємо їх у список цілих чисел
user_input = input("Введіть номери шкарпеток через пробіл: ").split()
socks = list(filter(lambda x: x is not None, map(is_valid_number, user_input)))

# Однорядковий код для знаходження унікальних шкарпеток
unique_socks = sorted(set(socks) - {x for x in socks if socks.count(x) > 1})

# Візуалізація даних у вигляді стовпців
plt.bar(range(len(unique_socks)), unique_socks)
plt.xlabel("Індекси")
plt.ylabel("Номери унікальних шкарпеток")
plt.title("Загублені шкарпетки")
plt.show()
