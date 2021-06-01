from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import pymysql

def main():
    root = Tk()
    app = window1(root)
    root.mainloop()

def main2():
    root = Tk()
    ob= Student(root)
    root.mainloop()

class window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Login")
        self.master.geometry('750x550+0+0')
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master,bg="powder blue")
        self.frame.pack() 

        # variable
        self.username = StringVar()
        self.password = StringVar()

       
        self.lblTitle = Label(self.frame, text='Login', font=('arial',50,'bold'),bg='powder blue',fg='black')
        self.lblTitle.grid(row=0,column='0',columnspan=2, pady=40)

         #frame
        self.loginframe1 = LabelFrame(self.frame, width=1350,height=600,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe1.grid(row=1,column=0)

        self.loginframe2 = LabelFrame(self.frame, width=1350,height=600,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.loginframe2.grid(row=2,column=0)

        #Label and Entry
        self.lblUsename= Label(self.loginframe1, text='UserName:',font=('arial',20,'bold'),bd=22,bg='cadet blue',fg='cornsilk')
        self.lblUsename.grid(row=0,column=0)
        self.textUsename=Entry(self.loginframe1,font=('arial',20,'bold'),textvariable=self.username)
        self.textUsename.grid(row=0,column=1)

        self.lblPassword= Label(self.loginframe1, text='Password:',font=('arial',20,'bold'),bd=22,bg='cadet blue',fg='cornsilk')
        self.lblPassword.grid(row=1,column=0)
        self.textPassword=Entry(self.loginframe1,font=('arial',20,'bold'), show='*',textvariable=self.password)
        self.textPassword.grid(row=1,column=1)

        #button
        self.btnlogin = Button(self.loginframe2, text='Login',width=17,font=('arial',10,'bold'), command = self.login_system)
        self.btnlogin.grid(row=3,column=0,pady=20, padx=8)

        self.btnreset = Button(self.loginframe2, text='Reset',width=17,font=('arial',10,'bold'), command = self.reset)
        self.btnreset.grid(row=3,column=1,pady=20, padx=8)

        self.btnexit = Button(self.loginframe2, text='Exit',width=17,font=('arial',10,'bold'),command =self.iExit)
        self.btnexit.grid(row=3,column=2,pady=20, padx=8)
    
    #login system
    def login_system(self):
        u=(self.username.get())
        p=(self.password.get())

        if(u==str(123456789) and p==str(987654321)):
            self.newWindow = Toplevel(self.master)
            self.app = window2(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Login Systemd", "Too bad, invalid login detail")
            self.username.set("")
            self.password.set("")
            self.textUsename.focus()
    
    #reset
    def reset(self):
        self.username.set("")
        self.password.set("")
        self.textUsename.focus()

    #exit
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login Systemd","Confirm if you want to exit")
        if self.iExit>0:
            self.master.destroy()
        else:
            command =self.new_window
            return

#main window

class window2:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Managment System")
        self.root.geometry("1350x760+0+0")


        # All variables
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_text=StringVar()



        title = Label(self.root, text="Student Managment System",bd=10,relief=GROOVE, font=("times new roman",40,"bold"), bg="powder blue", fg="#000")
        title.pack(side=TOP, fill=X)
        
        # manage frame
        manag_frame = Frame(self.root, bd=4, relief=RIDGE,bg="powder blue")
        manag_frame.place(x=20,y=100,width=450, height=650)
        
        m_title=Label(manag_frame, text="Manage Student", font=("times new roman",30,"bold"),bg="powder blue", fg="#000")
        m_title.grid(row=0,columnspan=2,pady=20)
        
      
        #label details
        lbl_frame_roll = Label(manag_frame, text="Roll No:", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_frame_roll.grid(row=1,column=0,pady=10,padx=20, sticky="w")
        
        lbl_txt_roll =Entry(manag_frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        lbl_txt_roll.grid(row=1,column=1,pady=10,padx=20, sticky="w")

        lbl_frame_name = Label(manag_frame, text="Name:", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_frame_name.grid(row=2,column=0,pady=10,padx=20, sticky="w")
        
        txt_name =Entry(manag_frame,textvariable=self.name_var,font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20, sticky="w")

        lbl_frame_email = Label(manag_frame, text="Email:", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_frame_email.grid(row=3,column=0,pady=10,padx=20, sticky="w")
        
        txt_email =Entry(manag_frame,textvariable=self.email_var,font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20, sticky="w")

        lbl_gender = Label(manag_frame, text="Gender:", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20, sticky="w")
        
        combo_gender=ttk.Combobox(manag_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"), state="readonly")
        combo_gender["values"] = ("Male","Female", "Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20, sticky="w")

        lbl_contact = Label(manag_frame, text="Contact:", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20, sticky="w")
        
        txt_contact =Entry(manag_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20, sticky="w")

        lbl_dob = Label(manag_frame, text="D.O.B:", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20, sticky="w")
        
        txt_dob =Entry(manag_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20, sticky="w")

        lbl_address = Label(manag_frame, text="Address:", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_address.grid(row=7,column=0,pady=10,padx=20, sticky="w")

        self.txt_address =Text(manag_frame,font=("times new roman",15,"bold"), bd=5, relief=GROOVE, width=20,height=4)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20, sticky="w")

        # button frame
        btn_frame=Frame(manag_frame,bd=4,relief=RIDGE, bg="cadet blue") 
        btn_frame.place(x=15,y=560,width=410)
        addbtn= Button(btn_frame,text="Add",width=10, command=self.add_students).grid(row=0,padx=10,pady=10)
        updatebtn= Button(btn_frame,command=self.update_data,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn= Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn= Button(btn_frame,command=self.clear,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)

  # dtails frame
        detail_frame = Frame(self.root, bd=4, relief=RIDGE,bg="powder blue")
        detail_frame.place(x=500,y=100,width=800, height=650)

        lbl_search = Label(detail_frame, text="Search By", font=("times new roman",20,"bold"),bg="powder blue", fg="#000")
        lbl_search.grid(row=0,column=0,pady=10,padx=20, sticky="w")

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"), state="readonly")
        combo_search["values"] = ("Roll_no","Name", "Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20, sticky="w")

        txt_search =Entry(detail_frame,textvariable=self.search_text,width=15,font=("times new roman",10,"bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20, sticky="w")

        searchbtn= Button(detail_frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn= Button(detail_frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        # table frame
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE,bg="powder blue")
        table_frame.place(x=16,y=70,width=760, height=500)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
    
    def add_students(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("error", "All fields are required!")
        else:
            con=pymysql.connect(host="localhost",user="root", password="", database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.roll_no_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END )
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success", "Record has been inserted")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
    
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END ),
                                                                        self.roll_no_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%' ")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


 


if __name__ == '__main__':
    main()

if __name__ == '__main2__':
    main2()


