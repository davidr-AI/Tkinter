from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfile
from PyPDF2 import PdfFileReader


# =================open file method======================
def openFile():
    file = askopenfilename(defaultextension=".pdf",
                           filetypes=[("Pdf files", "*.pdf")])
    if file == "":
        file = None
    else:
        fileEntry.delete(0, END)
        fileEntry.config(fg="black")
        fileEntry.insert(0, file)


def convert():
    try:
        pdf = fileEntry.get()
        pdfFile = open(pdf, 'rb')
        # creating a pdf reader object
        pdfReader = PdfFileReader(pdfFile)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        extractedText = pageObj.extractText()
        readPdf.delete(1.0, END)
        readPdf.insert(INSERT, extractedText)

        # closing the pdf file object
        pdfFile.close()
    except FileNotFoundError:
        fileEntry.delete(0, END)
        fileEntry.config(fg="red")
        fileEntry.insert(0, "Please select a pdf file first")
    except:
        pass


def save2word():
    text = str(readPdf.get(1.0, END))
    wordfile = asksaveasfile(mode='w', defaultextension=".doc",
                             filetypes=[("word file", "*.doc"),
                                        ("text file", "*.txt"),
                                        ("Python file", "*.py")])

    if wordfile is None:
        return
    wordfile.write(text)
    wordfile.close()
    print("saved")
    fileEntry.delete(0, END)
    fileEntry.insert(0, "pdf Extracted and Saved...")


# =================== Front End Design
root = Tk()
root.geometry("600x350")
root.config(bg="black")
# root.title("PDF Converter")
root.resizable(0, 0)

defaultText = "\n\n\n\n\t\t Your extracted text will appear here.\n \t\tYou can also modify the extracted text."
# ==============App Name==============================================================>>
appName = Label(root, text="PDF to Word, Txt or Python file Converter ", font=('arial', 20, 'bold'),
                bg="black", fg='white')
appName.place(x=20, y=5)
# Select pdf file
labelFile = Label(root, text="Select Pdf File", font=('arial', 12, 'bold'), bg='black', fg='white')
labelFile.place(x=30, y=50)
fileEntry = Entry(root, font=('Arial', 12), width=40)
fileEntry.pack(ipadx=200, pady=50, padx=150)
# ===========button to access openFile method=================================
openFileButton = Button(root, text=" Open ", font=('arial', 10, 'bold'), width=36,
                        bg="blue", fg='white', command=openFile)
openFileButton.place(x=150, y=80)
# ===========button to access convert method=================================
convert2Text = Button(root, text="Read Your File", font=('arial', 10, 'bold'),
                      bg="blue", fg='WHITE', width=20, command=convert)
convert2Text.place(x=221, y=120)
# ======================= Text Box to read pdf file and modify ===================>>
readPdf = Text(root, font=('Arial', 12), fg='black', bg='white', width=60, height=30, bd=10)
readPdf.pack(padx=30, ipadx=30, pady=30, ipady=30)
readPdf.insert(INSERT, defaultText)
# ===============================Button to access save2word method=================
save2Word = Button(root, text="Save Your File", font=('arial', 10, 'bold'),
                   bg="BLUE", fg='WHITE', command=save2word)
save2Word.place(x=245, y=320)

# ===================halt window=============================>>
if __name__ == "__main__":
    root.mainloop()
