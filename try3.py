from tkinter import *
from PIL import ImageTk, Image
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
import csv
global Marquee


class Marquee(tk.Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas.
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        # start the animation
        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)

        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)


def root():
    global root
    window.destroy()
    root = tk.Tk()
    root.title("STUDENT MANAGEMENT PORTAL")
    root.resizable(width=FALSE, height=FALSE)
    #root.geometry('500x400')
    root.config(bg="#a5b7c3")

    image = Image.open('business-3528035_960_720.jpg')
    photo_image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo_image)
    label.pack()
    mycolor = "#a5b7c3"

    w = Label(root, text='WELCOME TO STUDENT MANAGEMENT PORTAL', font=("Georgia", 14), fg="black", bg="lightblue").place(x=20, y=30)

    img = Image.open("home.png")
    tkimage = ImageTk.PhotoImage(img)
    tk.Label(root, image=tkimage, bg=mycolor).place(x=210, y=65)


    w1 = Label(root, text='MAIN MENU', font=("Arial black", 18), fg="Royalblue1",  bg=mycolor).place(x=155, y=120)

    T = Label(root, text='Retrive data from the register ' , fg="gray14",font=("Trebuchet MS", 14), bg=mycolor).place(x=30, y=170)

    T1 = Label(root, text='Add details to register', fg="gray14",font=("Trebuchet MS", 14), bg=mycolor).place(x=30, y=210)

    T2 = Label(root, text='Delete data from the register', fg="gray14",font=("Trebuchet MS", 14), bg=mycolor).place(x=30, y=250)

    T3 = Label(root, text='Edit data from the register', fg="gray14",font=("Trebuchet MS", 14), bg=mycolor).place(x=30, y=290)

    button = tk.Button(root, text="CLICK ME!", fg="black", command=display_item, highlightthickness=0, relief='flat')
    button.place(x=370, y=170)
    original = Image.open('icons8-next-page-24 (1).png')
    ph_im = ImageTk.PhotoImage(original)
    button.config(image=ph_im, bg=mycolor)

    button1 = tk.Button(root, text="CLICK ME!", fg="black", command=add_item, highlightthickness=0, relief='flat')
    button1.place(x=370, y=210)
    original1 = Image.open('icons8-next-page-24 (1).png')
    ph_im1 = ImageTk.PhotoImage(original1)
    button1.config(image=ph_im1, bg=mycolor)

    button2 = tk.Button(root, text="CLICK ME!", fg="black", command=delete_portal, highlightthickness=0, relief='flat')
    button2.place(x=370, y=250)
    original2 = Image.open('icons8-next-page-24 (1).png')
    ph_im2 = ImageTk.PhotoImage(original2)
    button2.config(image=ph_im2, bg=mycolor)

    button3 = tk.Button(root, text="CLICK ME!", fg="black", command=edit_portal, highlightthickness=0, relief='flat')
    button3.place(x=370, y=290)
    original3 = Image.open('icons8-next-page-24 (1).png')
    ph_im3 = ImageTk.PhotoImage(original3)
    button3.config(image=ph_im3, bg=mycolor)

    marquee = Marquee(root, text="NOTICE : This program is running for VENOm university.", borderwidth=0,relief="sunken")
    marquee.pack(side="bottom", fill="x")
    root.mainloop()

def edit_add():
    global e1, e2, e3, e4, top3

    top3 = tk.Toplevel()
    top3.geometry("500x400")

    image = Image.open('wp2164076-accounting-wallpapers.jpg')
    photo_image = ImageTk.PhotoImage(image)
    label = tk.Label(top3, image=photo_image).place(x=0, y=0, relwidth=1, relheight=1)

    img = Image.open("Contact Info (1).png")
    tkimage = ImageTk.PhotoImage(img)
    tk.Label(top3, image=tkimage).place(x=200, y=90)

    m = Label(top3, text='STUDENTS MANAGMENT', font=("Helvetica", 14), fg="gray14", bg='lightgreen').place(x=125, y=50)


    name = Label(top3, text="Name").place(x=30, y=170)

    branch = Label(top3, text="Branch").place(x=30, y=210)

    course = Label(top3, text="Course").place(x=30, y=250)

    sem = Label(top3, text="Semester").place(x=30, y=290)





    sbmitbtn = Button(top3, text="Submit", activebackground="pink", activeforeground="blue", command=edit_item).place(x=30, y=330)

    sbmitbtn = Button(top3, text="Exit", activebackground="pink", activeforeground="blue", command=top3.destroy).place(x=100, y=330)

    e1 = Entry(top3)
    e1.place(x=80, y=170)

    e2 = Entry(top3)
    e2.place(x=80, y=210)

    e3 = Entry(top3)
    e3.place(x=95, y=250)

    e4 = Entry(top3)
    e4.place(x=95, y=290)



    top3.mainloop()


