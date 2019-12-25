from tkinter import *
import backend



# from the listbox get the tuple with the index x
def get_selected_row(event):
    global selected_tuple
    if list1.curselection():
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])




def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])



def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())







window=Tk()

window.wm_title("Welcome { The Z BookStore } ")

l1=Label(window,text="Title",fg="red")
l1.grid(row=0,column=0)

l2=Label(window,text="Author",fg="red")
l2.grid(row=0,column=2)

l3=Label(window,text="Year",fg="red")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN",fg="red")
l4.grid(row=1,column=2)


title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1,padx=2, pady=2)


author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3,padx=2, pady=2)


year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1,padx=2, pady=2)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3,padx=2, pady=2)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6,columnspan=2,padx=2, pady=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,padx=2, pady=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)



b1=Button(window,text="View all", width=12,background="#b3ffff",fg="red",command=view_command)
b1.grid(row=2,column=3,padx=1, pady=1)

b2=Button(window,text="Search entry", width=12,background="#b3ffff",fg="red",command=search_command)
b2.grid(row=3,column=3,padx=1, pady=1)

b3=Button(window,text="Add entry", width=12,background="#b3ffff",fg="red",command=add_command)
b3.grid(row=4,column=3,padx=1, pady=1)

b4=Button(window,text="Update selected", width=12,background="#b3ffff",fg="red",command=update_command)
b4.grid(row=5,column=3,padx=1, pady=1)

b5=Button(window,text="Delete selected", width=12, background='#ff99cc',command=delete_command)
b5.grid(row=6,column=3, padx=1, pady=1)

b6=Button(window,text="Close", width=12,background="#b3ffff",fg="red",command=window.destroy)
b6.grid(row=7,column=3, padx=1, pady=1)





window.mainloop()
