class Editor:
    def __init__(self):
        self.text_arr = []
        self.write_text = ""

    def write(self, text):
        self.write_text += text
        self.text_arr.append(self.write_text)

    def undo(self):
        self.text_arr.pop()

    def show(self):
        print(self.text_arr[-1])

editor = Editor()

editor.write("Hello")
editor.write(" My")
editor.write(" Name")
editor.write(" is")
editor.write(" Vansh")

editor.show()

editor.undo()
editor.undo()

editor.show()