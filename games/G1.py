import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)

import mysql.connector as s
file=open('store.txt')
pasadusn=((file.read()).strip()).split()
file.close()
bsq=s.connect(host='localhost',user='root',passwd=pasadusn[0],database='gaming')
cur=bsq.cursor()

from tkinter import *
winner='None'
def reset(s):
    global b
    global v
    global lp1
    global lp2
    lp1=[[0,0,0],
        [0,0,0],
        [0,0,0]]
    lp2=[[0,0,0],
        [0,0,0],
        [0,0,0]]
    b='X'
    v=0
    if s:
        LABLE.config(text='       X TURN     ')
        for i in listbutton:
            i['state']='normal'
            i.config(image=i0)
reset(0)
def bt(button,c,d):
    global winner
    global LABLE
    global listbutton    
    global lp1
    global lp2
    global v
    global b
    
    '''
    l0=[[b,b,b],
        [0,0,0],
        [0,0,0]]
    l1=[[0,0,0],
        [b,b,b],
        [0,0,0]]
    l2=[[0,0,0],
        [0,0,0],
        [b,b,b]]
    l3=[[b,0,0],
        [b,0,0],
        [b,0,0]]
    l4=[[0,b,0],
        [0,b,0],
        [0,b,0]]
    l5=[[0,0,b],
        [0,0,b],
        [0,0,b]]
    l6=[[0,0,b],
        [0,b,0],
        [b,0,0]]
    l7=[[b,0,0],
        [0,b,0],
        [0,0,b]]'''
    
        
    if v==0:
        lp1[c][d]=b
        button.config(image=iX)
        button['state']=DISABLED
        v=1
        
        if ((b==lp1[0][0] and b==lp1[0][1] and b==lp1[0][2]) or
            (b==lp1[1][0] and b==lp1[1][1] and b==lp1[1][2]) or
            (b==lp1[2][0] and b==lp1[2][1] and b==lp1[2][2]) or
            (b==lp1[0][0] and b==lp1[1][0] and b==lp1[2][0]) or
            (b==lp1[0][1] and b==lp1[1][1] and b==lp1[2][1]) or
            (b==lp1[0][2] and b==lp1[1][2] and b==lp1[2][2]) or
            (b==lp1[0][2] and b==lp1[1][1] and b==lp1[2][0]) or
            (b==lp1[0][0] and b==lp1[1][1] and b==lp1[2][2])):
            LABLE.config(text='X PLAYER WON!')
            winner='X PLAYER WON!'
            close(0)
            for i in listbutton:
                i['state']=DISABLED
        else:
            b='O'
            LABLE.config(text='       O TURN     ')
    else:
        lp2[c][d]=b
        button.config(image=iO)
        button['state']=DISABLED
        v=0
        if ((b==lp2[0][0] and b==lp2[0][1] and b==lp2[0][2]) or
            (b==lp2[1][0] and b==lp2[1][1] and b==lp2[1][2]) or
            (b==lp2[2][0] and b==lp2[2][1] and b==lp2[2][2]) or
            (b==lp2[0][0] and b==lp2[1][0] and b==lp2[2][0]) or
            (b==lp2[0][1] and b==lp2[1][1] and b==lp2[2][1]) or
            (b==lp2[0][2] and b==lp2[1][2] and b==lp2[2][2]) or
            (b==lp2[0][2] and b==lp2[1][1] and b==lp2[2][0]) or
            (b==lp2[0][0] and b==lp2[1][1] and b==lp2[2][2])):
            LABLE.config(text='O PLAYER WON!')
            winner='O PLAYER WON!'
            close(0)
            for i in listbutton:
                i['state']=DISABLED
        else:
            b='X'
            LABLE.config(text='       X TURN     ')

a = Tk()
a.geometry("260x360")
a.title('XO')
a.config(bg='#00E5FF')
Label(a,width=100,height=10,bg='black').place(x=0,y=270)
Label(a,width=100,height=1,bg='black').place(x=0,y=0)

i0=PhotoImage(file='no0.png')
iX=PhotoImage(file='X.png')
iO=PhotoImage(file='O.png')

b1=Button(a,image=i0,command=lambda:bt(b1,0,0),bd=0,bg='black')
b1.place(x=0,y=10)
b2=Button(a,image=i0,command=lambda:bt(b2,0,1),bd=0,bg='black')
b2.place(x=90,y=10)
b3=Button(a,image=i0,command=lambda:bt(b3,0,2),bd=0,bg='black')
b3.place(x=180,y=10)

b5=Button(a,image=i0,command=lambda:bt(b5,1,0),bd=0,bg='black')
b5.place(x=0,y=100)
b6=Button(a,image=i0,command=lambda:bt(b6,1,1),bd=0,bg='black')
b6.place(x=90,y=100)
b7=Button(a,image=i0,command=lambda:bt(b7,1,2),bd=0,bg='black')
b7.place(x=180,y=100)

b9=Button(a,image=i0,command=lambda:bt(b9,2,0),bd=0,bg='black')
b9.place(x=0,y=190)
b10=Button(a,image=i0,command=lambda:bt(b10,2,1),bd=0,bg='black')
b10.place(x=90,y=190)
b11=Button(a,image=i0,command=lambda:bt(b11,2,2),bd=0,bg='black')
b11.place(x=180,y=190)
listbutton=[b1,b2,b3,b5,b6,b7,b9,b10,b11]
b12=Button(a,text='RESET',command=lambda:reset(1),font=('Arial 15') ,fg='black',bg='#00E5FF')
b12.place(x=90,y=305)

LABLE=Label(a,text='       X TURN    ', font=('Elephant 10'),bg='black',fg='#00E5FF')
LABLE.place(x=75,y=280)

def close(z):
    cur.execute('update gaming_details_{} set score="{}" where gamename="{}"'.format(pasadusn[1],winner,pasadusn[2]))
    bsq.commit()
    if z:
        a.destroy()
        bsq.close()
a.protocol('WM_DELETE_WINDOW',lambda:close(1))

a.resizable(False,False)
a.mainloop()
