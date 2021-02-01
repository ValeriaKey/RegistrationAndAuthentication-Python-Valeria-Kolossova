#Functions
def registration():
    #Welcome
    welcome = Label(text="Welcome to FaceBoom!", font=("Times",20,"bold"), fg="blue",bg="lightgray")
    welcome1 = Label(text="Registration:", font=("Times",20,"bold","underline"), fg="blue",bg="lightgray")
    welcome.pack()
    welcome1.pack()
    
    #Spaces
    space = Label(text="\n", bg="lightgray")
    space.pack()

    
    #Login label and enter
    text_log = Label(text="New login: ", font=("Times",15,"bold"),bg="lightgray")
    text_log.pack()
    register_login = Entry(win, bd="3")
    register_login.pack()
    
    #Password and enter 1
    text_password1 = Label(text="Enter your password:", font=("Times",15,"bold"),bg="lightgray")
    register_pass = Entry(win,bd="3",show="*")
    text_password1.pack()
    register_pass.pack()
    
    #Password and enter 2
    text_password2 = Label(text="Confirm your password: ", font=("Times",15,"bold"),bg="lightgray")
    register_password2 = Entry(win,bd="3",show="*")
    text_password2.pack()
    register_password2.pack()
    
    #Space
    space1 = Label(text=" ", bg="lightgray")
    space1.pack()
    
    #Checkbutton
    Rights = Checkbutton(win,text="Rules learned", bg="lightgray", font=("Times",15,"bold"))
    Rights.pack()
    
    #Button 
    button_register = Button(text="Registration",bg="lightgray",font=("Times",15,"bold"),command=lambda:save())
    button_register.pack()
    #Space
    space3 = Label(text=" ", bg="lightgray")
    space3.pack()

    def save():
        login_pass_save = {}
        login_pass_save[register_login.get()] = register_pass.get()
        f = open("login.txt","wb")
        dump(login_pass_save, f)
        f.close()
        login()
        
def login():
#Login
    text_log = Label(text="Faceboom message: ", font=("Times",15,"bold","underline"),fg="blue",bg="lightgray")
    text_log1= Label(text="Wuuhu! You are registrated! ", font=("Times",15,"bold"),fg="red",bg="lightgray")
    text_log.pack()
    text_log1.pack()
  
    space5 = Label(text="\n",bg="lightgray")
    space5.pack()
    
    text_log2= Label(text="Authentication", font=("Times",25,"bold","underline"),fg="black",bg="lightgray")
    text_log2.pack()
    
    text_enter_login = Label(text="Enter your login:",font=("Times",15,"bold"),bg="lightgray")
    text_enter_login.pack()
    
    enter_login = Entry(win,bd="3")
    enter_login.pack()
    
    text_enter_pass = Label(text="Enter your password:",font=("Times",15,"bold"),bg="lightgray")
    text_enter_pass.pack()
    
    enter_password = Entry(win,bd="3",show="*")
    enter_password.pack()
    
    #Space
    space6 = Label(text=" ", bg="lightgray")
    space6.pack()
    #Button
    button_enter = Button(text="Enter",bg="lightgray",font=("Times",15,"bold"), command=lambda:messages())
    button_enter.pack()



    #Output message windows
    def messages():
        f = open("login.txt", "rb")
        check = load(f)
        f.close()
        if enter_login.get() in check:
            if enter_password.get() == check[enter_login.get()]:
                name = enter_login.get()
                messagebox.showinfo("FACEBOOM",f"Welcome, {name}!")
            else:
                messagebox.showerror("FACEBOOM:Error!", "Uncorrect login or password!\n")
            
        
#Libraries
from tkinter import *
from tkinter import messagebox
from pickle import *

# Window / Title
win = Tk()
win.geometry("300x700")
win.title("FaceBoom")
win.config(bg="lightgray")



registration()
win.mainloop()