def add_item():
    global e1, e2, e3, e4, top

    top = tk.Toplevel()
    #top.config(bg='green4')
    top.resizable(width=FALSE, height=FALSE)
    top.geometry("500x400")

    image = Image.open('wp2164076-accounting-wallpapers.jpg')
    photo_image = ImageTk.PhotoImage(image)
    label = tk.Label(top, image=photo_image).place(x=0, y=0, relwidth=1, relheight=1)

    img = Image.open("Contact Info (1).png")
    tkimage = ImageTk.PhotoImage(img)
    tk.Label(top, image=tkimage).place(x=200, y=90)

    m = Label(top, text='STUDENTS MANAGMENT', font=("Helvetica", 14), fg="gray14", bg='lightgreen').place(x=125, y=50)


    name = Label(top, text="Name").place(x=30, y=170)

    branch = Label(top, text="Branch").place(x=30, y=210)

    course = Label(top, text="Course").place(x=30, y=250)

    sem = Label(top, text="Semester").place(x=30, y=290)





    sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue", command=enter_button).place(x=30, y=330)

    sbmitbtn = Button(top, text="Exit", activebackground="pink", activeforeground="blue", command=top.destroy).place(x=100, y=330)

    e1 = Entry(top)
    e1.place(x=80, y=170)

    e2 = Entry(top)
    e2.place(x=80, y=210)

    e3 = Entry(top)
    e3.place(x=95, y=250)

    e4 = Entry(top)
    e4.place(x=95, y=290)

    top.mainloop()


def image():
    w = Canvas(top1, width=300, height=400, bg="white")
    w.place(x=300, y=0, anchor=NW)
    photo = PhotoImage(file="icons8-trash-can-100.png")
    item = w.create_image(152, 200, image=photo)


