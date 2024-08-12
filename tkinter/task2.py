import tkinter

app=tkinter.Tk()
a=tkinter.Canvas(app,width=400,height=400,bg='green')
a.create_line(0,100,100,100,fill='black')
a.create_rectangle(50,50,300,300,fill="red")
a.create_oval(100,120,200,200,fill="blue")
a.create_polygon(100,100,100,100,fill="violet")
a.pack()
app.mainloop()
