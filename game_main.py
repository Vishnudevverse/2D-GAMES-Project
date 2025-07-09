from tkinter import *
import os
import mysql.connector as s
import pickle

DIR=os.getcwd()
os.chdir(DIR+'\\games')

import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)


def opening():
    global l
    global L
    global P
    f=open('pswd.txt','r')
    l=[]
    P=[]
    L=[]
    x=f.readlines()
    if x!=[]:
        for i in x:
            i=i.strip()
            i=i.split()
            P+=i[1],
            l+=i[0],i[1],
            L+=(i[0],i[1]),
    f.close()
opening()

DICT={'G1':('TIC_TAC_TOE',"USE DOUBLE TRICK"),
      'G2':('MEMORY','DONT FORGET'),
      'G3':('STONE_PAPER_SCISSOR','DEPENDS ON LUCK'),
      'G5':('TURTLE_RACE','DEPENDS ON LUCK')}

def sqlchk(d,ab):
    
    if ab==1:
        try:
            global cur
            global bsq
            bsq=s.connect(host='localhost',user='root',passwd=d)
            cur=bsq.cursor()
            cur.execute("create database if not exists gaming")
            cur.execute("use gaming")
            bsq.commit()
            return 1
        except:
            return 0
        
    if ab==2:
        cur.execute("create table if not exists gaming_details_{}(GAMENAME VARCHAR(20),DATES_AND_TIME varchar(20),SCORE varchar(20))".format(d))
        Lg=['MEMORY','STONE_PAPER_SCISSOR','TURTLE_RACE','TIC_TAC_TOE']
        cur.execute('select gamename from gaming_details_{}'.format(d))
        lg=[]
        for i in cur:
            lg+=list(i)
        if Lg!=lg:
            for i in Lg:
                cur.execute('insert into gaming_details_{}(GAMENAME) values ("{}")'.format(d,i))
                bsq.commit()
                
    if ab==3:
        cur.execute('select * from gaming_details_{}'.format(d))
        listgm=cur.fetchall()
        return listgm
