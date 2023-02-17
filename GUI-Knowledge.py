import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



import random
messages = ['กระเพาหมู่ตุ๋ม','ก๋วยเตี๋ยวเรือ','ข้าวเหนียวหมูปิ้ง','สปาเก็ตตี้','ข้าวมันไก่']
messages2 = ['เซนทรัลลาดพร้าว','บางขุนเทียน','ถนนข้าวสาร','พัทยาใต้','เกาะเต่า']
messages3 = ['The last fo us(ซีรี่)','ทิตน้อย','Ant man','Fuck the whole world','Avatar 2']
mess = random.choice(messages)
mess2 = random.choice(messages2)
mess3 = random.choice(messages3)


GUI = Tk()
GUI.title('โปรแกรมช่วยตัดสินใจสำหรับคุณผ.ญ.ที่คิดไม่ออกว่าต้องการอะไร')
GUI.geometry('500x400')

L1 = Label(GUI,text='ให้เราช่วยคุณ',font=('Sukhumvit',40),fg='blue')
L1.pack()
L2 = Label(GUI,text='จิ้มสิ่งที่ต้องการตอนนี้ด้านล่าง',font=('Sukhumvit',20),fg='green')
L2.pack()

def Button1():
    #text = 'กระเพราหมู้ตุ๋น!!'
    random.choice(mess)
    messagebox.askyesno('กินอะไร',mess)


FB1 = Frame(GUI)
FB1.place(x=50,y=120)
B1 = ttk.Button(FB1,text='กินอะไร',command=Button1)
B1.pack(ipadx=20,ipady=30)

def Button2():
    #text = 'เซนทรัลลาดพร้าว'
    random.choice(mess2)
    messagebox.askyesno('สถานที่เที่ยว',mess2)

FB1 = Frame(GUI)
FB1.place(x=185,y=120)
B2 = ttk.Button(FB1,text='สถานที่เที่ยว',command=Button2)
B2.pack(ipadx=20,ipady=30)
#B2.place(x=20,y=200)#กำหนดที่ตั้งของปุ่ม

def Button3():
    #text = 'ถ่ายรูปเล่นที่สวนรถไฟ'
    random.choice(mess3)
    messagebox.askyesno('หนังเรื่อง',mess3)
FB1 = Frame(GUI)
FB1.place(x=330,y=120)
B3 = ttk.Button(FB1,text='หนังเรื่อง',command=Button3)
B3.pack(ipadx=20,ipady=30)




GUI.mainloop()
