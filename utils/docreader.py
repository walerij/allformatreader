#класс считывания данных с файлов .doc или docx

from docx import Document
import mammoth


class Docreader():


    def __init__(self):
        pass

    def extact_text_docx(self, file):
        doc = Document(file)  # конвертируй .doc в .docx
        text = "\n".join([para.text for para in doc.paragraphs])
        return text


