from tkinter import *
from tkinter import messagebox
import math
import string
root=Tk()
root.geometry("375x375")
root.title("Cryptography")
root.resizable(FALSE,FALSE)	
def num(p,q):
    return p*q

def phi(p,q):
    return (p-1)*(q-1)

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

def get_e(p):
    e=2 
    while gcd(p,e)!=1:
      e=e+1
    return e 

def get_d(e, p):
  n=1 
  while (p*n+1) % e !=0:
       n=n+1  
  d=(p*n+1)/e
  return d

def encryption(e, N, msg):
    cipher = ""
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "
    return cipher

def decryption(d, N, cipher):
    msg = ""
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))
        print(msg)    
    return msg
  
def clear():
    Code.set("")
    text1.delete(1.0,END)

def encrypt():
    code=Code.get()
    if code=="123":
        app=Toplevel(root)
        app.title("Encryption")
        app.geometry("400x200")
        app.configure(bg="black")
        plaintext = text1.get(1.0,END)
        p=phi(59,61)
        n=num(59,61)
        e=get_e(p)
        d=get_d(e, p)
        d=int(d)
        print ("Plaintext:",plaintext)
        print ("Public Key:(",e,",",n,")")
        print ("Private Key:(",d,",",n,")")
        ciphertext=encryption(e,n,plaintext)
        print ('Ciphertext:' ,ciphertext)
        Label(app,text="ENCRYPTED TEXT",font="arial",fg="black",bg="grey").place(x=10,y=0)
        text2=Text(app,font="bold",bg="white",relief=GROOVE,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,ciphertext)
        app.mainloop()
    elif code=="":
        messagebox.showerror("Encryption","Input Password")
    else:
        messagebox.showerror("Encryption","Invalid Password")

def decrypt(): 
    code=Code.get()
    if code=="123":
        app=Toplevel(root)
        app.title("Decryption")
        app.geometry("400x200")
        app.configure(bg="black")
        ciphertext = text1.get(1.0,END)
        p=phi(59,61)
        n=num(59,61)
        e=get_e(p)
        d=get_d(e, p)
        d=int(d)
        print ("Ciphertext:",ciphertext)
        print ("Public Key:(",e,",",n,")")
        print ("Private Key:(",d,",",n,")")
        plaintext=decryption(d,n,ciphertext)
        print ('Plaintext:',plaintext)
        Label(app,text="DECRYPTED TEXT",font="arial",fg="black",bg="grey").place(x=10,y=0)
        text2=Text(app,font="bold",bg="white",relief=GROOVE,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,plaintext)
        app.mainloop()
    elif code=="":
        messagebox.showerror("Decryption","Input Password")
    else:
        messagebox.showerror("Decryption","Invalid Password")

Label(text="Enter the text for encrytion or decryption",fg="black",font=("calibri",13)).place(x=10,y=10)
text1=Text(root,font="Bold",bg="white",relief=GROOVE,bd=1)
text1.place(x=10,y=50,width=355,height=100)
Label(text="Enter the Passcode",fg="black",font=("calibri",13)).place(x=10,y=170 )
Code=StringVar()
Entry(textvariable=Code,bg="white",fg="black",width=19,bd=2,font=("arial",25),show="*").place(x=10,y=200)
Button(text="Encrypt",font=("bold",10),height="2",width="23",bg="red",fg="black",bd=0,command=encrypt).place(x=10,y=250)
Button(text="Decrypt",font=("bold",10),height="2",width="23",bg="green",fg="black",bd=0,command=decrypt).place(x=200,y=250)
Button(text="CLEAR",height="2",width="50",bg="yellow",fg="black",bd=0,command=clear).place(x=11,y=300)
root.mainloop()