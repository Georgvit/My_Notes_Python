import datetime

from src.controllers.NotesController import NotesController
from src.model.Notes import Notes
from src.view.NotesCommands import NotesCommands


class NotesView:

    def run(self):
        while True:
            self.greeting()
            inputComand = input('Введите команду: ').upper()
            if inputComand == NotesCommands.EXIT.value:
                exit()

            match inputComand:
                case 'CREATE':
                    topic = input("Введите тему записи:")
                    text = input("Введите текси записи:")
                    date = datetime.date.today()
                    notes = Notes(date, topic, text)
                    notesCont = NotesController()
                    notesCont.createNote(notes)

                case 'READ':
                    notesCont.printNote()


    def greeting(self):
        print("\nСписок команд записной книги: \n",
              NotesCommands.CREATE.value, "- создание новой записи. \n",
              NotesCommands.READ.value, "- чтение записи по ID. \n",
              NotesCommands.UPDATE.value, "- обновление записи. \n",
              NotesCommands.LIST.value, "- вывод всех записей. \n",
              NotesCommands.DELETE.value, "- удаление записей. \n",
              NotesCommands.EXIT.value, "- выход из программы. \n")