def Loginform():
    def Game(x,y):
        global bt
        global gmimg
        lable=Label(pg3,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t',font=('ravie 10'),fg='#FF00B5',bg='black')
        lable.place(x=420,y=620)
        lable2=Label(pg3,text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t",font=('ravie 10'),fg='#FF00B5',bg='black')
        lable2.place(x=420,y=650)
        lable3=Label(pg3,text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t",font=('ravie 10'),fg='#FF00B5',bg='black')
        lable3.place(x=700,y=620)
        lable4=Label(pg3,text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t",font=('ravie 10'),fg='#FF00B5',bg='black')
        lable4.place(x=858,y=650)
        try:
            gmimg.destroy()
            bt.destroy()
        except:
            pass
        def run():
            a.withdraw()
            cur.execute('update gaming_details_{} set DATES_AND_TIME=sysdate() where gamename="{}"'.format(d,DICT[g][0]))
            bsq.commit()
            llg=sqlchk(d,3)
            cur.execute('select DATES_AND_TIME from gaming_details_{} where gamename="{}"'.format(d,DICT[g][0]))
            ll3=cur.fetchone()
            ll3=(ll3[0])
            lable3.config(text='\t\tLAST USED ON: '+str(ll3)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            close(0)
            os.system('python G'+str(x)+'.py')
            sqlchk(p1,1)
            cur.execute('select score from gaming_details_{} where gamename="{}"'.format(d,DICT[g][0]))
            ll3=cur.fetchone()
            ll3=(ll3[0])
            lable4.config(text='SCORE: '+str(ll3)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            a.deiconify()
            
        if x!=0:
            d=username.get()
            llg=sqlchk(d,3)
            gmimg=Label(pg3,image=y,bg='black')
            gmimg.place(x=50,y=490)
            g='G'+str(x)
            p1=passw.get()
            b=username.get()
            file=open('store.txt','w')
            file.write(p1+' '+b+' '+DICT[g][0])
            file.close()
            lable.config(text='GAME:'+DICT[g][0]+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            lable2.config(text='HINT:'+DICT[g][1]+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            cur.execute('select DATES_AND_TIME,score from gaming_details_{} where gamename="{}"'.format(d,DICT[g][0]))
        
            ll3=cur.fetchone()
            if str(ll3[0])==str(None):
                lable3.config(text='\t\tLAST USED ON: '+'None'+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            else:
                ll31=(ll3[0])
                lable3.config(text='\t\tLAST USED ON: '+str(ll31)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")

            if str(ll3[1])==str(None):
                lable4.config(text='SCORE: '+'None'+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            else:
                ll32=(ll3[1])
                lable4.config(text='SCORE: '+str(ll32)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            bt=Button(pg3,image=b1,command=lambda: run(),bd=0,bg='black',fg='black')
            bt.place(x=27,y=625)
        
        
    a = Tk()
    a.title(' '*180+'CLASSIC 2D GAMES\t')
    a.geometry("1280x700")

    pg1=Frame(a)
    pg2=Frame(a)
    pg3=Frame(a)
    pg0=Frame(a)

    for frame in (pg1,pg2,pg3,pg0):
        frame.grid(row=0,column=0,sticky='nsew')

    def shwfrm(frame):
        frame.tkraise()
    shwfrm(pg0)
    pg0.after(2000,lambda:shwfrm(pg1))

    def reset(z):
        E1.delete(0,END)
        E2.delete(0,END)
        E3.delete(0,END)
        E4.delete(0,END)
        E5.delete(0,END)
        pcheck(0)
        pcheck2(0)
        if z==1:
            shwfrm(pg1)
            
    def pcheck2(z):
        if z==1:
            global l2
            b=username1.get()
            p=password1.get()
            af=0
            if b=='' or p=='':
                me='                                    FILL THE EMPTY FIELD!!!                          '
            else:
                if (b in l) or (p in l):
                    me='               USERNAME OR PASSWORD IS ALREADY TAKEN                   '
                elif (' ' in b) or (' ' in p):
                    me='                           SPACES ARE NOT ALLOWED!!                    '            
                else:
                    me='                   USERNAME AND PASSWORD CREATED                       '
                    f=open('pswd.txt','a')
                    f.write(b+' '+p+'\n')
                    af=1
                    f.flush()
                    f.close()
            l2=Label(pg2,text=me,font=('Arial 12'),bg="black",fg="red")
            l2.place(x=845,y=400)
            if af==1:
                Button(pg2,image=bga5,width=92, height=28,command=lambda: [opening(),reset(1)],bg='black',fg='black').place(x=1027,y=465)
        if z==0:
            l2=Label(pg2,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t',font=('Arial 12'),bg="black",fg="red")
            l2.place(x=845,y=400)
            Button(pg2,image=bga1,width=92, height=28,command=lambda: pcheck2(1),bg='black',fg='black').place(x=1027,y=465)

    def pcheck(z):
        if z==1:
            global l1
            b=username.get()
            p=password.get()
            p1=passw.get()
            af=sqlchk(p1,1)
            v=0
            if L==[]:
                mes='                                        KINDLY LOGIN!!!                          '                
            elif b=='' or p=='' or p1=='':
                mes='                                 FILL THE EMPTY FIELD!!!                          '
            else:
                if ((b,p) in L) and af==1:
                    mes='                                        LOGIN SUCCESS                                 '
                    sqlchk(b,2)
                    v=1
                else:
                    mes='                    WRONG USERNAME OR PASSWORDS!!!                            '
    
            l1=Label(pg1,text=mes,font=('Arial 12'),bg="black",fg="red")
            l1.place(x=845,y=425)
            if v==1:
                shwfrm(pg3)
        if z==0:
            l1=Label(pg1,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t',font=('Arial 12'),bg="black",fg="red")
            l1.place(x=845,y=425)

    #############################pg0#######################
    bga0=PhotoImage(file='gamer.png')
    a3 = Canvas( pg0, width = 1280,height = 700)
    a3.pack(fill = "both", expand = True)  
    a3.create_image( 0, 0, image = bga0,anchor = "nw")    
    
    username = StringVar()
    password = StringVar()
    username1 = StringVar()
    password1 = StringVar()
    passw = StringVar()
    
    c=IntVar(value=0)
    cc=IntVar(value=0)
    ccc=IntVar(value=0)

    ################### Page 1 #####################    
    bga=PhotoImage(file='mainpg.png')
    bga1=PhotoImage(file='login.png')
    bga2=PhotoImage(file='crtacc.png')
    bga3=PhotoImage(file='mainpg1.png')
    bga5=PhotoImage(file='back.png')
    bga6=PhotoImage(file='main3.png')
    
    a1 = Canvas( pg1, width = 1280,height = 700)
    a1.pack(fill = "both", expand = True)  
    a1.create_image( 0, 0, image = bga,anchor = "nw")

    E1=Entry(pg1,width=24, font=('Arial 14'),textvariable=username,bg='#A7A7A7')
    E1.place(x=948,y=223)
    E2=Entry(pg1,width=21, font=('Arial 14'),textvariable=password ,show="-",bg='#A7A7A7')
    E2.place(x=948,y=288)
    E3=Entry(pg1,width=21, font=('Arial 14'),textvariable=passw,show="-",bg='#A7A7A7')
    E3.place(x=948,y=353)
    
    

    def m():
        if(c.get()==1):
            E2=Entry(pg1,width=21, font=('Arial 14'), textvariable=password,bg='#A7A7A7')
            E2.place(x=948,y=288)
        else:
            E2=Entry(pg1,width=21, font=('Arial 14'),textvariable=password,show="-",bg='#A7A7A7')
            E2.place(x=948,y=288)
    Checkbutton(pg1,variable=c,onvalue = 1, offvalue = 0, width=1, height=1,command=m,bg='black',fg='black').place(x=1183,y=288)
    
    def m2():
        if(cc.get()==1):
            E3=Entry(pg1,width=21, font=('Arial 14'),textvariable=passw,bg='#A7A7A7')
            E3.place(x=948,y=353)
        else:
            E3=Entry(pg1,width=21, font=('Arial 14'),textvariable=passw,show="-",bg='#A7A7A7')
            E3.place(x=948,y=353)
    Checkbutton(pg1,variable=cc,onvalue = 1, offvalue = 0, width=1, height=1,command=m2,bg='black',fg='black').place(x=1183,y=353)
    
    Button(pg1,image=bga1,width=92, height=28,command=lambda: pcheck(1),bd=0,bg='black',fg='black').place(x=1027,y=465)
    Button(pg1,image=bga2,width=80, height=20,command=lambda: [reset(0),shwfrm(pg2)],bd=0,bg='black',fg='black').place(x=1180,y=650)

    #################### page 2 ###########################
    
    a4 = Canvas( pg2, width = 1280,height = 700)
    a4.pack(fill = "both", expand = True)  
    a4.create_image( 0, 0, image = bga3,anchor = "nw")

    E4=Entry(pg2,width=24, font=('Arial 14'),textvariable=username1,bg='#A7A7A7')
    E4.place(x=948,y=223)
    E5=Entry(pg2,width=21, font=('Arial 14'),textvariable=password1 ,show="-",bg='#A7A7A7')
    E5.place(x=948,y=288)

    def m3():
        if(ccc.get()==1):
            E5=Entry(pg2,width=21, font=('Arial 14'), textvariable=password1,bg='#A7A7A7')
            E5.place(x=948,y=288)
        else:
            E5=Entry(pg2,width=21, font=('Arial 14'),textvariable=password1,show="-",bg='#A7A7A7')
            E5.place(x=948,y=288)
    Checkbutton(pg2,variable=ccc,onvalue = 1, offvalue = 0, width=1, height=1,command=m3,bg='black',fg='black').place(x=1183,y=288)
    Button(pg2,image=bga1,width=92, height=28,command=lambda: pcheck2(1),bd=0,bg='black',fg='black').place(x=1027,y=465)

    bga28=PhotoImage(file='home pg.png')
    Button(pg2,image=bga28,command=lambda: [opening(),shwfrm(pg1)],bd=0,bg='black',fg='black').place(x=1170,y=10)

    ##########################page 3#########################
    a2 = Canvas( pg3, width = 1280,height = 700)
    a2.pack(fill = "both", expand = True)  
    a2.create_image( 0, 0, image = bga6,anchor = "nw")

    def ACCDEL():
        b=username.get()
        p=password.get()
        cur.execute('drop table gaming_details_{}'.format(b))
        bsq.commit()
        f1=open('pswd.txt')
        f2=open('sam.txt','w')
        for i in f1.readlines():
            if i.strip()!=b+' '+p:
                f2.write(i)
        f1.close()
        f2.close()
        os.remove('pswd.txt')
        os.rename('sam.txt','pswd.txt')
            

    b1=PhotoImage(file='playgame.png')
    
    bga7=PhotoImage(file='XO.png')
    bga8=PhotoImage(file='mem.png') 
    bga9=PhotoImage(file='rps.png') 
    bga11=PhotoImage(file='turtle.png')

    bga71=PhotoImage(file='XO1.png')
    bga81=PhotoImage(file='mem1.png') 
    bga91=PhotoImage(file='rps1.png') 
    bga111=PhotoImage(file='turtle1.png')
    
    Button(pg3,image=bga71,command=lambda: Game(1,bga7),bd=0,bg='black',fg='black').place(x=145,y=215)
    Button(pg3,image=bga81,command=lambda: Game(2,bga8),bd=0,bg='black',fg='black').place(x=410,y=215)
    Button(pg3,image=bga91,command=lambda: Game(3,bga9),bd=0,bg='black',fg='black').place(x=675,y=215) 
    Button(pg3,image=bga111,command=lambda: Game(5,bga11),bd=0,bg='black',fg='black').place(x=940,y=215)
    
    bga30=PhotoImage(file='custom.png')
    Button(pg3,image=bga30,command=lambda: [Game(0,0),reset(1)],bd=0,bg='black',fg='black').place(x=1000,y=30)

    bga31=PhotoImage(file='DELE.png')
    Button(pg3,image=bga31,command=lambda: [ACCDEL(),opening(),Game(0,0),reset(1)],bd=0,bg='black',fg='black').place(x=60,y=25)
    

        
    def close(Z):
        try:
            bsq.close()
        except:
            pass
        if Z==1:
            file=open('store.txt','w')
            file.close()
            a.destroy()
    a.protocol('WM_DELETE_WINDOW',lambda:close(1))
    a.resizable(False,False)
    a.mainloop()

    
Loginform()
