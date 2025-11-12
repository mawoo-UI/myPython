# tkinter example4 - 버튼 컨트롤
from tkinter import *
from tkinter import messagebox


# 함수 정의(선서)
def myFunc1():
  messagebox.showinfo("버튼1 클릭", "버튼1을 눌렀습니다.")

def myFunc2():
  messagebox.showinfo("버튼2 클릭", "버튼2을 눌렀습니다.")



#메인 
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

button1 = Button(root, text="클릭", fg="red", command=myFunc1)
button2 = Button(root, text="클릭",bg="blue" ,fg="white", command=myFunc2)

button1.pack()
button2.pack()

#한번에 처리하려면
# Button(root, text="클릭", fg="red", command=myFunc1).pack()

#메인 루프
root.mainloop()

