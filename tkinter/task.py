import tkinter
from tkinter import messagebox
app=tkinter.Tk()

def data():
    # d1=d.get()
    # a1.config(text=d1)
    #messagebox.askyesno('display',d.get())
    if v_ch1.get()==1:
        print('mal select')
    if v_ch2.get()==1:
        print('eng select')
    if vr1.get()==1:
        print('male_')
    if vr1.get()==2:
        print('female_')


app.title("welcome")
app.minsize(400,400)
app.maxsize(600,600)
app.config(bg="yellow")
a=tkinter.Label(app,text='hello',bg='yellow',fg='black')
a.pack()
d=tkinter.StringVar()
b=tkinter.Entry(app,textvariable=d)
b.pack()
v_ch1=tkinter.IntVar()
v_ch2=tkinter.IntVar()
ch1=tkinter.Checkbutton(app,text='mal',variable=v_ch1)
ch1.pack()
ch2=tkinter.Checkbutton(app,text='eng',variable=v_ch2)
ch2.pack()
vr1=tkinter.IntVar()
r1=tkinter.Radiobutton(app,text='male',value=1,variable=vr1)
r2=tkinter.Radiobutton(app,text='female',value=2,variable=vr1)
r1.pack()
r2.pack()
c=tkinter.Button(app,text="save",bg='black',fg='white',activebackground='green',activeforeground='red',padx=20,pady=10,command=data)
c.pack()
a1=tkinter.Label(app,bg='yellow',fg='black')
a1.pack()
app.mainloop()


# import tkinter
# from tkinter import messagebox
# app = tkinter.Tk()
# def data():
#     # v=v1.get()
#     # l2.config(text=v)
#     # messagebox.showinfo("display",v1.get())
#     # messagebox.askokcancel("display",v1.get())
#     if v_c1.get()==1:
#         print("mal select")
#     if v_c2.get()==1:
#         print("eng selected")    
#     if vr1.get()==1:
#         print("male")
#     if vr1.get()==2:
#         print("female")    
# app.title("synnefo")
# app.minsize(400,400)
# app.maxsize(600,600)
# app.config(bg="red")
# l1=tkinter.Label(app,text="welcome",bg="red",fg="blue")
# l1.pack()
# v1=tkinter.StringVar()
# e1=tkinter.Entry(app,textvariable=v1)
# e1.pack()
# v_c1=tkinter.IntVar()
# v_c2=tkinter.IntVar()
# c1=tkinter.Checkbutton(app,text="mal",variable=v_c1)
# c1.pack()
# c2=tkinter.Checkbutton(app,text="eng",variable=v_c2)
# c2.pack()
# vr1=tkinter.IntVar()
# r1=tkinter.Radiobutton(app,text="male",value=1,variable=vr1)
# r2=tkinter.Radiobutton(app,text="female",value=2,variable=vr1)
# r1.pack()
# r2.pack()
# b1=tkinter.Button(app,text="save",bg="black",fg="white",activebackground="green",activeforeground="red",padx=10,pady=10,command=data)
# b1.pack()
# l2=tkinter.Label(app)
# l2.pack()
# app.mainloop()