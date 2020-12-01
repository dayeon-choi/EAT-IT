import tkinter
from tkinter import *
from note import Note
from noteEditGUI import noteEditGUI

class noteDetailGUI:
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

        # entry(글 제목)
        entry_title = tkinter.Entry(self.root, width=20, background="#FAF7F4", font=("None", "20"), borderwidth=9,
                                    relief="flat", justify="center")
        entry_title.insert(0, "글 제목")
        entry_title.pack(pady=50)

        # button(delete)
        btn_delete = tkinter.Button(self.root, text="DELETE", width=8, foreground="#000000", background="#B99D7A",
                                 relief="raised", font=("None", "20"))
        btn_delete.place(x=750, y=120)

        # button(modify)
        btn_modify = tkinter.Button(self.root, text="MODIFY", width=8, foreground="#000000", background="#EDBC83",
                                 relief="raised", font=("None", "20"), command=lambda: self.btnModify())
        btn_modify.place(x=910, y=120)

        # text(content)
        text_con = tkinter.Text(self.root, width=52, height=13, background="#FAF7F4", wrap='word', font=("None", "20"),
                                spacing1=7)
        text_con.insert(tkinter.CURRENT, "글 내용")
        text_con.place(x=132, y=210)

        scroll_y = tkinter.Scrollbar(self.root, orient="vertical", command=text_con.yview)
        scroll_y.place(x=950, y=605)

        text_con.configure(yscrollcommand=scroll_y.set)

        self.root.mainloop()

    # Click event
    def btnModify(self):
        self.root.destroy()
        noteEditGUI()

    def btnDelete(self, title):
        Note.delete_note(None, title)

if __name__ == '__main__':
    noteDetailGUI = noteDetailGUI()
