import tkinter
from tkinter import *
from note import Note

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

        # PhotoImage(back)
        img_back = tkinter.PhotoImage(file="../image/button_back.PNG")
        btn_back = tkinter.Button(self.root, image=img_back, relief="solid", highlightthickness=0, borderwidth=0,
                                  command=lambda: self.btnBack())
        btn_back.place(x=10, y=10)

        # label(노트 추가)
        label = tkinter.Label(self.root, text="노트 추가",foreground="#ffffff", background="#503A2E", font=("None", "35"))
        label.pack(pady=50)

        # entry(title)
        entry_title = tkinter.Entry(self.root, width=51, background="#FAF7F4", font=("None", "20"), borderwidth=9,
                                    relief="flat")
        entry_title.insert(0, "제목을 입력하세요")
        entry_title.place(x=132, y=210)

        # text(content)
        text_con = tkinter.Text(self.root, width=52, height=11, background="#FAF7F4", wrap='word', font=("None", "20"),
                                spacing1=7)
        text_con.insert(tkinter.CURRENT, "내용을 입력하세요")
        text_con.place(x=132, y=280)

        scroll_y = tkinter.Scrollbar(self.root, orient="vertical", command=text_con.yview)
        scroll_y.place(x=935, y=525)

        # button(save)
        btn_new = tkinter.Button(self.root, text="SAVE", width=8 , foreground="#000000", background="#CCB9A8", relief="raised",
                                 font=("None", "20"), command=lambda: self.btnSave(entry_title.get(), text_con.get("1.0", END)))
        btn_new.place(x=910, y=120)


        text_con.configure(yscrollcommand=scroll_y.set)


        self.root.mainloop()

    # Click event
    def btnSave(self, title, content):
        Note.add_note(None, title, content)

    def btnBack(self):
        from noteListGUI import noteListGUI
        self.root.destroy()
        noteListGUI()

if __name__ == '__main__':
    noteAddGUI = noteAddGUI()
