
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("employees.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1200x760+0+0")
root.config(bg="brown")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
contact = StringVar()
email = StringVar()
address = StringVar()

#entries frame
entries_frame = Frame(root, bg="#2c3e50")
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 20, "bold"), bg="#2c3e50", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20,sticky="w")

labelName=Label(entries_frame, text="Name",font=("calibri",18), bg="#2c3e50", fg="white")
labelName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("calibri",18),width=30)
txtName.grid(row=1,column=1,sticky="w",padx=10,pady=10)


labelAge=Label(entries_frame, text="Age",font=("calibri",18), bg="#2c3e50", fg="white")
labelAge.grid(row=1,column=2, padx=10,pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("calibri",18), width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

labelDoj=Label(entries_frame, text="Date-of-Join",font=("calibri",18), bg="#2c3e50", fg="white")
labelDoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("calibri",18), width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

labelGender=Label(entries_frame, text="Gender",font=("calibri",18), bg="#2c3e50", fg="white")
labelGender.grid(row=2,column=2,padx=10,pady=10,sticky="w")
comboGender =ttk.Combobox(entries_frame,font=("calibri",18),width=28,textvariable=gender,state="readonly")
comboGender['values'] = ("Male","Female")
comboGender.grid(row=2,column=3,padx=10,sticky="w")

labelEmail=Label(entries_frame, text="Email",font=("calibri",18), bg="#2c3e50", fg="white")
labelEmail.grid(row=3,column=0,padx=10,pady=10,sticky="w")#
txtEmail = Entry(entries_frame, textvariable=email, font=("calibri",18), width=30)
txtEmail.grid(row=3,column=1,padx=10,pady=10,sticky="w")

labelContact=Label(entries_frame, text="Contact.NO",font=("calibri",18), bg="#2c3e50", fg="white")
labelContact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("calibri",18), width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

labelAddress=Label(entries_frame, text="Address",font=("calibri",18), bg="#2c3e50", fg="white")
labelAddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")

txtAddress=Text(entries_frame,width=85,height=5, font=("calibri",18))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
   # print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    contact.set(row[5])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[6])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END,values=row)


def add_employee():
    if txtName.get() =="" or txtAge.get() =="" or txtDoj.get() =="" or txtContact.get() =="" or txtEmail.get() =="" or comboGender.get() =="" or txtAddress.get(1.0, END) =="":
        messagebox.showerror("Error in Input", "Please fill all the details")
        return
    db.insert(txtName.get(), txtAge.get(), txtDoj.get(), txtContact.get(), txtEmail.get(), comboGender.get(), txtAddress.get(1.0, END))

    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()



def update_employee():
    if txtName.get() =="" or txtAge.get() =="" or txtDoj.get() =="" or txtContact.get() =="" or txtEmail.get() =="" or comboGender.get() =="" or txtAddress.get(1.0, END) =="":
        messagebox.showerror("Error in Input", "Please fill all the details")
        return
    db.update(row[0], txtName.get(), txtAge.get(), txtDoj.get(), txtContact.get(), txtEmail.get(), comboGender.get(), txtAddress.get(1.0, END))
    messagebox.showinfo("Success","Record updated")
    clearAll()
    displayAll()

def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)

btn_frame=Frame(entries_frame,bg="#2c3e50")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
Button(btn_frame, command=add_employee, text="Add details", width=13,
       font=("calibri", 12, "bold"), bg="#16a085",
       fg="white",bd=0).grid(row=0, column=0)

Button(btn_frame, command=update_employee, text="Update details", width=13,
       font=("calibri", 12, "bold"), bg="yellow",
       fg="white",bd=0).grid(row=0, column=1,padx=10)

Button(btn_frame, command=delete_employee, text="Delete details", width=13,
       font=("calibri", 12, "bold"), bg="blue",
       fg="white",bd=0).grid(row=0, column=2,padx=10)

Button(btn_frame, command=clearAll, text="Clear details", width=13,
       font=("calibri", 12, "bold"), bg="green",
       fg="white",bd=0).grid(row=0, column=3,padx=10)


#table frame
tree_frame = Frame(root, bg="white")
tree_frame.place(x=0,y=495,width=1400,height=500)
style = ttk.Style()
style.configure("mystyle.Treeview", font=("calibri",18),rowheight=50)
style.configure("mystyle.Treeview.Headings", font=("calibri",20,"bold"))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7),style="mystyle.Treeview")
tv.heading("1", text="Id")
tv.column("1",width=5)
tv.heading("2", text="Name")
tv.column("2",width=10)
tv.heading("3", text="Age")
tv.heading("4", text="D.o.j")
tv.column("4",width=20)
tv.heading("5", text="Gender")
tv.column("5",width=5)
tv.heading("6", text="Contact")
tv.heading("7", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()
root.mainloop()



