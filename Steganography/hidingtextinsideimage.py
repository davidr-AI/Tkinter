from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb


def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select an Image File",
                                          filetype=(("PNG file", "*.png"),
                                                    ("JPG File", "*.jpg"), ("All File", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    label1.configure(image=img, width=250, height=250)
    label1.image = img
    print("")


def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)


def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


def save():
    secret.save("hiddentext.png")


root = Tk()

blank_space = " "
root.title(80 * blank_space + "Hiding Text in an Image")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="black")

# logo
logo = PhotoImage(file="maxresdefault.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

logo1 = PhotoImage(file="maxresdefault.png")
Label(root, image=logo1, bg="#2f4155").place(x=600, y=0)

Label(root, text="STEGANOGRAPHY", bg="black", fg="white", font="arial 20 bold").place(x=250, y=20)

frame1 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
frame1.place(x=10, y=80)

label1 = Label(frame1, bg="black")
label1.place(x=40, y=10)

frame2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

# scrollbar
scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3 = Frame(root, bd=3, bg="black", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

# Buttons
Button(frame3, text="Open an Image", width=12, height=2, font="arial 10 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save the Image", width=12, height=2, font="arial 10 bold", command=save).place(x=180, y=30)

frame4 = Frame(root, bd=3, bg="black", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

# Buttons
Button(frame4, text="Hide Text", width=12, height=2, font="arial 10 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show the Text", width=12, height=2, font="arial 10 bold", command=Show).place(x=180, y=30)
root.mainloop()
