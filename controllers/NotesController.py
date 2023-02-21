import os.path
import re
class NotesController:
    noteslist = []
    notesDictionary = {}
    idUser = 0

    # Создание массива данных
    def createNote(self, notes):
        self.notesDictionary = {"id": notes.id, 'date': notes.date, 'topic': notes.topic, 'text': notes.text}
        self.noteslist.append(self.notesDictionary)
        self.createFileAndWriteText(self.notesDictionary)

    # Вывод данных
    def dataOutput(self, id):
        if id != None:
            self.readFileAndPrintTextNoteId(id)
        elif self.trueFile():
            self.readFileAndPrintTextNote()
        else:
            for s in range(len(self.noteslist)):
                self.printTextNote(self.noteslist[s])

    # Выводим записи в консоль
    def printTextNote(self, notesDictionary):
        print(f"id: {notesDictionary.get('id')} \nДата создания: {notesDictionary.get('date')}\n"
              f"Тема: {notesDictionary.get('topic')}\nТекст: {notesDictionary.get('text')}\n")


    # Создаем и записываем данные в файл
    def createFileAndWriteText(self, notesDictionary):
        text = (f"id:{notesDictionary.get('id')};date:{notesDictionary.get('date')};"
              f"topic:{notesDictionary.get('topic')};text:{notesDictionary.get('text')}\n")
        # Создаем и открываем файлы для записи текста
        tempFile = open('BD_NOTES.csv', 'a+')
        # Записываем данные в файл и закрываем их
        tempFile.write(text)
        tempFile.close()

    # Читаем и выводим данные из файла
    def readFileAndPrintTextNote(self):
        with open('BD_NOTES.csv', 'r') as file:
            for line in file.readlines():
                noteslist = list(line.split(";"))
                for s in noteslist:
                    t = s.split(':')
                    for e in range(len(t)):
                        if t[e] == 'id':
                            self.idUser = t[e + 1]
                            print(f"id: {t[e + 1]}")
                        if t[e] == 'date':
                            print(f"Дата создания: {t[e + 1]}")
                        if t[e] == 'topic':
                            print(f"Тема: {t[e + 1]}")
                        if t[e] == 'text':
                            print(f"Текст: {t[e + 1]}")

    def readFileAndPrintTextNoteId(self,id):
        with open('BD_NOTES.csv', 'r') as file:
            for line in file.readlines():
                testr = re.split(":|;", line)
                if testr[1] == id:
                    noteslist = list(line.split(";"))
                    for s in noteslist:
                        t = s.split(':')
                        for e in range(len(t)):
                            if t[e] == 'id':
                                self.idUser = t[e + 1]
                                print(f"id: {t[e + 1]}")
                            if t[e] == 'date':
                                print(f"Дата создания: {t[e + 1]}")
                            if t[e] == 'topic':
                                print(f"Тема: {t[e + 1]}")
                            if t[e] == 'text':
                                print(f"Текст: {t[e + 1]}")



    # Проверяем и парсим id последней записи
    def readFile(self):
        with open('BD_NOTES.csv', 'r') as file:
            for line in file.readlines():
                noteslist = list(line.split(";"))
                for s in noteslist:
                    t = s.split(':')
                    for e in range(len(t)):
                        if t[e] == 'id':
                            self.idUser = t[e + 1]

    # Получаем номер id последней записи
    def getFinalId(self):
        self.readFile()
        return self.idUser

    # Проверяем существует ли файл
    def trueFile(self):
        return os.path.isfile('BD_NOTES.csv')

    # Проверяем есть ли записи в файле
    def sizeFile(self):
        if os.path.isfile('BD_NOTES.csv'):
            return os.path.getsize('BD_NOTES.csv')

    # Удаление всех записей
    def clearingFile(self):
        tempFile = open('BD_NOTES.csv', 'w+')
        tempFile.seek(0)
        tempFile.close()

    # Проверяем массив на наличие данных
    def boolNoteslist(self):
        if len(self.noteslist) > 0:
            return True
        else:
            return False




