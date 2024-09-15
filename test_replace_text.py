import sys

def split_and_sort_text(text): # функция для разделения и сортировки текста
    text = text.split(" ")
    print(text)
    sorted_text = sorted(text, key=str.lower) # сортировка по алфавиту без учета регистра
    
    print(sorted_text)
    return sorted_text

def replace_e_to_i(text):
    new_text = []
    for word in text:
        new_text.append(word.replace('е', 'и').replace('Е', 'И'))
    print(new_text)
    return " ".join(new_text)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)
        return text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    source_file = sys.argv[1]
    destination_file = sys.argv[2]

    # Чтение всего содержимого исходного файла
    content = read_file(source_file)
    mass_text = split_and_sort_text(content)
    text_editing = replace_e_to_i(mass_text)

    # Запись содержимого в новый файл
    with open(destination_file, 'w', encoding='utf-8') as destination:
        destination.write(text_editing)