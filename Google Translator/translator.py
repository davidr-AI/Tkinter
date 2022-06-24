from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

blank = " "
root = Tk()
root.title(100 * blank + "Google Translator -- Translate From English To Any Language")
root.geometry("1080x400")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# left box
combo1 = ttk.Combobox(root, font="Arial", values=languageV, state="r")
combo1.place(x=110, y=20)
combo1.set("English")

label1 = Label(root, text="ENGLISH", font="Arial", bg='blue', width=21, bd=5, relief=RAISED)
label1.place(x=110, y=50)

# right box
combo2 = ttk.Combobox(root, values=languageV, font='Arial', state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="Arial", bg='blue', width=21, bd=5, relief=RAISED)
label2.place(x=730, y=50)

# first frame
f1 = Frame(root, bg="white", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Arial", bg="white", fg="blue", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# 2nd frame
f2 = Frame(root, bg="white", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Arial", bg="white", fg="blue", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate button
translate = Button(root, text="TRANSLATE", font=("Arial", 12), activebackground="blue",
                   cursor="heart", bd=1, width=10, height=2, bg="red",
                   fg="black", command=translate_now)
translate.place(x=476, y=200)

label_change()

root.config(bg="black")
root.mainloop()
