import sys
v = sys.version

from Tkinter import *
import tkFileDialog
from ScrolledText import *

root = Tk("Text Editor")
text = ScrolledText(root)

# add some color fam
text.configure(background='black')
text.configure(insertbackground = 'green')
text.configure(foreground='green')
text.configure(font=("Courier", 12))
text.grid()

# Saving a file
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    #savelocation = raw_input("[+] ")
    # Open a file function

def open1():
    filename = tkFileDialog.askopenfilename(title = "Select File")
    f = open(filename, 'r')
    return f.read()


# The copy funtion
def copy1():
    duple
# Create the menu bar
menubar = Menu(root)

# The file menu tab
file = Menu(menubar, tearoff = 0)
# The file commands
file.add_command(label = "Open", command = open1)
file.add_command(label = "Save", command = saveas)
file.add_separator()
file.add_command(label = "Exit", command = root.quit)

# The Edit menu tab
edit = Menu(menubar, tearoff = 0)
# The menu commands
edit.add_command(label = "Undo")
edit.add_command(label = "Redo")
edit.add_command(label = "Copy")
edit.add_command(label = "Paste")

# The view menu tab
view = Menu(menubar, tearoff = 0)
# The view commands
view.add_command(label = " Vertical Split")
view.add_command(label = "Horizontal Split")
view.add_separator()
view.add_command(label = "Word Wrap")
menubar.add_cascade(label ="File", menu = file)
menubar.add_cascade(label ="Edit", menu = edit)
menubar.add_cascade(label ="View", menu = view)
root.config(menu = menubar)
root.configure(background ='black')
root.title("My Creation")
root.mainloop()
