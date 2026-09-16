from customtkinter import *
import json , os 
from tkinter import messagebox as msg
home = os.path.expanduser("~")
os.chdir(os.path.join(home,"Desktop"))

mw = CTk()
mw.after(0,lambda:mw.state('zoomed'))

h = mw.winfo_screenheight()
w = mw.winfo_screenwidth()

frame = CTkFrame(mw,width=w-10,height=h-5,fg_color="#B9A8A8")
frame.place(x=5 ,y=70)

CTkLabel(mw,text="Name",font=("calibri" ,18, "bold"),text_color="#CACACA").place(x=80,y=40)
CTkLabel(mw,text="ID",font=("calibri" ,18, "bold"),text_color="#C2BDBD").place(x=290,y=40)
CTkLabel(mw,text="September",font=("calibri" ,18, "bold",),text_color="#CCCBCB",bg_color="transparent").place(x=800,y=40)

vline = CTkFrame(frame,width=1,height=h,border_color="#333333",border_width=1)
vline.place(x=200,y=0)

vline = CTkFrame(frame,width=1,height=h,border_color="#333333",border_width=1)
vline.place(x=400,y=0)

hline = CTkFrame(frame,width=w,height=1,border_width=1,border_color="#333333")
hline.place(x=0,y=60)

hline = CTkFrame(frame,width=w,height=1,border_width=1,border_color="#333333")
hline.place(x=420,y=30)

for i in range(1,31):
    n = i * 30
    vline = CTkFrame(frame,width=1,height=h,border_color="#333333",border_width=1)
    vline.place(x=400+n,y=0)
    
days = ['M','T','W','T','F','S','S']   
for i in range(30):
    n = i * 30
    CTkLabel(frame,text=days[i % 7],font=("calibri" , 16 ,"bold"),text_color="#333333").place(x=410+n,y=0)
    CTkLabel(frame,text=f"{i+1:02d}",font=("calibri" , 16 ,"bold"),text_color="#333333").place(x=408+n,y=30)
ERA_ID = {}
ERA_ID = dict()
def refresh():
    global ERA_ID
    if  os.path.exists("database.json"):
        with open("database.json","r") as file:
            try:
                ERA_ID = json.load(file)
                print(ERA_ID)
            except:
                ERA_ID = {}
                ERA_ID = dict()
                
                
    for idx , key in enumerate(ERA_ID.keys()):
        cell = idx * 30
        data = ERA_ID[key]

        CTkLabel(frame,font=("Arial",15),text=f"{idx+1}.  {data[0]}",text_color="#000000").place(x=10,y=62+cell)
        CTkLabel(frame,font=("Arial",15),text=f"{data[1]}",text_color="#000000").place(x=230,y=62+cell)
        for i in range(len(ERA_ID)):
            cell = i * 30
            hline = CTkFrame(frame,width=w,height=1,border_width=1,border_color="#333333")
            hline.place(x=0,y=90+cell)
refresh()



def add_id():
    add = CTkToplevel(mw)
    add.transient(mw)
    add.title("Add ERA ID")
    x = int((w / 2) - (360 / 2))
    y = int((h / 2) - (150 / 2))
    add.geometry(f"360x150+{x}+{y}")
    add.resizable(False,False)

    CTkLabel(add,text="NAME",font=("Arial",15),text_color="#ffffff").grid(row=0,column=0,padx=10,sticky="w",pady=(10,0))
    CTkLabel(add,text="ERA ID",font=("Arial",15),text_color="#ffffff").grid(row=1,column=0,padx=10,sticky="w")
    
    e1 = CTkEntry(add,font=("Arial",16),width=270,fg_color="#ffffff",text_color="#000000")
    e1.grid(row=0,column=1,padx=10,pady=(20,10),sticky="w")
    
    e2 = CTkEntry(add,font=("Arial",16),width=270,fg_color="#ffffff",text_color="#000000")
    e2.grid(row=1,column=1,padx=10,sticky="w")

    def submit():
        name =e1.get()
        era = e2.get()

        sr_no = str(len(ERA_ID) + 1)
        ERA_ID[sr_no] = [name,era]
        msg.showinfo("Success!","ERA ID updated successfully!")
        e1.delete(0,"end")
        e2.delete(0,"end")
        with open("database.json","w") as file:
            json.dump(ERA_ID,file,indent=4)
        refresh()



    CTkButton(id,text="Add ID",font=("Arial",15),width=100,command=submit).grid(row=2,column=0,columnspan=2,pady=15)
    add.mainloop()



CTkButton(mw,text="Add ID",font=("Arial",15),command=add_id).place(x=1220,y=5)
CTkButton(mw,text="Edit ID",font=("Arial",15)).place(x=1220,y=37)
mw.mainloop()