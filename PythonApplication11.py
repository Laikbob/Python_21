import tkinter as tk
import random

# Функция для генерации случайной карты
def loe_kaart():
    return random.choice(range(2, 12))  # Генерация карты в диапазоне 2–11

# Функция для расчёта результата
def arvuta_tulemus(mangija_summa, arvuti_summa):
    if mangija_summa > 21:
        return "Проиграл!"
    elif arvuti_summa > 21 or mangija_summa > arvuti_summa:
        return "Выиграл!"
    elif mangija_summa == arvuti_summa:
        return "Ничья!"
    else:
        return "Проиграл!"

# Функция для сохранения результата в файл
def salvesta_tulemus(nimi, tulemus, punktid):
    with open("tulemused.txt", "a", encoding="utf-8") as f:
        f.write(f"{nimi}: {tulemus} ({punktid} очков)\n")

# Функция для отображения истории игр
def näita_ajalugu():
    try:
        # Попытка открыть файл с историей игр
        with open("tulemused.txt", "r", encoding="utf-8-sig", errors="ignore")as f:
            # Создаём новое окно для отображения истории
            ajalugu_aken = tk.Toplevel(root)
            ajalugu_aken.title("История игр")  # Заголовок окна
            ajalugu_aken.geometry("400x300")  # Размер окна
            tk.Label(ajalugu_aken, text="История игр", font=("Arial", 14, "bold")).pack(pady=10)  # Заголовок
            # Текстовое поле для отображения истории
            ajalugu_tekst = tk.Text(ajalugu_aken, wrap="word", font=("Arial", 12))
            ajalugu_tekst.insert("1.0", f.read())  # Вставляем содержимое файла в текстовое поле
            ajalugu_tekst.config(state="disabled")  # Делает текст недоступным для редактирования
            ajalugu_tekst.pack(padx=10, pady=10, fill="both", expand=True)  # Отображаем текстовое поле
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение
        tk.Label(root, text="История отсутствует.", font=("Arial", 12, "italic"), fg="red").pack()
    except UnicodeDecodeError as e:
        # Если ошибка кодировки, выводим сообщение об ошибке
        print(f"Ошибка кодировки: {e}")
        tk.Label(root, text="Ошибка при чтении файла. Проверьте кодировку.", font=("Arial", 12, "italic"), fg="red").pack()

# Функция для игры компьютера
def mängi_arvuti():
    arvuti_summa = 0
    # Компьютер тянет карты, пока сумма не станет 17 или больше
    while arvuti_summa < 17:
        arvuti_summa += loe_kaart()
    return arvuti_summa

# Функция для начала новой игры
def alusta_mang():
    global mangija_summa, kaardid  # Используем глобальные переменные для хранения данных о сумме и картах
    mangija_summa = 0  # Начальная сумма карт игрока
    kaardid = []  # Пустой список для карт игрока
    võta_kaart()  # Даем первую карту

# Функция для взятия карты игроком
def võta_kaart():
    global mangija_summa  # Используем глобальную переменную для хранения суммы карт
    kaart = loe_kaart()  # Генерируем карту
    kaardid.append(kaart)  # Добавляем карту в список карт игрока
    mangija_summa += kaart  # Увеличиваем сумму карт игрока
    uuenda_seis()  # Обновляем отображение состояния игры
    if mangija_summa > 21:  # Если сумма карт игрока больше 21, то игра заканчивается
        lopeta_mang()

# Функция для остановки игры
def peatu():
    lopeta_mang()  # Останавливаем игру, вызывая завершение

# Функция для завершения игры
def lopeta_mang():
    arvuti_summa = mängi_arvuti()  # Получаем сумму карт компьютера
    tulemus = arvuta_tulemus(mangija_summa, arvuti_summa)  # Рассчитываем результат игры
    mangija_nimi = nimi_sisestus.get()  # Получаем имя игрока
    if not mangija_nimi:  # Если имя не введено, ставим "Неизвестный"
        mangija_nimi = "Неизвестный"
    salvesta_tulemus(mangija_nimi, tulemus, mangija_summa)  # Сохраняем результат в файл
    # Обновляем результат на экране
    tulemus_silt.config(text=f"{tulemus}\nТвои очки: {mangija_summa}, Компьютер: {arvuti_summa}", fg="green" if "Выиграл" in tulemus else "red")

# Функция для обновления состояния игры
def uuenda_seis():
    seis_silt.config(text=f"Твои карты: {kaardid} (Сумма: {mangija_summa})")  # Обновляем отображение карт и суммы

# Создание основного окна игры
root = tk.Tk()
root.title("Игра 21") 
root.geometry("600x500")
root.configure(bg="#2C3E50")

# Заголовок игры
pealkiri = tk.Label(root, text="Добро пожаловать в игру 21!", font=("Arial", 18, "bold"), bg="#2C3E50", fg="#ECF0F1")
pealkiri.pack(pady=10)

# Поле ввода имени игрока
nimi_silt = tk.Label(root, text="Введите своё имя:", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1")
nimi_silt.pack(pady=5)
nimi_sisestus = tk.Entry(root, font=("Arial", 12))  # Поле для ввода имени
nimi_sisestus.pack(pady=5)

# Строка состояния игры
seis_silt = tk.Label(root, text="Начни игру!", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1")
seis_silt.pack(pady=20)

# Строка для отображения результата игры
tulemus_silt = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#2C3E50")
tulemus_silt.pack(pady=10)

nupu_stiil = {"font": ("Arial", 12, "bold"), "bg": "#3498DB", "fg": "#ECF0F1", "activebackground": "#2980B9", "width": 15, "pady": 5}

# Кнопки
alusta_nupp = tk.Button(root, text="Начать игру", command=alusta_mang, **nupu_stiil)  # Кнопка для начала игры
alusta_nupp.pack(pady=5)

võta_nupp = tk.Button(root, text="Взять карту", command=võta_kaart, **nupu_stiil)  # Кнопка для взятия карты
võta_nupp.pack(pady=5)

peatu_nupp = tk.Button(root, text="Стоп", command=peatu, **nupu_stiil)  # Кнопка для остановки игры
peatu_nupp.pack(pady=5)

ajalugu_nupp = tk.Button(root, text="Показать историю", command=näita_ajalugu, **nupu_stiil)  # Кнопка для показа истории
ajalugu_nupp.pack(pady=5)

# Запуск графического интерфейса
root.mainloop()