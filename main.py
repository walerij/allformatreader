import argparse, os, os.path
from pathlib import Path
from utils.txtreader import Txtreader
from utils.docreader import Docreader
from utils.pdfreader import Pdfreader
def main():
    parser = argparse.ArgumentParser(description="allformatreader - считывает данные всех форматов в текст через консоль")
    parser.add_argument("--file", help="Путь к обрабатываемому файлу")
    parser.add_argument("--path", help="Каталог, где хранятся обрабатываемые файлы ")
    #parser.add_argument("--clean", action="store_true", help="Очистка текста")
    args = parser.parse_args()

    txt_ = Txtreader()
    doc_ = Docreader()
    pdf_ = Pdfreader()


    #если параметр  - файл
    if args.file:
        result_text = []
        result= parse_file_all_formats(args.file, doc_, pdf_, txt_)
        result_text.append([args.file, result])
        print(result_text)

    elif args.path:
        #получаем имена файлов директории
        result_text = []
        for root, _, files in os.walk(args.path):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
                result_text.append([file_path,parse_file_all_formats(file_path, doc_, pdf_, txt_)])


        print(result_text)


def parse_file_all_formats(file, doc_, pdf_, txt_):
    result_text = ""
    extension = Path(file).suffix  # получаем расширение файла
    if search_ext_txt(extension):
        result_text = txt_.extact_text(file)
    elif search_ext_office(extension):
        result_text = doc_.extact_text_docx(file)
    if search_ext_pdf(extension) == ".pdf":
        result_text = pdf_.extract_text_pdf(file)
    return result_text



#проверка, текстовый ли формат файла
def search_ext_txt(ext):
    exts = [".txt", ".cmd",".bat",".py",".cs",".html",".xml",".css"]
    if ext in exts:
        return True
    return False


#Проверка, не pdf ли формат
def search_ext_pdf(ext):
    exts = [".pdf"]
    if ext in exts:
        return True
    return False

#Проверка, не офисный ли формат ли формат
def search_ext_office(ext):
    exts = [".docx"]
    if ext in exts:
        return True
    return False

if __name__ == "__main__":
    main()