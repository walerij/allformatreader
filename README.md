
# 🧠 Программа allformatreader

Консольная утилита для чтения текста из файлов различных форматов на Python.  
Позволяет получать информацию и преобразовывать в текст из конкретного файла (аргумент --file) 
или из всех файлов в папках и подпапках по пути, указанном в аргументе --path

---

## 🚀 Возможности

- Получение текстовой информации из файлов .txt и подобных им
- Обработка файлов офисных приложений .docx, .odsx 
- Обработка формата .pdf


---

## ⚙️ Установка

```bash
git clone https://github.com/walerij/allformatreader.git
cd allformatreader
pip install -r requirements.txt
```

## ⚙️ Пример использования

#### Чтение из файла:
```
python allformatreader.py --file sample.txt 
```

#### Обработка всех файлов папки :
```
python allformatreader.py --path C:\123\path-to-files\ 
```