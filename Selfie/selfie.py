from tkinter import *
import cv2
from PIL import Image, ImageTk

import time

blank_space = " "


class App:
    def __init__(self, video_source=0):

        self.title = (60 * blank_space + "Take A Selfie And Save To Your Folder")
        # app name
        self.appName = "Take A Selfie"
        # make the window
        self.window = Tk()
        # saving the title
        self.window.title(self.title)
        # not resizeable
        self.window.resizable(0, 0)

        self.window['bg'] = 'black'
        self.video_source = video_source

        # create the label
        self.vid = MyVideoCapture(self.video_source)
        self.label = Label(self.window, text=self.appName, font=15,
                           bg='black', fg='white').pack(side=TOP, fill=BOTH)

        # Create a Canvas
        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height,
                             bg='black')
        self.canvas.pack()

        # Create Button to take the snapshot
        self.btn_snapshot = Button(self.window, text="CLICK", width=30, bg='white',
                                   fg='black', activebackground='red', command=self.snapshot)
        self.btn_snapshot.pack(anchor=CENTER, expand=True)
        self.update()
        self.window.mainloop()

    def snapshot(self):
        check, frame = self.vid.getFrame()
        if check:
            image = "IMG-" + time.strftime("%d-%m-%Y at %H-%M-%p") + ".jpg"

            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # show message on window that imsage has been saved
            msg = Label(self.window, text='Image Saved ' + image, bg='black', fg='blue',
                        ).place(x=0, y=30)

    def update(self):
        # Getting the frame from video source
        isTrue, frame = self.vid.getFrame()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.window.after(15, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Not able to open this Camera \n select another video source", video_source)

        # Getting the video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                # if  isTrue is true, then current frame converted to RGB
                return isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return isTrue, None
        else:
            return isTrue, None
        # release video source

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


if __name__ == '__main__':
    App()
