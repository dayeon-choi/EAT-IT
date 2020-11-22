import tkinter
import tkinter.font as tkFont
import time

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
        self.right_top_bundle()
        # #오른쪽 아래 캔버스 및 그 안의 요소
        self.right_bottom_bundle()

        self.root.mainloop()


    def right_top_bundle(self): # 오른쪽 위 캔버스 묶음
        self.right_top_canvas()
        self.update_clock()

    def right_top_canvas(self): #오른쪽 위 캔버스
        # canvas
        self.right_top_canvas = tkinter.Canvas(self.canvas, width=210, height=280,highlightthickness=0)  # highlightthickness는 canvas 회색 테두리 없앰
        self.right_top_canvas.place(x=890, y=0)
        # canvas배경
        self.right_top_canvas_bg = tkinter.PhotoImage(file="../image/article_right_top_bg.gif")
        self.right_top_canvas.create_image(0, 0, image=self.right_top_canvas_bg, anchor='nw')


    def right_bottom_bundle(self):  #오른쪽 아래 캔버스 묶음
        #캔버스
        self.right_bottom_canvas=tkinter.Canvas(self.canvas, bg='#CCB9A8', width=210, height=470,highlightthickness=0)
        self.right_bottom_canvas.place(x=890, y=280)

        #note버튼
        self.note_bg=tkinter.PhotoImage(file="../image/article_right_bottom_note.gif")
        self.right_bottom_note=tkinter.Button(self.right_bottom_canvas,image=self.note_bg,width=100,height=45,highlightthickness=0,borderwidth=0,padx=0,pady=0)
        self.right_bottom_note.place(x=55,y=80)
        
        #다 봤어요!
        self.saw_font=tkinter.PhotoImage(file="../image/article_right_bottom_saw.gif")
        #self.saw_label=tkinter.Label(self.right_bottom_canvas,text="다 봤어요!",font=(None,25),fg='#000000',bg='#CCB9A8')
        self.saw_label = tkinter.Label(self.right_bottom_canvas,image=self.saw_font,width=135,height=35,highlightthickness=0,borderwidth=0,padx=0,pady=0)
        self.saw_label.place(x=37,y=180)

        #complete버튼
        self.complete_bg=tkinter.PhotoImage(file="../image/article_right_bottom_complete.gif")
        self.right_bottom_complete=tkinter.Button(self.right_bottom_canvas,image=self.complete_bg,width=180,height=45,highlightthickness=0,borderwidth=0,padx=0,pady=0)
        self.right_bottom_complete.place(x=15,y=230)
        
        #prev버튼(화살표-이전버튼)
        self.prev_bg=tkinter.PhotoImage(file="../image/article_right_bottom_prev.gif")
        self.right_bottom_prev=tkinter.Button(self.right_bottom_canvas, image=self.prev_bg, width=44,height=45, highlightthickness=0, borderwidth=0, padx=0, pady=0)
        self.right_bottom_prev.place(x=15, y=370)

        # next버튼(화살표-이후버튼)
        self.next_bg=tkinter.PhotoImage(file="../image/article_right_bottom_next.gif")
        self.right_bottom_next=tkinter.Button(self.right_bottom_canvas, image=self.next_bg, width=44, height=45,highlightthickness=0, borderwidth=0, padx=0, pady=0)
        self.right_bottom_next.place(x=151, y=370)

    def update_clock(self):
        #text가 겹치는 것을 방지를 위해 canvas 지우기
        self.right_top_canvas.delete('all')

        # canvas 다시 세팅
        self.right_top_canvas = tkinter.Canvas(self.canvas, width=210, height=280,highlightthickness=0)  # highlightthickness는 canvas 회색 테두리 없앰
        self.right_top_canvas.place(x=890, y=0)
        self.right_top_canvas_bg = tkinter.PhotoImage(file="../image/article_right_top_bg.gif")
        self.right_top_canvas.create_image(0, 0, image=self.right_top_canvas_bg, anchor='nw')

        #time
        self.now=time.strftime("%H:%M:%S")
        self.right_top_canvas.create_text(100, 100, text=self.now, font=("None", 25, 'bold'), fill="#FBDDC5")
        self.root.after(1000,self.update_clock)


if __name__=='__main__':
    articleGUI=articleGUI()