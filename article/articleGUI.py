import tkinter

class articleGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH=1100  #canvas 가로 길이
        CANVAS_SIZE_HEIGHT=750  #canvas 세로 길이
        # self.TITLE_SIZE=CANVAS_SIZE_WIDTH//3    #title 사이즈

        # root
        self.root=tkinter.Tk()
        self.root.title("ARTICLE")
        self.root.geometry(str(CANVAS_SIZE_WIDTH)+'x'+str(CANVAS_SIZE_HEIGHT)+"+300+100")
        self.root.resizable(False,False)   #창 길이 조절 불가능

        # basic canvas
        self.canvas=tkinter.Canvas(self.root,bg='#F3F3F3',width=CANVAS_SIZE_WIDTH,height=CANVAS_SIZE_HEIGHT)
        self.canvas.pack()

        # 오른쪽 위 캔버스 및 그 안의 요소
        self.right_top_canvas()
        # #오른쪽 아래 캔버스 및 그 안의 요소
        self.right_bottom_canvas()

        self.root.mainloop()



    def right_top_canvas(self): # 오른쪽 위 캔버스
        self.left_top_canvas = tkinter.Canvas(self.canvas, width=210, height=280, highlightthickness=0) #highlightthickness는 canvas 회색 테두리 없앰
        self.left_top_canvas.place(x=890, y=0)
        self.bg = tkinter.PhotoImage(file="../image/article_right_top_bg.gif")
        self.left_top_canvas.create_image(0, 0, image=self.bg,anchor='nw')


    def right_bottom_canvas(self):  #오른쪽 아래 캔버스
        self.right_bottom_canvas = tkinter.Canvas(self.canvas, bg='#CCB9A8', width=210, height=470,highlightthickness=0)
        self.right_bottom_canvas.place(x=890, y=280)

if __name__=='__main__':
    articleGUI=articleGUI()