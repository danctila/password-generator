import string
import random
import tkinter as tk
from tkinter import ttk

# window creator
window = tk.Tk()
window.title('Password Generator')
window.geometry('720x600')

# password generator


def PasswordGen():
    global length, output

    characterList = ""

    if (lettPrefButton.cget('text') == 'Yes'):
        characterList += string.ascii_letters
    if (numPrefButton.cget('text') == 'Yes'):
        characterList += string.digits
    if (symPrefButton.cget('text') == 'Yes'):
        characterList += string.punctuation

    password = []

    for i in range(length.get()):
        # Pick random character from character list for desired length
        password.append(random.choice(characterList))

    output.set("".join(password))


# global varibable initialization
length = tk.IntVar()
output = tk.StringVar()

# handles the button text change for letter preference


def lettPrefChange():
    if lettPrefButton.cget('text') == 'No':
        lettPrefButton.configure(text='Yes')
    else:
        lettPrefButton.configure(text='No')

# handles the button text change for number preference


def numPrefChange():
    if numPrefButton.cget('text') == 'No':
        numPrefButton.configure(text='Yes')
    else:
        numPrefButton.configure(text='No')

# handles the button text change for symbol preference


def symPrefChange():
    if symPrefButton.cget('text') == 'No':
        symPrefButton.configure(text='Yes')
    else:
        symPrefButton.configure(text='No')


# length widget creators
label = ttk.Label(master=window, text='Length?')
label.pack()

entry = ttk.Entry(master=window, textvariable=length)
entry.pack()

# letters widgets
lettPrefLabel = ttk.Label(master=window, text='Letters?')
lettPrefButton = ttk.Button(
    master=window, text='No', command=lettPrefChange)
lettPrefLabel.pack(pady=(10, 1))
lettPrefButton.pack()

# Numbers widgets
numPrefLabel = ttk.Label(master=window, text='Numbers?')
numPrefButton = ttk.Button(
    master=window, text='No', command=numPrefChange)
numPrefLabel.pack(pady=(20, 1))
numPrefButton.pack()

# symbols widget
symPrefLabel = ttk.Label(master=window, text='Symbols?')
symPrefButton = ttk.Button(
    master=window, text='No', command=symPrefChange)
symPrefLabel.pack(pady=(20, 1))
symPrefButton.pack()

# output text
outputEntry = ttk.Entry(master=window, textvariable=output,
                        state='readonly', width='300')
outputEntry.pack(pady=(50, 1))

# password generator button
passGenButton = ttk.Button(
    master=window, text='Generate Password', command=PasswordGen)
passGenButton.pack()

# window loop
window.mainloop()
