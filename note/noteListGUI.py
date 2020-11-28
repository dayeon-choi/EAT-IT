import tkinter
from tkinter import *
from tkinter import ttk
from DB.noteDB import noteDB

# Click event
def btnClick():
    pass

class noteListGUI:
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

        # label(노트 목록)
        label = tkinter.Label(self.root, text="노트 목록",foreground="#ffffff", background="#503A2E", font=("None", "35"))
        label.pack(pady=50)

        # button(new)
        btn_new = tkinter.Button(self.root, text="NEW",foreground="#F4DBCD", background="#81634E", relief="raised", font=("None", "20"), command=btnClick)
        btn_new.place(x=950, y=120)

        # Add treeview Style
        style = ttk.Style()
        style.configure("Treeview",
                        background="#F3E9DF",
                        foreground="black",
                        rowheight=35,
                        fieldbackground="silver",
                        font=("None", "10")
                        )
        # selected color
        style.map('Treeview',
                  background=[('selected', '#AD8F89')])


        # treeview(노트 표)
        note_tree = ttk.Treeview(self.root)

        # Columns
        note_tree['columns'] = ("title", "content", "date")

        # Formate Columns
        note_tree.column("#0", width=0, stretch=NO)
        note_tree.column("title", anchor=W, width=200)
        note_tree.column("content", anchor=W, width=200)
        note_tree.column("date", anchor=W, width=200)

        # Create Headings
        note_tree.heading("#0", text="", anchor=W)
        note_tree.heading("title", text="제목(title)", anchor=W)
        note_tree.heading("content", text="내용(content)", anchor=W)
        note_tree.heading("date", text="날짜(date)", anchor=W)

        # Add data
        data = noteDB.find(self)
        cnt = 0
        for record in data:
            note_tree.insert(parent='', index='end', iid=cnt, text="", value=(record[0], record[1], record[2]))
            cnt += 1

        note_tree.pack(pady=70)

        self.root.mainloop()

if __name__ == '__main__':
    noteListGUI = noteListGUI()
