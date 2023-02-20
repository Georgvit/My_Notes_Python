class NotesController:
    noteslist = []
    test = {}

    def createNote(self, notes):
        self.test = {"id": notes.count, 'date': notes.date, 'topic': notes.topic, 'text': notes.text}
        self.noteslist.append(self.test)
        self.encrypted(self.test)

    def printNote(self):
        self.readText()
        # for s in range(len(self.noteslist)):
        #     self.printTest(self.noteslist[s])



    def printTest(self,test):
        print(f"id: {test.get('id')} \nДата создания: {test.get('date')}\n"
              f"Тема: {test.get('topic')}\nТекст: {test.get('text')}\n")


    def encrypted(self,test):
        text = (f"id:{test.get('id')};date:{test.get('date')};"
              f"topic:{test.get('topic')};text:{test.get('text')}\n")
        # Создаем и открываем файлы для записи оригинального текста
        o_text = open('original_text.csv', 'a+')

        # Записываем данные в файл и закрываем их
        o_text.write(text)
        o_text.close()

    def readText(self):
        with open('original_text.csv', 'r') as file:
            for line in file.readlines():
                listtest = list(line.split(";"))
                for s in listtest:
                    t = s.split(':')
                    for e in range(len(t)):
                        if t[e] == 'id':
                            print(t[e + 1])
                        if t[e] == 'date':
                            print(t[e + 1])
                        if t[e] == 'topic':
                            print(t[e + 1])
                        if t[e] == 'text':
                            print(t[e + 1])



