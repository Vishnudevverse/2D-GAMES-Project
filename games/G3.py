import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)
from tkinter import *
import random as r

import mysql.connector as s
file=open('store.txt')
pasadusn=((file.read()).strip()).split()
file.close()
bsq=s.connect(host='localhost',user='root',passwd=pasadusn[0],database='gaming')
cur=bsq.cursor()

a = Tk()
a.geometry("400x340")
a.title('STONE PAPER SCISSOR')
a.config(bg='black')
def run(u,pic):
    global l1
    global l2
    global user
    global computer
    x=['r','p','s']
    r.shuffle(x)
    pc=r.choice(x)
    dict={'r':i1,'p':i2,'s':i3}
    pclab=Label(a,image=dict[pc],bg='black').place(x=40,y=60)
    uslab=Label(a,image=pic,bg='black').place(x=260,y=60)
    rt=' '
    l3=Label(a,text=rt, font=('Arial 15'),bg='black',fg='#00E5FF')
    l3.place(x=45,y=180)    
    if u==pc:
        rt='\t  DRAW\t   '
        img=smile
        
    elif u=='r' and pc=='s':
        rt='\tYOU WON!\t'
        img=smile
        user+=1
    elif u=='r' and pc=='p':
        rt='\tYOU LOSS!\t'
        img=sad
        computer+=1
        
    elif u=='s' and pc=='r':
        rt='\tYOU lOSS!\t'
        img=sad
        computer+=1
    elif u=='p' and pc=='r':
        rt='\tYOU WON!\t'
        img=smile
        user+=1
        
    elif u=='p' and pc=='s':
        rt='\tYOU LOSS!\t'
        img=sad
        computer+=1
    elif u=='s' and pc=='p':
        rt='\tYOU WON!\t'
        img=smile
        user+=1
    l1.config(text='PC:'+str(computer))
    l2.config(text='USER:'+str(user))
    l3.config(text=rt)
    Label(a,image=img,bg='black').place(x=165,y=60)
    Label(a,text=rt,font=('Arial 15'),bg='black',fg='#00E5FF').place(x=70,y=180)

user=0
computer=0  
l1=Label(a,text='PC:0', font=('Arial 15'),bg='black',fg='#00E5FF')
l1.place(x=65,y=25)
l2=Label(a,text='USER:0', font=('Arial 15'),bg='black',fg='#00E5FF')
l2.place(x=270,y=25)
sad=PhotoImage(file='sad.png')
smile=PhotoImage(file='smile.png')
i1=PhotoImage(file='stone.png')
i2=PhotoImage(file='paper.png')
i3=PhotoImage(file='scissor.png')
b1=Button(a,image=i1,command=lambda:run('r',i1),bd=0,bg='black')
b1.place(x=10,y=220)
b2=Button(a,image=i2,command=lambda:run('p',i2),bd=0,bg='black')
b2.place(x=150,y=220)
b3=Button(a,image=i3,command=lambda:run('s',i3),bd=0,bg='black')
b3.place(x=290,y=220)

def close(z):
    cur.execute('update gaming_details_{} set score="{}" where gamename="{}"'.format(pasadusn[1],'pc:'+str(computer)+' '+'user:'+str(user),pasadusn[2]))
    bsq.commit()
    if z:
        a.destroy()
        bsq.close()
        
a.protocol('WM_DELETE_WINDOW',lambda:close(1))
a.resizable(False,False)
a.mainloop()
