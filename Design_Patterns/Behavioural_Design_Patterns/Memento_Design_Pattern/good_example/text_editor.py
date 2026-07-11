from text_memento import TextMemento

class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, txt):
        self.text += txt

    def save(self):
        return TextMemento(self.text)
    
    def return_text(self):
        return self.text