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
        if self.sizeFile():
            if id != None:
                self.readFileAndPrintTextNoteId(id)
            elif self.trueFile():
                self.readFileAndPrintTextNote()
            else:
                for s in range(len(self.noteslist)):
                    self.printTextNote(self.noteslist[s])
        else:
            print('Записи в файле отсутствуют!')

    #  Вывод по дате
    def outputByDate(self, dateSt, dateFin):
        if self.sizeFile():
            if dateSt != '':
                self.readFileAndPrintTextNoteDate(dateSt, dateFin)
            else:
                print('Некорректный ввод')
        else:
            print('Записи в файле отсутствуют!')

    # Обновление данных
    def dataUpdate(self, id, comand):
        if self.sizeFile():
            if id != '':
                self.upateTextNote(id, comand)
            else:
                print('Не корректный ID')
        else:
            print('Записи в файле отсутствуют!')

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

    # Запись обновленных данных в файл
    def updateFileAndWriteText(self, templist):

        for tmp in templist:
            text = (f"id:{tmp.get('id')};date:{tmp.get('date')};"
                    f"topic:{tmp.get('topic')};text:{tmp.get('text')}")
            # Создаем и открываем файлы для записи обновленного текста
            tempFile = open('BD_NOTES.csv', 'a+')
            # Записываем данные в файл и закрываем их
            tempFile.writelines(text)
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

    # Чтение файла и вывод в консоль
    def readFileAndPrintTextNoteId(self, id):
        with open('BD_NOTES.csv', 'r') as file:
            for line in file.readlines():
                temp_count = 0
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
                    break
                else:
                    temp_count += 1
        if temp_count > 0:
            print('Нет записи с таким ID')

    # Чтение файла и вывод в консоль по дате
    def readFileAndPrintTextNoteDate(self, dateStart, dateFinal):
        with open('BD_NOTES.csv', 'r') as file:
            stopCycle = True
            startCycle = False
            for line in file.readlines():
                testr = re.split(":|;", line)
                if testr[3] == dateFinal:
                    noteslist = list(line.split(";"))
                    for s in noteslist:
                        t = s.split(':')
                        for e in range(len(t)):
                            if t[e] == 'id':
                                stopCycle = False
                if testr[3] == dateStart:
                    noteslist = list(line.split(";"))
                    for s in noteslist:
                        t = s.split(':')
                        for e in range(len(t)):
                            if t[e] == 'id':
                                startCycle = True
                if startCycle:
                    if stopCycle:
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

    #  Обновление записи
    def upateTextNote(self, id, comand):
        templist = []
        with open('BD_NOTES.csv', 'r') as file:
            for line in file.readlines():
                line.replace('\n', '')
                idTemp = None
                dataTemp = None
                topicTemp = None
                textTemp = None
                testr = re.split(":|;", line)
                noteslist = list(line.split(";"))
                if testr[1] == id:
                    noteslist = list(line.split(";"))
                    for s in noteslist:
                        t = s.split(':')
                        for e in range(len(t)):
                            if t[e] == 'id':
                                idTemp = t[e + 1]
                            if t[e] == 'date':
                                dataTemp = t[e + 1]
                            if t[e] == 'topic':
                                if comand == 'topic':
                                    topicTemp = input('Введите новую тему записи: ')
                                else:
                                    topicTemp = t[e + 1]
                            if t[e] == 'text':
                                if comand == 'text':
                                    textTemp = input('Введите новый текст записи: ') + '\n'
                                else:
                                    textTemp = t[e + 1]
                    notesDictionary = {"id": idTemp, 'date': dataTemp, 'topic': topicTemp,
                                       'text': textTemp}
                    templist.append(notesDictionary)
                else:
                    for s in noteslist:
                        t = s.split(':')
                        for e in range(len(t)):
                            if t[e] == 'id':
                                idTemp = t[e + 1]
                            if t[e] == 'date':
                                dataTemp = t[e + 1]
                            if t[e] == 'topic':
                                topicTemp = t[e + 1]
                            if t[e] == 'text':
                                textTemp = t[e + 1]
                    notesDictionary = {"id": idTemp, 'date': dataTemp, 'topic': topicTemp,
                                       'text': textTemp}
                    templist.append(notesDictionary)
        self.clearingFile()
        self.updateFileAndWriteText(templist)

    # Проверяем и парсим id последней записи
    def readFile(self):
        with open('BD_NOTES.csv', 'r') as file:
            for line in file.readlines():
                noteslist = list(line.split(";"))
                for s in noteslist:
                    t = s.split(':')
                    for e in range(len(t)):
                        if t[e] == 'id':
                            self.idUser = int(t[e + 1])

    # Получаем номер id последней записи
    def getFinalId(self):
        if self.trueFile():
            self.readFile()
            self.idUser += 1
        else:
            self.idUser += 1
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
