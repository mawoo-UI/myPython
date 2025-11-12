# tkinter example2 - 창 조절 연습
from tkinter import *


#TK 객체(스크린) 생성 - root
root = Tk()

#스크린 설정
root.title('창 조절 연습') #타이틀
root.geometry('500x200') #창 크기
root.resizable(width=True, height=True) # 리사이즈 허용 여부

#메인 루프
root.mainloop()