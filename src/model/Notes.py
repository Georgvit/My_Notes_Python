class Notes:
    count = 0

    def __init__(self, date, topic, text):
        Notes.count += 1
        self.date = date
        self.topic = topic
        self.text = text
