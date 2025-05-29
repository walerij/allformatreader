# класс считывания данных из файла с расширением txt

class Txtreader():
    def __init__(self):
        pass

    def extact_text(self, file):
        text = ""
        try:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            text=e
        return text
