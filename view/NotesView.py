import datetime

from controllers.NotesController import NotesController
from model.Note import Note
from view.NotesCommands import NotesCommands


class NotesView:
    id = 0

    def run(self):
        while True:
            self.greeting()
            inputComand = input('Введите команду: ').upper()
            notesCont = NotesController()
            if inputComand == NotesCommands.EXIT.value:
                exit()

            match inputComand:
                case 'CREATE':
                    topic = input("Введите тему записи:")
                    text = input("Введите текси записи:")
                    date = datetime.date.today()
                    self.id = notesCont.getFinalId()
                    notes = Note(self.id, date, topic, text)
                    notesCont.createNote(notes)

                case 'UPDATE':
                    id = input("Введите номер записи: ")
                    self.litlMenu()
                    comandUpdat = input('Введите команду: ')
                    notesCont.dataUpdate(id, comandUpdat)

                case 'READ':
                    id = input("Введите номер записи:")
                    notesCont.dataOutput(id)
                case 'UNLOAD':
                    startDate = input("Введите начальную дату в формате гггг-мм-дд:")
                    finalDate = input("Введите конечную дату в формате гггг-мм-дд:")
                    notesCont.outputByDate(startDate, finalDate)

                case 'LIST':
                    notesCont.dataOutput(None)

                case 'DELETE':
                    notesCont.clearingFile()

    # Пользовательское меню
    def greeting(self):
        print("\nСписок команд записной книги: \n",
              NotesCommands.CREATE.value, "- создание новой записи. \n",
              NotesCommands.READ.value, "- чтение записи по ID. \n",
              NotesCommands.UNLOADING.value, "- выгрузка записей по дате. \n",
              NotesCommands.UPDATE.value, "- обновление записи. \n",
              NotesCommands.LIST.value, "- вывод всех записей. \n",
              NotesCommands.DELETE.value, "- удаление записей. \n",
              NotesCommands.EXIT.value, "- выход из программы. \n")

    def litlMenu(self):
        print("\nЧто изменить в существующей записи: \n",
              NotesCommands.TOPIC.value, "- изменить тему записи. \n",
              NotesCommands.TEXT.value, "- изменить текс записи. \n")
