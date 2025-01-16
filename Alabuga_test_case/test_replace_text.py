import sys

def read_file(file_path): # функция для чтения исходного файла и передачи содержимого текста для обработки
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)
        return text

def split_and_sort_text(text): # функция для разделения текста на слова и сортировки списка
    text = text.split(" ")
    print(text)
    sorted_text = sorted(text, key=str.lower) # сортировка по алфавиту без учета регистра
    print(sorted_text)
    return sorted_text

def replace_e_to_i(text): # функция для замены букв "е" на "и"
    new_text = []
    for word in text:
        new_text.append(word.replace('е', 'и').replace('Е', 'И')) # замена "е" на "и" сохраняя регистр буквы
    print(new_text)
    return " ".join(new_text)

if __name__ == "__main__": # основная функция
    if len(sys.argv) != 3: # проверка количества аргументов
        print("Вызовите скрипт с аргументами по типу: python script.py input.txt output.txt") # сообщение об ошибке
        sys.exit(1) # выход из программы

    source_file = sys.argv[1] # получение имени исходного файла
    destination_file = sys.argv[2] # получение имени выходного файла

    # Чтение всего содержимого исходного файла
    content = read_file(source_file) # получение содержимого исходного файла
    mass_text = split_and_sort_text(content) # разделение текста и сортировка слов по алфавиту в списке
    text_editing = replace_e_to_i(mass_text) # замена букв "е" на "и" и сборка обработанного текста

    # Запись содержимого в новый файл
    with open(destination_file, 'w', encoding='utf-8') as destination:
        destination.write(text_editing)