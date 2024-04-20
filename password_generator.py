import random as r
from tkinter import *

def password_generate(s,length):
    A=''
    for i in range(65,91,1):
        A+=chr(i)
    a=''
    for i in range(97,123,1):
        a+=chr(i)
        
    ss=''
    for i in range(33,48,1):
        ss+=chr(i)
    n=''
    for i in range(48,58,1):
        n+=chr(i)

    all=A+a+ss+n

    start=r.randrange(0,length-len(s),1)
    
    passw="".join(r.sample(all,start))+s+"".join(r.sample(all,length-(start+len(s))))
    
    return passw

def password_strength(s):
    score=0
    if len(s)>8:
        score+=2*(len(s)-8)
    if any(char.isupper() for char in s):
        score+=1
    if any(char.islower() for char in s):
        score+=1
    num="0123456789"
    if any(char in num for char in s):
        score+=1
    ss=''
    for i in range(33,48,1):
        ss+=chr(i)
    if any(char in ss for char in s):
        score+=1
    return score
    
    
    
def generate_and_display():
    try:
        lenn=int(password_length.get())
       
        if lenn<=0:
            raise ValueError("password should be a positive number")
        s=str(wrd.get())
        
         
        password=password_generate(s,lenn)
        strength=password_strength(password)
        status=''
        if strength<=5:status="weak"
        elif strength>=6 and strength<=10:status="moderate"
        else:status="strong"
        password_label.config(text="GENERATED PASSWORD: " + password,bg="black",fg="white",font=("franklin gothic medium",15,"italic","underline"))
       
        strength_label.config(text="GENERATED PASSWORD'S STRENGTH: " + str(strength)+" "+"("+status+")",bg="black",fg="white",font=("franklin gothic medium",15,"bold"))
    except ValueError as e: 
        print("e")
    

root =Tk()

root.title("PASSWORD GENERATOR")
root.geometry("555x444")
root.config(bg="black")
lable=Label(text="ENTER LENGTH OF YOUR PASSWORD:",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"))
lable.pack()

password_length = Entry(root)
password_length.pack()
label2=Label(text="ENTER TEXT YOU WANT IN YOUR PASSWORD \n IF NOT CLICK (GENERATE PASSWORD):",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"))
label2.pack()
wrd = Entry(root)
wrd.pack()

generate=Button(root,text="GENERATE PASSWORD",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"), command=generate_and_display)
generate.pack()
label3=Label(text="PASSWORD STRENGTH CATEGORY \n 0-5:WEAK \n 6-10:MODERATE \n 11+:STRONG\n ",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"))
label3.pack()
        
password_label=Label(root,text="")
password_label.pack() 

strength_label=Label(root,text="" )
strength_label.pack()

root.mainloop()