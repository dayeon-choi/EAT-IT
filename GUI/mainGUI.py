import tkinter
from tkinter import *

class MainGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 1100  # canvas 가로 길이
        CANVAS_SIZE_HEIGHT = 750  # canvas 세로 길이

        # root
        self.root = tkinter.Tk()
        self.root.title("Main")
        self.root.geometry(str(CANVAS_SIZE_WIDTH) + 'x' + str(CANVAS_SIZE_HEIGHT))
        self.root.resizable(False, False)  # 창 길이 조절 불가능

        # background image
        wall = PhotoImage(file="../image/main.PNG")
        wall_label = Label(image=wall)
        wall_label.place(x=-3, y=0)

        # button(HOME)
        btn_home = tkinter.Button(self.root, text="HOME", width=23, height=2, foreground="#000000", background="#786255",
                                    relief="raised", font=('Arial', "20"), borderwidth=0)
        btn_home.place(x=0, y=0)

        # button(ARTICLE)
        btn_article = tkinter.Button(self.root, text="ARTICLE", width=23, height=2, foreground="#000000", background="#CCB9A8",
                                    relief="raised", font=("Arial", "20"), borderwidth=0, command=lambda: self.articleClick() )
        btn_article.pack(side="top")

        # button(NOTE)
        btn_note = tkinter.Button(self.root, text="NOTE", width=23, height=2, foreground="#000000", background="#CCB9A8",
                                    relief="raised", font=("Arial", "20"), borderwidth=0, command=lambda: self.noteClick())
        btn_note.place(x=733, y=0)

        # label(한줄 문구)
        label_ment = tkinter.Label(self.root, text="SWEET IT : 짧은 시간들을 모아 IT 지식을 꿀꺽 삼켜봅시다", background="#E4E3E1", font=('Nirmala UI', "15"))
        label_ment.pack(side='bottom', pady=300)

        self.root.mainloop()

    def articleClick(self):
        from GUI.articleGUI import articleGUI
        self.root.destroy()
        articleGUI()

    def noteClick(self):
        from GUI.noteListGUI import noteListGUI
        self.root.destroy()
        noteListGUI()

if __name__ == '__main__':
    MainGUI = MainGUI()
