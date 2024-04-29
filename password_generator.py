import tkinter as tk

from tkinter import ttk, messagebox

import random as r


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
    all_new=''
    for i in all:
        if i in s:
            continue
        all_new+=i

    start=r.randrange(0,length-len(s),1)
    
    passw="".join(r.sample(all_new,start))+s+"".join(r.sample(all_new,length-(start+len(s))))
    
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

def copy_to_clipboard(text):

    root = tk.Tk()

    root.withdraw()

    root.clipboard_clear()

    root.clipboard_append(text)

    root.destroy()
  
def generate_and_display():
    try:
        lenn=int(password_length.get())
       
        if lenn<=0:
            raise ValueError("password should be a positive number")
        s=str(wrd.get())
        
        
        password=password_generate(s,lenn)
        strength=password_strength(password)
        status = "weak" if strength <= 5 else "moderate" if strength <= 10 else "strong"
        password_label.config(text="GENERATED PASSWORD: " + password,bg="black",fg="white",font=("franklin gothic medium",15,"italic","underline"))
        
        strength_label.config(text="GENERATED PASSWORD'S STRENGTH: " + str(strength)+" "+"("+status+")",bg="black",fg="white",font=("franklin gothic medium",15,"bold"))
        
        progress_bar['value'] = min(100, strength * 10)

        copy_button.config(command=lambda: copy_to_clipboard(password))
    except ValueError as e: 
        print("e")
    

root =tk.Tk()

root.title("PASSWORD GENERATOR")
root.geometry("777x555")
root.config(bg="black")
lable=tk.Label(text="ENTER LENGTH OF YOUR PASSWORD:",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"))
lable.pack()

password_length =tk.Entry(root)
password_length.pack()
label2=tk.Label(text="ENTER TEXT YOU WANT IN YOUR PASSWORD \n IF NOT CLICK (GENERATE PASSWORD):",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"))
label2.pack()
wrd = tk.Entry(root)
wrd.pack()

generate=tk.Button(root,text="GENERATE PASSWORD",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"), command=generate_and_display)
generate.pack()

label3=tk.Label(text="PASSWORD STRENGTH CATEGORY \n 0-5:WEAK \n 6-10:MODERATE \n 11+:STRONG\n ",bg="black",fg="yellow",font=("cascadia mono semibold",15,"bold"))
label3.pack()
        
password_label=tk.Label(root,text="")
password_label.pack() 

strength_label=tk.Label(root,text="" )
strength_label.pack()

progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')

progress_bar.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(""))

copy_button.pack()

root.mainloop()