def delete_portal():

    global E1, top1

    top1 = tk.Toplevel()
    top1.title("Deletion Portal")
    top1.geometry('800x600')
    top1.config(bg='white')

    image = Image.open('wp2164076-accounting-wallpapers.jpg')
    photo_image = ImageTk.PhotoImage(image)
    label = tk.Label(top1, image=photo_image).place(x=0, y=0, relwidth=1, relheight=1)

    Label(top1, text='DELETION PORTAL', font=("Helvetica", 14), fg="gray14").place(x=300, y=10)
    Label(top1, text='LIST OF DATA REGISTERED IN YOUR DATABASE', font=("Helvetica", 12), fg="gray14", bg="lightgreen").place(x=350, y=50)
    Label(top1, text='NOTE: The index number are reverse in order\n i.e. last entry has index 0', font=("Helvetica", 10), fg="gray14", bg='white').place(x=10, y=180)

    width = 800
    height = 600

    screen_width = top1.winfo_screenwidth()
    screen_height = top1.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    top1.resizable(0, 0)

    TableMargin = Frame(top1)
    TableMargin.place(x=280, y=80)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("NAME", "BRANCH", "COURSE", "SEMESTER"), height=20,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('BRANCH', text="BRANCH", anchor=W)
    tree.heading('COURSE', text="COURSE", anchor=W)
    tree.heading('SEMESTER', text="SEMESTER", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.pack()

    with open('File12.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NAME = row['NAME']
            BRANCH = row['BRANCH']
            COURSE = row['COURSE']
            SEM = row['SEM']
            tree.insert("", 0, values=(NAME, BRANCH, COURSE, SEM))

    Label(top1, text="Enter the index you want to delete :").place(x=5, y=270)
    E1 = Entry(top1, width=10)
    E1.place(x=200, y=270)
    Button(top1, text="OK", command=delete_item).place(x=210, y=310)

    w = Canvas(top1, width=80, height=70, bg="white")
    w.place(x=95, y=30, anchor=NW)
    photo = PhotoImage(file="icons8-trash-can-50.png")
    item = w.create_image(40, 40, image=photo)

    top1.mainloop()


def delete_item():
    try:
        import pandas as pd
        amount = E1.get()
        amount = int(amount)
        df = pd.read_csv("File12.csv")
        df.drop([amount], axis=0, inplace=True)
        csv_file = open(r"File12.csv", 'w')
        csv_file.truncate()
        csv_file.close()
        df.to_csv(r"File12.csv", index=False)
        messagebox.showinfo("-- COMPLETE --", "Selected Entry Deleted.", icon="info")
        top1.destroy()
    except KeyError:
        messagebox.showinfo("-- ERROR --", "Please enter valid index!", icon="warning")

    #display = Label(top1, text="ITEM deleted successfully !")
    #display.config(bg='red')
    #display.pack(side=BOTTOM)


def edit_portal():

    global E2, top2

    top2 = tk.Toplevel()
    top2.title("Manupulation Portal")
    top2.geometry('800x600')
    top2.config(bg='white')

    image = Image.open('wp2164076-accounting-wallpapers.jpg')
    photo_image = ImageTk.PhotoImage(image)
    label = tk.Label(top2, image=photo_image).place(x=0, y=0, relwidth=1, relheight=1)

    Label(top2, text='EDIT PORTAL', font=("Helvetica", 14), fg="gray14").place(x=300, y=10)
    Label(top2, text='LIST OF DATA REGISTERED IN YOUR DATABASE', font=("Helvetica", 12), fg="gray14", bg="lightgreen").place(x=350, y=50)
    Label(top2, text='NOTE: The index number are reverse in order\n i.e. last entry has index 0', font=("Helvetica", 10), fg="gray14", bg='white').place(x=10, y=180)

    width = 800
    height = 600

    screen_width = top2.winfo_screenwidth()
    screen_height = top2.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    top2.geometry("%dx%d+%d+%d" % (width, height, x, y))
    top2.resizable(0, 0)

    TableMargin = Frame(top2)
    TableMargin.place(x=280, y=80)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("NAME", "BRANCH", "COURSE", "SEMESTER"), height=20,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('BRANCH', text="BRANCH", anchor=W)
    tree.heading('COURSE', text="COURSE", anchor=W)
    tree.heading('SEMESTER', text="SEMESTER", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.pack()

    with open('File12.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            name = row['NAME']
            branch = row['BRANCH']
            course = row['COURSE']
            sem = row['SEM']
            tree.insert("", 0, values=(name, branch, course, sem))

    Label(top2, text="Enter the index you want to edit :").place(x=5, y=270)
    E2 = Entry(top2, width=10)
    E2.place(x=200, y=270)
    Button(top2, text="OK", command=edit_add).place(x=210, y=310)

    w = Canvas(top2, width=80, height=80, bg="white")
    w.place(x=95, y=30, anchor=NW)
    photo = PhotoImage(file="icons8-edit-profile-80.png")
    item = w.create_image(40, 40, image=photo)

    top2.mainloop()


def edit_item():
    amount = e1.get()
    amount1 = e2.get()
    amount2 = e3.get()
    amount3 = e4.get()
    with open('File12.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([amount, amount1, amount2, amount3])  # write Date/Time and the value
    f.close()
    try:
        import pandas as pd
        edit = E2.get()
        edit = int(edit)
        df = pd.read_csv("File12.csv")
        df.drop([edit], axis=0, inplace=True)
        csv_file = open(r"File12.csv", 'w')
        csv_file.truncate()
        csv_file.close()
        df.to_csv(r"File12.csv", index=False)
        top2.destroy()
        messagebox.showinfo("-- COMPLETE --", "Selected Entry Edited.", icon="info")
        top3.destroy()
    except KeyError:
        top2.destroy()
        messagebox.showinfo("-- ERROR --", "Please enter valid index!", icon="warning")
        top3.destroy()




    #display = Label(top3, text="ITEM edited successfully !")
    #display.config(bg='lightgreen')
    #display.place(x=170, y=370)


def enter_button():

    amount = e1.get()
    amount1 = e2.get()
    amount2 = e3.get()
    amount3 = e4.get()
    with open('File12.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([amount, amount1, amount2, amount3])  # write Date/Time and the value
    f.close()
    messagebox.showinfo("-- COMPLETE --", "Data Registered Successfully", icon="info")
    top.destroy()
    #display = Label(top, text="ITEM inserted successfully !")
    #display.config(bg='lightgreen')
    #display.place(x=170, y=370)


def display_item():
    root = Tk()
    root.title("STUDENTS REGISTER")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("NAME", "BRANCH", "COURSE", "SEMESTER"), height=400,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('NAME', text="NAME", anchor=W)
    tree.heading('BRANCH', text="BRANCH", anchor=W)
    tree.heading('COURSE', text="COURSE", anchor=W)
    tree.heading('SEMESTER', text="SEMESTER", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.pack()

    with open('File12.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            name = row['NAME']
            branch = row['BRANCH']
            course = row['COURSE']
            sem = row['SEM']
            tree.insert("", 0, values=(name, branch, course, sem))


global window, username, password
window = tk.Tk()
window.resizable(width=FALSE, height=FALSE)

username = "admin"
password = "123"


image = Image.open('business-3528035_960_720.jpg')
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo_image)
label.pack()
mycolor = "#a5b7c3"
label1 = Label(window, text="**WELCOME TO VeNom's UNIVERSITY**", font=("Georgia bold", 16), bg=mycolor)
label1.place(x=20, y=30)



def try_login():
    print("Trying to login...")
    if username_guess.get() == username and password_guess.get() == password:
        messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
        root()
    else:
        messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")


img = Image.open("lock (2).png")
tkimage = ImageTk.PhotoImage(img)
tk.Label(window, image=tkimage, bg=mycolor).place(x=110, y=145)

    #Creating the username & password entry boxes
Label(window, text="*AUTHORISED ONLY*", font=("Trebuchet MS", 14), bg=mycolor).place(x=60, y=100)
username_text = Label(window, text="Username:", bg=mycolor)
username_guess = Entry(window)
password_text = Label(window, text="Password:", bg=mycolor)
password_guess = Entry(window, show="*")

    #attempt to login button
attempt_login = Button(window, text="Login", command=try_login)
attempt_exit = Button(window, text="Exit", command=window.destroy)

username_text.place(x=10, y=240)
username_guess.place(x=100, y=240)
password_text.place(x=10, y=270)
password_guess.place(x=100, y=270)
attempt_login.place(x=135, y=300)
attempt_exit.place(x=190, y=300)

window.mainloop()
