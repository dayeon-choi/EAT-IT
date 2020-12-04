import tkinter
from tkinter import *
from tkinter import messagebox
from note.note import Note
from GUI.noteEditGUI import noteEditGUI


class noteDetailGUI:
    def __init__(self, title, content):
        CANVAS_SIZE_WIDTH = 1100  # canvas 가로 길이
        CANVAS_SIZE_HEIGHT = 750  # canvas 세로 길이

        # root
        self.root = tkinter.Tk()
        self.root.title("상세보기")
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

        # button(delete)
        btn_delete = tkinter.Button(self.root, text="DELETE", width=8, foreground="#000000", background="#B99D7A",
                                 relief="raised", font=("Arial", "20"), command=lambda: self.btnDelete(title))
        btn_delete.place(x=750, y=120)

        # button(modify)
        btn_modify = tkinter.Button(self.root, text="MODIFY", width=8, foreground="#000000", background="#EDBC83",
                                 relief="raised", font=("Arial", "20"), command=lambda: self.btnModify(entry_title.get(), text_con.get("1.0", END)))
        btn_modify.place(x=910, y=120)

        # entry(글 제목)
        entry_title = tkinter.Entry(self.root, width=20, background="#FAF7F4", font=("Nirmala UI", "20"), borderwidth=9, disabledforeground="black",
                                    relief="flat", justify="center")
        entry_title.insert(0, title)
        entry_title.configure(state='disabled')
        entry_title.pack(pady=50)

        # text(content)
        text_frame = Frame(self.root)
        text_frame.place(x=132, y=210)

        text_con = tkinter.Text(self.root, width=60, height=11, background="#FAF7F4", wrap='word', font=("Nirmala UI", "20"),
                                spacing1=7)
        text_con.insert(tkinter.CURRENT, content)
        text_con.configure(state='disabled')
        text_con.place(x=99, y=210)

        self.root.mainloop()

    # Click event
    def btnModify(self, title, content):
        self.root.destroy()
        noteEditGUI(title, content)

    def btnDelete(self, title):
        from GUI.noteListGUI import noteListGUI
        Note.delete_note(None, title)
        tkinter.messagebox.showinfo("삭제 확인", "삭제되었습니다")
        self.root.destroy()
        noteListGUI()

    def btnBack(self):
        from GUI.noteListGUI import noteListGUI
        self.root.destroy()
        noteListGUI()

if __name__ == '__main__':
    noteDetailGUI = noteDetailGUI()
