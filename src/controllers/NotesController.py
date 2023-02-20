class NotesController:
    noteslist = []
    test = {}

    def createNote(self, notes):
        self.test = {"id": notes.count, 'date': notes.date, 'topic': notes.topic, 'text': notes.text}
        self.noteslist.append(self.test)

    def printNote(self):
        for s in range(len(self.noteslist)):
            self.printTest(self.noteslist[s])


    def printTest(self,test):
        print(f"id: {test.get('id')} \nДата создания: {test.get('date')}\n"
              f"Тема: {test.get('topic')}\nТекст: {test.get('text')}")