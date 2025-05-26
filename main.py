import argparse, os, os.path
from pathlib import Path
from utils.txtreader import Txtreader
from utils.docreader import Docreader
def main():
    parser = argparse.ArgumentParser(description="allformatreader - считывает данные всех форматов в текст через консоль")
    parser.add_argument("--file", help="Путь к обрабатываемому файлу")
    parser.add_argument("--path", help="Каталог, где хранятся обрабатываемые файлы ")
    #parser.add_argument("--clean", action="store_true", help="Очистка текста")
    args = parser.parse_args()

    txt_ = Txtreader()
    doc_ = Docreader()


    #если параметр  - файл
    if args.file:
        result_text = ""
        extension = Path(args.file).suffix # получаем расширение файла
        if extension==".txt":
            result_text = txt_.extact_text(args.file)
        elif extension==".docx":
            result_text = doc_.extact_text_docx(args.file)
        elif extension == ".doc":
            result_text = doc_.extact_text_doc(args.file)

        print(result_text)

    elif args.path:
        #получаем имена файлов директории
        print(args.path)








if __name__ == "__main__":
    main()