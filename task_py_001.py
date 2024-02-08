# ДОМАШНЕЕ ЗАДАНИЕ К 05.02.2024
# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла
# в другой.
# _____________________________________________________________________________
# АЛГОРИТМ
# 1. Открыть и прочитать исходный файл.
# 2. Открыть файл, в который будут копироваться данные (если его нет, создать новый).
# 3. Считать данные из исходного файла.
# 4. Выбрать нужную строку по номеру строки, введенной пользователем.
# 5. Записать эту строку в целевой файл.
# _____________________________________________________________________________
# ПРИМЕЧАНИЯ
# Пользователь вводит номер строки, которую хочет скопировать из исходного файла.
# Код открывает исходный файл для чтения, читает все строки в память,
# выбирает нужную строку и записывает её в целевой файл.
# _____________________________________________________________________________
def copy_line(source_file, target_file, line_number):
    try:
        with open(source_file, 'r') as f_source:
            lines = f_source.readlines()
            # Проверяем, существует ли указанная строка
            if line_number < 1 or line_number > len(lines):
                print("Ошибка: указанной строки не существует.")
                return
            line_to_copy = lines[line_number - 1]  # -1, так как индексация начинается с 0
            with open(target_file, 'a') as f_target:
                f_target.write(line_to_copy)
            print("Строка успешно скопирована.")
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")


if __name__ == "__main__":
    source_file = input("Введите имя исходного файла: ")
    target_file = input("Введите имя целевого файла: ")
    line_number = int(input("Введите номер строки для копирования: "))

    copy_line(source_file, target_file, line_number)
