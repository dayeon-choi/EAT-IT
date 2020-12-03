import tkinter
from tkinter import *
from article.articlefProcessing import ArticleProcessing
from article.timefProcessing import TimeProcessing

class MainGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH = 1100  # canvas 가로 길이
        CANVAS_SIZE_HEIGHT = 750  # canvas 세로 길이

        # root
        self.root = tkinter.Tk()
        self.root.title("EAT-IT")
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

        # label(개수)
        ArticlePro = ArticleProcessing()
        article_total = ArticlePro.show_total_article()
        label_article_total = tkinter.Label(self.root, text=article_total, width=11, background="#F3F3F3", font=('Arial', "60", "bold"))
        label_article_total.place(x=10,y=570)
        # label(내가 본 기사 개수)
        label_article = tkinter.Label(self.root, text="내가 본 기사 개수", width=50, background="#F3F3F3", font=('Arial', "13"))
        label_article.place(x=50, y=550)

        # label(개수)
        TimePro = TimeProcessing()
        time_total = TimePro.show_total_time()
        label_time_total = tkinter.Label(self.root, text=time_total, width=11, background="#F3F3F3", font=('Arial', "40", "bold"))
        label_time_total.place(x=650, y=583)
        # label(내가 본 기사 개수)
        label_time = tkinter.Label(self.root, text="내가 투자한 시간", width=30, background="#F3F3F3",font=('Arial', "13"))
        label_time.place(x=680, y=550)

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
