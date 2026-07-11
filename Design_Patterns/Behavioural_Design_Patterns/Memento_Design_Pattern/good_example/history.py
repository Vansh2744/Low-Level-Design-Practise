from text_memento import TextMemento
from text_editor import TextEditor

class History:
    def __init__(self):
        self.history = []

    def save_state(self, tm:TextMemento):
        self.history.append(tm)
        TextEditor().text = self.history[-1]

    def undo(self):
        self.history.pop()

    def display_main_text(self):
        if len(self.history) > 0:
            print(self.history[-1].display_text())