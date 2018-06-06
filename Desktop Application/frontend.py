from tkinter import *

window=Tk()
l1=Label(window,text="Title",width=10)
l1.grid(row=0,column=0)

l1=Label(window,text="Author",width=10)
l1.grid(row=0,column=2)

l1=Label(window,text="Year",width=10)
l1.grid(row=1,column=0)

l1=Label(window,text="ISBN",width=10)
l1.grid(row=1,column=2)

e1_text=StringVar()
e1=Entry(window,textvariable=e1_text,width=15)
e1.grid(row=0,column=1)

e2_text=StringVar()
e2=Entry(window,textvariable=e2_text,width=15)
e2.grid(row=0,column=3)

e3_text=StringVar()
e3=Entry(window,textvariable=e3_text,width=15)
e3.grid(row=1,column=1)

e4_text=StringVar()
e4=Entry(window,textvariable=e4_text,width=15)
e4.grid(row=1,column=3)

ls1=Listbox(window,height=6,width=35)
ls1.grid(row=2,column=0,rowspan=6,columnspan=2)

sc1=Scrollbar(window)
sc1.grid(row=4,column=2,rowspan=5)

ls1.configure(yscrollcommand=sc1.set)
sc1.configure(command=ls1.yview)

b1=Button(window,text="View All",width=15)
b1.grid(row=2,column=3)

b1=Button(window,text="Search Entry",width=15)
b1.grid(row=3,column=3)

b1=Button(window,text="Add Entry",width=15)
b1.grid(row=4,column=3)

b1=Button(window,text="Update",width=15)
b1.grid(row=5,column=3)

b1=Button(window,text="Delete",width=15)
b1.grid(row=6,column=3)

b1=Button(window,text="Close",width=15)
b1.grid(row=7,column=3)





window.mainloop()
