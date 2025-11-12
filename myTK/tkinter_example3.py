# tkinter example2 - 창 조절 연습
from tkinter import *


#TK 객체(스크린) 생성 - root
root = Tk()

#스크린 설정
root.title('라벨 붙이기') #타이틀
root.geometry('500x200') #창 크기
root.resizable(width=True, height=True) # 리사이즈 허용 여부

#라벨 붙이기
label1 = Label(root, text="Hello")
label2 = Label(root, text="World", font=("굴림", 30), fg="red")
label3 = Label(root, text="Bye", bg="pink", width=20, height=5, anchor= CENTER)

label1.pack()
label2.pack()
label3.pack()

Label(root, text="Hello").pack()

#메인 루프
root.mainloop()

