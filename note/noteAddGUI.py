import tkinter
from tkinter import *
from tkinter import ttk
from DB.noteDB import noteDB

class noteAddGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 1100  # canvas 가로 길이
        CANVAS_SIZE_HEIGHT = 750  # canvas 세로 길이

        # root
        self.root = tkinter.Tk()
        self.root.title("NOTE")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)  # 창 길이 조절 불가능

        # background image
        wall = PhotoImage(file="../image/note_bg.PNG")
        wall_label = Label(image=wall)
        wall_label.place(x=-2, y=-2)

        # label(노트 추가)
        label = tkinter.Label(self.root, text="노트 추가",foreground="#ffffff", background="#503A2E", font=("None", "35"))
        label.pack(pady=50)

        # button(save)
        btn_new = tkinter.Button(self.root, text="SAVE",foreground="#000000", background="#CCB9A8", relief="raised", font=("None", "20"))
        btn_new.place(x=950, y=120)

        # entry(title)
        entry_title = ttk.Entry(self.root)
        entry_title.pack(pady=100)

        # entry(content)

        self.root.mainloop()

if __name__ == '__main__':
    noteAddGUI = noteAddGUI()
