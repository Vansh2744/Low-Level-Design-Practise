from history import History
from text_editor import TextEditor
from text_memento import TextMemento

te = TextEditor()
his = History()

te.write("Hello")
his.save_state(te.save())
te.write(" World")
his.save_state(te.save())

his.display_main_text()
his.undo()
his.display_main_text()