import tkinter
from tkinter import *


class noteListGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 1100  # canvas 가로 길이
        CANVAS_SIZE_HEIGHT = 750  # canvas 세로 길이
        # self.TITLE_SIZE=CANVAS_SIZE_WIDTH//3    #title 사이즈

        # root
        self.root = tkinter.Tk()
        self.root.title("NOTE")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)  # 창 길이 조절 불가능

        # background image
        wall = PhotoImage(file="../image/note_bg.gif")
        wall_label = Label(image=wall)
        wall_label.place(x=-2, y=-2)

        # label(노트 묵록)
        label = tkinter.Label(self.root, text="노트 목록",foreground="#ffffff", background="#503A2E", font=("None", "35"))
        label.place(x=445, y=50)

        # button(new)
        btn_new = tkinter.Button(self.root, text="NEW",foreground="#F4DBCD", background="#81634E", relief="sunken")
        btn_new.pack()

        self.root.mainloop()

if __name__ == '__main__':
    noteListGUI = noteListGUI()
