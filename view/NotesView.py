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
                    topic = input("Введите тему записи:")
                    text = input("Введите текси записи:")
                    date = datetime.date.today()
                    self.id = notesCont.getFinalId()
                    notes = Note(self.id, date, topic, text)
                    notesCont.createNote(notes)

                case 'READ':
                    id = input("Введите номер записи:")
                    if notesCont.sizeFile():
                        notesCont.dataOutput(id)
                    elif notesCont.boolNoteslist():
                        notesCont.dataOutput()
                    else:
                        print('Записи в файле отсутствуют!')

                case 'LIST':
                    if notesCont.sizeFile():
                        notesCont.dataOutput(None)
                    elif notesCont.boolNoteslist():
                        notesCont.dataOutput()
                    else:
                        print('Записи в файле отсутствуют!')
                case 'DELETE':
                    notesCont.clearingFile()

    # Пользовательское меню
    def greeting(self):
        print("\nСписок команд записной книги: \n",
              NotesCommands.CREATE.value, "- создание новой записи. \n",
              NotesCommands.READ.value, "- чтение записи по ID. \n",
              NotesCommands.UPDATE.value, "- обновление записи. \n",
              NotesCommands.LIST.value, "- вывод всех записей. \n",
              NotesCommands.DELETE.value, "- удаление записей. \n",
              NotesCommands.EXIT.value, "- выход из программы. \n")
