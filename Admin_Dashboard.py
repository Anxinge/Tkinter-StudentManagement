# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:19:27 2019

@author: ashwin
"""
from tkinter import  *
import sqlite3
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import  ttk, Tk, StringVar

def Database_pf():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `professor_admin` (pf_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, pf_name TEXT, pf_code TEXT, pf_pword TEXT, pf_subject_flag INTEGER, pf_student_flag INTEGER)")

def Database_st():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `student_admin` (st_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, st_name TEXT, st_code TEXT, st_pword TEXT, st_subject_flag INTEGER,st_professor_flag INTEGER)")

def Database_cr():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `course_admin` (Course_No INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Subject_1 TEXT, Subject_2 TEXT, Subject_3 TEXT, Subject_4 TEXT,Subject_5 TEXT)")


def professor_register():
    global  Pf_RegisterForm
    Pf_RegisterForm = Tk()
    Pf_RegisterForm.geometry('1280x720')
    Pf_RegisterForm.resizable(0,0)
    Pf_RegisterForm.title("Admin's Dashboard")
    Pf_RegisterForm.config(bg='white')
    AHframe = Frame(Pf_RegisterForm, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
    AHHeading = Label(Pf_RegisterForm, text='Professor Resister', font=('impact', 18), bg='#3C6739', fg='white').place(
            relx=0.5, rely=0)
    Pf_RegisterForm.Left = ttk.Frame(Pf_RegisterForm, width=300, height=1000, relief="raise")
    Pf_RegisterForm.Left.place(x=2, y=50)
    lbl = Label(Pf_RegisterForm, text="ADD A NEW PROFESSOR", font=("Arial Black", 10, 'bold'), bg='white')
    lbl.place(x=25, y=68)
    global ent_pf_no
    global ent_pf_name
    global ent_pf_code
    global ent_pf_pword
    global ent_pf_sub_flag
    global ent_pf_st_flag

    lbl_reg_no = Label(Pf_RegisterForm, text="Reg_No", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                              y=100)
    lbl_pf_name = Label(Pf_RegisterForm, text="Professor Name", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=135)
    lbl_pf_code = Label(Pf_RegisterForm, text="Login_name", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=170)
    lbl_Pf_pword = Label(Pf_RegisterForm, text="Login_pword", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=205)
    lbl_pf_course_flag = Label(Pf_RegisterForm, text="Course_flag", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=240)
    lbl_pf_st_flag = Label(Pf_RegisterForm, text="Student_flag", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=275)
        
    ent_pf_no = ttk.Entry(Pf_RegisterForm, width=15)
    ent_pf_no.place(x=115, y=100)
    ent_pf_name = ttk.Entry(Pf_RegisterForm, width=15)
    ent_pf_name.place(x=115, y=135)
    ent_pf_code = ttk.Entry(Pf_RegisterForm, width=15)
    ent_pf_code.place(x=115, y=170)
    ent_pf_pword = ttk.Entry(Pf_RegisterForm,width=15)
    ent_pf_pword.place(x=115, y=205)
    ent_pf_sub_flag = ttk.Entry(Pf_RegisterForm, width=15)
    ent_pf_sub_flag.place(x=115, y=240)
    ent_pf_st_flag = ttk.Entry(Pf_RegisterForm, width=15)
    ent_pf_st_flag.place(x=115, y=275)
    
    btn_show = ttk.Button(Pf_RegisterForm, text="LOAD", command=Read_pf, width = 20).place(x = 40,y = 320)
    #btn_show.pack()
    btn_add = ttk.Button(Pf_RegisterForm, text="ADD_New_Professor" ,command=add_book_pf,width = 20).place(x = 40,y = 350)
    #btn_add.pack()
    btn_exit = ttk.Button(Pf_RegisterForm, text="EXIT", command = exit_register_pf,width = 20).place(x = 40,y = 380)
    #btn_exit.pack()
    #goto_TeacherHome
    Pf_RegisterForm.Right = ttk.Frame(Pf_RegisterForm, width=600, height=500, relief="raise")
    Pf_RegisterForm.Right.place(x=250, y=45)
    global tree

    scrollbary = Scrollbar(Pf_RegisterForm.Right, orient=VERTICAL)
    scrollbarx = Scrollbar(Pf_RegisterForm.Right, orient=HORIZONTAL)
    tree = ttk.Treeview(Pf_RegisterForm.Right, columns=(
            "pf_id", "pf_name", "pf_code", "pf_pword", "pf_subject_flag", "pf_student_flag"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('pf_id', text="ID", anchor=W)
    tree.heading('pf_name', text="Professor Name", anchor=W)
    tree.heading('pf_code', text="login_name", anchor=W)
    tree.heading('pf_pword', text="login_pword", anchor=W)
    tree.heading('pf_subject_flag', text="course_flag", anchor=W)
    tree.heading('pf_student_flag', text="student_flag", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)

    tree.pack()
   
    Read_pf()
    AFframe = Frame(Pf_RegisterForm, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)

def Read_pf():
    tree.delete(*tree.get_children())
    Database_pf()
    cursor.execute("SELECT * FROM `professor_admin` ORDER BY `pf_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    cursor.close()
    conn.close()

def add_book_pf():
    if ent_pf_no.get() == "" or ent_pf_name.get() == "" or ent_pf_code.get() == "" or ent_pf_pword.get() == "" or ent_pf_sub_flag.get() == "" or ent_pf_st_flag.get() == "":
        messagebox.showinfo("Requirment!", "Please fill all the fields")
    else:
        Database_pf()

        cursor.execute("INSERT INTO 'professor_admin' (pf_id, pf_name, pf_code, pf_pword, pf_subject_flag,pf_student_flag) VALUES(?, ?, ?, ?, ?, ?)",  (str(ent_pf_no.get()), str(ent_pf_name.get()), str(ent_pf_code.get()), str(ent_pf_pword.get()), str(ent_pf_sub_flag.get()), str(ent_pf_st_flag.get())))
        print("query runnning")
        conn.commit()    

def exit_register_pf():
    Pf_RegisterForm.destroy()
    

def student_register():
    global  st_RegisterForm
    st_RegisterForm = Tk()
    st_RegisterForm.geometry('1280x720')
    st_RegisterForm.resizable(0,0)
    st_RegisterForm.title("Admin's Dashboard")
    st_RegisterForm.config(bg='white')
    AHframe = Frame(st_RegisterForm, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
    AHHeading = Label(st_RegisterForm, text='Student Resister', font=('impact', 18), bg='#3C6739', fg='white').place(
            relx=0.5, rely=0)
    st_RegisterForm.Left = ttk.Frame(st_RegisterForm, width=300, height=1000, relief="raise")
    st_RegisterForm.Left.place(x=2, y=50)
    lbl = Label(st_RegisterForm, text="ADD A NEW STUDENT", font=("Arial Black", 10, 'bold'), bg='white')
    lbl.place(x=25, y=68)
    global ent_st_no
    global ent_st_name
    global ent_st_code
    global ent_st_pword
    global ent_st_sub_flag
    global ent_st_pro_flag

    lbl_reg_no = Label(st_RegisterForm, text="Reg_No", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                              y=100)
    lbl_st_name = Label(st_RegisterForm, text="Student Name", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=135)
    lbl_st_code = Label(st_RegisterForm, text="Login_name", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=170)
    lbl_st_pword = Label(st_RegisterForm, text="Login_pword", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=205)
    lbl_st_subject_flag = Label(st_RegisterForm, text="Course_flag", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=240)
    lbl_st_professor_flag = Label(st_RegisterForm, text="Professor_flag", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=275)
        
    ent_st_no = ttk.Entry(st_RegisterForm, width=15)
    ent_st_no.place(x=115, y=100)
    ent_st_name = ttk.Entry(st_RegisterForm, width=15)
    ent_st_name.place(x=115, y=135)
    ent_st_code = ttk.Entry(st_RegisterForm, width=15)
    ent_st_code.place(x=115, y=170)
    ent_st_pword = ttk.Entry(st_RegisterForm, width=15)
    ent_st_pword.place(x=115, y=205)
    ent_st_sub_flag = ttk.Entry(st_RegisterForm, width=15)
    ent_st_sub_flag.place(x=115, y=240)
    ent_st_pro_flag = ttk.Entry(st_RegisterForm, width=15)
    ent_st_pro_flag.place(x=115, y=275)
    
    btn_show = ttk.Button(st_RegisterForm, text="LOAD", command=Read_st, width = 20).place(x = 40,y = 320)
    #btn_show.pack()
    btn_add = ttk.Button(st_RegisterForm, text="ADD_New_Student" ,command=add_book_st,width = 20).place(x = 40,y = 350)
    #btn_add.pack()
    btn_exit = ttk.Button(st_RegisterForm, text="EXIT", command = exit_register_st,width = 20).place(x = 40,y = 380)
    #btn_exit.pack()
    #goto_TeacherHome
    st_RegisterForm.Right = ttk.Frame(st_RegisterForm, width=600, height=500, relief="raise")
    st_RegisterForm.Right.place(x=250, y=45)
    global tree

    scrollbary = Scrollbar(st_RegisterForm.Right, orient=VERTICAL)
    scrollbarx = Scrollbar(st_RegisterForm.Right, orient=HORIZONTAL)
    tree = ttk.Treeview(st_RegisterForm.Right, columns=(
            "st_id", "st_name", "st_code", "st_pword", "st_subject_flag","st_professor_flag"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('st_id', text="ID", anchor=W)
    tree.heading('st_name', text="Student Name", anchor=W)
    tree.heading('st_code', text="login_name", anchor=W)
    tree.heading('st_pword', text="login_pword", anchor=W)
    tree.heading('st_subject_flag', text="subject_flag", anchor=W)
    tree.heading('st_professor_flag', text="professor_flag", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
            
    tree.pack()
   
    Read_st()
    AFframe = Frame(st_RegisterForm, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)
    st_RegisterForm.mainloop()
def Read_st():
    tree.delete(*tree.get_children())
    Database_st()
    cursor.execute("SELECT * FROM `student_admin` ORDER BY `st_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    cursor.close()
    conn.close()

def add_book_st():
    #print("ID:",ent_st_no.get())
    if ent_st_no.get() == "" or ent_st_name.get() == "" or ent_st_code.get() == "" or ent_st_pword.get() == "" or ent_st_sub_flag.get() == "" or ent_st_pro_flag.get() == "":
        messagebox.showinfo("Requirment!", "Please fill all the fields")
    else:
        Database_st()

        cursor.execute("INSERT INTO 'student_admin' (st_id, st_name, st_code, st_pword, st_subject_flag, st_professor_flag) VALUES(?, ?, ?, ?, ?, ?)",  (str(ent_st_no.get()), str(ent_st_name.get()), str(ent_st_code.get()), str(ent_st_pword.get()), str(ent_st_sub_flag.get()),str(ent_st_pro_flag.get())))
        print("query runnning")
        conn.commit()    

def exit_register_st():
    st_RegisterForm.destroy()

def course_register():
    global  cr_RegisterForm
    cr_RegisterForm = Tk()
    cr_RegisterForm.geometry('1280x720')
    cr_RegisterForm.resizable(0,0)
    cr_RegisterForm.title("Admin's Dashboard")
    cr_RegisterForm.config(bg='white')
    AHframe = Frame(cr_RegisterForm, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
    AHHeading = Label(cr_RegisterForm, text='Course Resister', font=('impact', 18), bg='#3C6739', fg='white').place(
            relx=0.5, rely=0)
    cr_RegisterForm.Left = ttk.Frame(cr_RegisterForm, width=300, height=1000, relief="raise")
    cr_RegisterForm.Left.place(x=2, y=50)
    lbl = Label(cr_RegisterForm, text="ADD A NEW Course", font=("Arial Black", 10, 'bold'), bg='white')
    lbl.place(x=25, y=68)
    global ent_cr_no
    global ent_cr_1
    global ent_cr_2
    global ent_cr_3
    global ent_cr_4
    global ent_cr_5

    lbl_reg_no = Label(cr_RegisterForm, text="Course_No", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                              y=100)
    lbl_cr_1 = Label(cr_RegisterForm, text="Subject_1", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=135)
    lbl_cr_2 = Label(cr_RegisterForm, text="Subject_2", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=170)
    lbl_cr_3 = Label(cr_RegisterForm, text="Subject_3", font=("Helvetica", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=205)
    lbl_cr_4 = Label(cr_RegisterForm, text="Subject_4", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=240)
    lbl_cr_5 = Label(cr_RegisterForm, text="Subject_5", font=("Helvetica", 8, 'bold'), bg='white').place(x=16, y=275)
        
    ent_cr_no = ttk.Entry(cr_RegisterForm, width=15)
    ent_cr_no.place(x=115, y=100)
    ent_cr_1 = ttk.Entry(cr_RegisterForm, width=15)
    ent_cr_1.place(x=115, y=135)
    ent_cr_2 = ttk.Entry(cr_RegisterForm, width=15)
    ent_cr_2.place(x=115, y=170)
    ent_cr_3 = ttk.Entry(cr_RegisterForm, width=15)
    ent_cr_3.place(x=115, y=205)
    ent_cr_4 = ttk.Entry(cr_RegisterForm, width=15)
    ent_cr_4.place(x=115, y=240)
    ent_cr_5 = ttk.Entry(cr_RegisterForm, width=15)
    ent_cr_5.place(x=115, y=275)
    
    btn_show = ttk.Button(cr_RegisterForm, text="LOAD", command=Read_cr, width = 20).place(x = 40,y = 320)
    #btn_show.pack()
    btn_add = ttk.Button(cr_RegisterForm, text="ADD_New_Course" ,command=add_book_cr,width = 20).place(x = 40,y = 350)
    #btn_add.pack()
    btn_exit = ttk.Button(cr_RegisterForm, text="EXIT", command = exit_register_cr,width = 20).place(x = 40,y = 380)
    #btn_exit.pack()
    #goto_TeacherHome
    cr_RegisterForm.Right = ttk.Frame(cr_RegisterForm, width=600, height=500, relief="raise")
    cr_RegisterForm.Right.place(x=250, y=45)
    global tree

    scrollbary = Scrollbar(cr_RegisterForm.Right, orient=VERTICAL)
    scrollbarx = Scrollbar(cr_RegisterForm.Right, orient=HORIZONTAL)
    tree = ttk.Treeview(cr_RegisterForm.Right, columns=(
            "Course_No", "Subject_1", "Subject_2", "Subject_3", "Subject_4","Subject_5"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Course_No', text="Course_No", anchor=W)
    tree.heading('Subject_1', text="Subject_1", anchor=W)
    tree.heading('Subject_2', text="Subject_2", anchor=W)
    tree.heading('Subject_3', text="Subject_3", anchor=W)
    tree.heading('Subject_4', text="Subject_4", anchor=W)
    tree.heading('Subject_5', text="Subject_5", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
            
    tree.pack()
   
    Read_cr()
    AFframe = Frame(cr_RegisterForm, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)
    cr_RegisterForm.mainloop()
def Read_cr():
    tree.delete(*tree.get_children())
    Database_cr()
    cursor.execute("SELECT * FROM `course_admin` ORDER BY `Course_No` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    cursor.close()
    conn.close()

def add_book_cr():
    #print("ID:",ent_st_no.get())
    if ent_cr_no.get() == "" or ent_cr_1.get() == "" or ent_cr_2.get() == "" or ent_cr_3.get() == "" or ent_cr_4.get() == "" or ent_cr_5.get() == "":
        messagebox.showinfo("Requirment!", "Please fill all the fields")
    else:
        Database_cr()

        cursor.execute("INSERT INTO 'course_admin' (Course_No, Subject_1, Subject_2, Subject_3, Subject_4, Subject_5) VALUES(?, ?, ?, ?, ?, ?)",  (str(ent_cr_no.get()), str(ent_cr_1.get()), str(ent_cr_2.get()), str(ent_cr_3.get()), str(ent_cr_4.get()),str(ent_cr_5.get())))
        print("query runnning")
        conn.commit()    

def exit_register_cr():
    cr_RegisterForm.destroy()


def goto_AdminHome():
    global  AdminRegisterForm
    AdminRegisterForm = Tk()
    AdminRegisterForm.geometry('1280x720')
    AdminRegisterForm.resizable(0,0)
    AdminRegisterForm.title("Admin's Dashboard")
    AdminRegisterForm.config(bg='white')
    AHframe = Frame(AdminRegisterForm, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)
    LAdminTitle = Label(AdminRegisterForm, font=('impact', 30, 'bold'), text="Administrator's Home", bg='white').place(relx=0.4,
                                                                                                               y=150)
    B_ProfessorReg = Button(AdminRegisterForm, text='New Professor Register', width=25, height=13, bg='#3C6739', fg='white',
                                      font=('arial black', 10), bd=6,command = professor_register).place(x=120, rely=0.4)
    B_CourseReg = Button(AdminRegisterForm, text='New Course Register', width=25, height=13, bg='#3C6739', fg='white',
                                   font=('arial black', 10), bd=6,command = course_register).place(x=520, rely=0.4)
    B_StudentReg = Button(AdminRegisterForm, text='New Student Register', width=25, height=13, bg='#3C6739', fg='white',
                                       font=('arial black', 10), bd=6,command = student_register).place(x=930, rely=0.4)
    AFframe = Frame(AdminRegisterForm, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)



#goto_AdminHome()
#professor_register()
#student_register()
#