import tkinter
import tkinter.font as tkFont
import time
from article.articleCrawling import articleCrawling
import webbrowser

class articleGUI:
    def __init__(self):
        CANVAS_SIZE_WIDTH=1100  #canvas 가로 길이
        CANVAS_SIZE_HEIGHT=750  #canvas 세로 길이

        # root
        self.root=tkinter.Tk()
        self.root.title("ARTICLE")
        self.root.geometry(str(CANVAS_SIZE_WIDTH)+'x'+str(CANVAS_SIZE_HEIGHT)+"+300+100")
        self.root.resizable(False,False)   #창 길이 조절 불가능
        # basic canvas
        self.canvas = tkinter.Canvas(self.root, bg='#F3F3F3', width=CANVAS_SIZE_WIDTH, height=CANVAS_SIZE_HEIGHT)
        self.canvas.pack()

        #article
        self.articleURL=''
        self.articleContent=''
        self.articleIndex=1

        # 왼쪽 캔버스 및 그 안의 요소
        self.left_bundle()
        # 오른쪽 위 캔버스 및 그 안의 요소
        self.right_top_bundle()
        # #오른쪽 아래 캔버스 및 그 안의 요소
        self.right_bottom_bundle()

        self.root.mainloop()

    def left_bundle(self):  #왼쪽 캔버스 묶음
        # canvas
        self.left_canvas = tkinter.Canvas(self.canvas, width=890, height=750,highlightthickness=0)  # highlightthickness는 canvas 회색 테두리 없앰
        self.left_canvas.place(x=0, y=0)
        # 크롤링 결과
        self.articleCrawlingArray=articleCrawling()
        self.articleURL=self.articleCrawlingArray[0]
        self.articleContent=self.articleCrawlingArray[1]
        # URL Label
        self.left_url_top = tkinter.Label(self.left_canvas,width=108,height=2,bg='#503A2E', fg='#FBDDC5', text="웹 페이지에서 직접 기사를 보고 싶다면? 아래 링크를 클릭!", font=("None", 10))
        self.left_url_top.place(x=10,y=5)
        self.left_url_label = tkinter.Label(self.left_canvas,width=108,height=2,bg='#786255', fg='#FBDDC5', text=self.articleURL, font=("Arial", 10))
        self.left_url_label.bind("<Button-1>",self.callback)
        self.left_url_label.place(x=10, y=37)
        # Content Label
        self.left_content_label= tkinter.Label(self.left_canvas,width=108,height=40,bg='#FFFFFF', fg='#000000', text=self.articleContent, font=("Arial", 10))
        self.left_content_label.place(x=10,y=85)


    def right_top_bundle(self): # 오른쪽 위 캔버스 묶음
        # canvas
        self.right_top_canvas = tkinter.Canvas(self.canvas, width=210, height=280, highlightthickness=0)  # highlightthickness는 canvas 회색 테두리 없앰
        self.right_top_canvas.place(x=890, y=0)
        # canvas배경
        self.right_top_canvas_bg = tkinter.PhotoImage(file="../image/article_right_top_bg.PNG")
        self.right_top_canvas.create_image(0, 0, image=self.right_top_canvas_bg, anchor='nw')
        # Label
        self.right_top_time_label=tkinter.Label(self.right_top_canvas,bg='#786255',fg='#FBDDC5',text='00:00',font=("None", 25, 'bold'))
        self.right_top_time_label.place(x=62,y=110)
        # button
        self.timer_start = tkinter.PhotoImage(file="../image/article_right_top_timer_start.png")
        self.right_top_time_btn = tkinter.Button(self.right_top_canvas, image=self.timer_start, command=self.timer_toggle,width=45, height=45, highlightthickness=0, borderwidth=0, padx=0, pady=0)
        self.right_top_time_btn.place(x=82.5,y=170)
        #timer toggle true
        self.paused=True    #start안한상태


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

    def timer_toggle(self):
        if self.paused:
            self.paused=False
            self.timer_stop = tkinter.PhotoImage(file="../image/article_right_top_timer_stop.png")
            self.right_top_time_btn.config(image=self.timer_stop)
            self.oldtime=time.time()
            self.timer_run()
        else:
            self.paused=True
            self.oldtime=time.time()
            self.right_top_time_btn.config(image=self.timer_start)

    def timer_run(self):
        # stop 버튼 눌렀을 때
        if self.paused:
            # 타이머 file에 추가 저장
            f=open("../article/timef.txt",'a')
            f.write(self.timestr+"\n")
            f.close()
            print("시간이 정상적으로 저장되었습니다. ["+self.timestr+"]")
            return
        # start 버튼 눌렀을 때 or 타이머 시간 갱신
        self.delta = int(time.time() - self.oldtime)
        self.timestr = '{:02}:{:02}'.format(*divmod(self.delta, 60))
        self.right_top_time_label.config(text=self.timestr)
        self.right_top_time_label.after(1000,self.timer_run)

    def callback(self,event):
        webbrowser.open_new(self.articleURL)

if __name__=='__main__':
    articleGUI=articleGUI()