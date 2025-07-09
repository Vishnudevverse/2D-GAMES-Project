import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)

import mysql.connector as s
file=open('store.txt')
pasadusn=((file.read()).strip()).split()
file.close()
bsq=s.connect(host='localhost',user='root',passwd=pasadusn[0],database='gaming')
cur=bsq.cursor()

from tkinter import *
import random as r
addbt=[]
v1=0
point=0
Dval=[]
score='None'
def bt(c,d,X,Y):
    global Dval
    global point
    global addbt
    global v1
    addbt+=c,
    v1+=1
    Dval+=d,
    c.config(image=d)
    if v1==2 and Dval[0]==Dval[1] and addbt[0]!=addbt[1]:
        point+=1
        addbt[0].destroy()
        addbt[1].destroy()
        v1=0
        addbt=[]
        Dval=[]
        if point==8:
            global score
            score=100
            close(1)
    elif v1==3:
        addbt[0].config(image=i0)
        addbt[1].config(image=i0) 
        v1=1
        addbt=[]
        addbt=c,
        Dval=[]
        Dval+=d,
        
a = Tk()
a.geometry("430x415")
a.title('MEMORY')
a.config(bg='grey')
bg=PhotoImage(file='bg.png')
a3 = Canvas( a, width = 425,height = 415)
a3.pack(fill = "both", expand = True)  
a3.create_image( 0, 0, image = bg,anchor = "nw")
i0=PhotoImage(file='no0.png')
i1=PhotoImage(file='no1.png')
i2=PhotoImage(file='no2.png')
i3=PhotoImage(file='no3.png')
i4=PhotoImage(file='no4.png')
i5=PhotoImage(file='no5.png')
i6=PhotoImage(file='no6.png')
i7=PhotoImage(file='no7.png')
i8=PhotoImage(file='no8.png')
l=[i1,i2,i3,i4,i1,i2,i3,i4,i5,i6,i7,i8,i5,i6,i7,i8]
r.shuffle(l)

b1=Button(a,image=i0,command=lambda:bt(b1,l[0],10,10),bd=0,bg='black')
b1.place(x=10,y=10)
b2=Button(a,image=i0,command=lambda:bt(b2,l[1],120,10),bd=0,bg='black')
b2.place(x=120,y=10)
b3=Button(a,image=i0,command=lambda:bt(b3,l[2],230,10),bd=0,bg='black')
b3.place(x=230,y=10)
b4=Button(a,image=i0,command=lambda:bt(b4,l[3],340,10),bd=0,bg='black')
b4.place(x=340,y=10)

b5=Button(a,image=i0,command=lambda:bt(b5,l[4],10,110),bd=0,bg='black')
b5.place(x=10,y=110)
b6=Button(a,image=i0,command=lambda:bt(b6,l[5],120,110),bd=0,bg='black')
b6.place(x=120,y=110)
b7=Button(a,image=i0,command=lambda:bt(b7,l[6],230,110),bd=0,bg='black')
b7.place(x=230,y=110)
b8=Button(a,image=i0,command=lambda:bt(b8,l[7],340,110),bd=0,bg='black')
b8.place(x=340,y=110)

b9=Button(a,image=i0,command=lambda:bt(b9,l[8],10,210),bd=0,bg='black')
b9.place(x=10,y=210)
b10=Button(a,image=i0,command=lambda:bt(b10,l[9],120,210),bd=0,bg='black')
b10.place(x=120,y=210)
b11=Button(a,image=i0,command=lambda:bt(b11,l[10],230,210),bd=0,bg='black')
b11.place(x=230,y=210)
b12=Button(a,image=i0,command=lambda:bt(b12,l[11],340,210),bd=0,bg='black')
b12.place(x=340,y=210)

b13=Button(a,image=i0,command=lambda:bt(b13,l[12],10,310),bd=0,bg='black')
b13.place(x=10,y=310)
b14=Button(a,image=i0,command=lambda:bt(b14,l[13],120,310),bd=0,bg='black')
b14.place(x=120,y=310)
b15=Button(a,image=i0,command=lambda:bt(b15,l[14],230,310),bd=0,bg='black')
b15.place(x=230,y=310)
b16=Button(a,image=i0,command=lambda:bt(b16,l[15],340,310),bd=0,bg='black')
b16.place(x=340,y=310)

def close(z):
    cur.execute('update gaming_details_{} set score="{}" where gamename="{}"'.format(pasadusn[1],score,pasadusn[2]))
    bsq.commit()
    if z:
        bsq.close()
        a.destroy()
        
a.protocol('WM_DELETE_WINDOW',lambda:close(1))

a.resizable(False,False)
a.mainloop()
