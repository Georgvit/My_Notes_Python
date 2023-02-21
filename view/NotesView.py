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
                    if notesCont.trueFile():
                        self.id = int(notesCont.getFinalId()) + 1
                    else:
                        self.id += 1
                    notes = Note(self.id, date, topic, text)
                    notesCont.createNote(notes)

                case 'READ':
                    if notesCont.sizeFile():
                        notesCont.dataOutput()
                    elif notesCont.boolNoteslist():
                        notesCont.dataOutput()
                    else:
                        print('Записи в файле отсутствуют!')

                case 'LIST':
                    notesCont.dataOutput()
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
