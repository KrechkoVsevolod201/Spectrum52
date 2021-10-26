from tkinter import *  # Note: lower case "t" in tkinter
from tkinter import font as tkFont  # for convenience
# you don't have to use Helvetica or bold, this is just an example
import os

# import filedialog module
from tkinter import filedialog

# Create the root window
root = Tk()
helv36 = tkFont.Font(family='Helvetica', size=18, weight='bold')
# Set window title
root.title('File Explorer')

# Set window size
root.geometry("400x200")

# Set window background color
root.config(background="gray")

# Create a File Explorer label
label_file_explorer = Label(root,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

# Cleaning file
my_file = open("AssistFiles\FileWay.txt", "w+")
my_file.close()


# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Image",
                                                      "*.jpg*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)

    # Create filename txt
    my_file = open("AssistFiles\FileWay.txt", "w+")
    my_file.write(filename)
    my_file.close()

# Spectrum start class
def startSpectrum1():
    os.system('python spectrum1.py')

# Help
def helpText():
    main = Tk()
    f = open('AssistFiles/Help.txt', 'r')
    filename = f.read()
    ourMessage = filename
    print(filename)
    messageVar = Message(main, text=ourMessage)
    messageVar.config(bg='lightgreen')
    messageVar['font'] = helv36
    messageVar.pack()
    main.mainloop()

# top menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open...', command=browseFiles)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_command(label='Help', command=helpText)


# Start button
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
startRegularProgramButton = Button(frame, text = 'Start program', fg ='red', command=startSpectrum1)
startRegularProgramButton['font'] = helv36
startRegularProgramButton.pack( side = LEFT)

# File label
label_file_explorer.pack(side = LEFT)

root.mainloop()