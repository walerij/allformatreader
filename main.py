import argparse, os, os.path
from pathlib import Path
def main():
    parser = argparse.ArgumentParser(description="allformatreader - считывает данные всех форматов в текст через консоль")
    parser.add_argument("--file", help="Путь к обрабатываемому файлу")
    parser.add_argument("--path", help="Каталог, где хранятся обрабатываемые файлы ")
    #parser.add_argument("--clean", action="store_true", help="Очистка текста")
    args = parser.parse_args()

    #если параметр  - файл
    if args.file:
        extension = Path(args.file).suffix # получаем расширение файла
        print(extension) # печатаем его

    elif args.path:
        #получаем имена файлов директории
        print(args.path)








if __name__ == "__main__":
    main()