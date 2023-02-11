class Letter:
    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.body = []

    def addLine(self, line):
        self.body.append(line)

    def getText(self):
        letter = "Dear " + self.letterTo + ":\n\n"
        for line in self.body:
            letter += line + "\n"
        letter += "\nSincerely,\n\n" + self.letterFrom
        return letter


letter = Letter("Mary", "John")
letter.addLine("I am sorry we must part.")
letter.addLine("I wish you all the best.")
print(letter.getText())
