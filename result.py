from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======title======
        title=Label(self.root,text="Add Student Results",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)
 


        #==================labels(widges)=============
        #==================variables==============
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()




        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=100)
        lbl_name=Label(self.root,text="Nmae",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=160)        
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=220)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",15,"bold"),bg='white').place(x=50,y=340)
        

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text='Search',font=("goudy old style ",15,"bold"),bg="#03A9F4",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=120,height=28)


        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg='lightyellow',state='readonly').place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg='lightyellow',state='readonly').place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",20,"bold"),bg='lightyellow').place(x=280,y=280,width=320)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20,"bold"),bg='lightyellow').place(x=280,y=340,width=320)
       
        #===========button========================
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)


         #=======image====
        self.pic4_img = Image.open("images/pic4.png")
        self.pic4_img = self.pic4_img.resize((450,300), Image.LANCZOS)
        self.pic4_img = ImageTk.PhotoImage(self.pic4_img)

        # Move image more to the RIGHT
        self.lbl_pic4 = Label(self.root, image=self.pic4_img,bg="white")
        self.lbl_pic4.place(x=630, y=100, width=500, height=290)

#=====================================================================
    def fetch_roll(self):
        con= con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
           
            cur.execute("select roll from student" )
            rows=cur.fetchall()
    
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:  
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
       


        #===========search function ======
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "Select":
                messagebox.showerror("Error", "Please select a roll number", parent=self.root)
            else:
                cur.execute("SELECT name, course FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_name.set(row[0])
                    self.var_course.set(row[1])
                else:
                    messagebox.showinfo("Not Found", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    #addfunction======
    def add(self):
        con= con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","please first search student record",parent=self.root) 
            else:
                # 1. डेटाबेसमध्ये हा निकाल आधीच आहे का ते तपासा
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                # 2. लॉजिक
                if row != None:
                    messagebox.showerror("Error","Result already exists for this Student and Course",parent=self.root)
                else:
                    per = (int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(round(per, 2))
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
       




       





    def clear(self): 
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),          
    





       







    # ========================= RUN APP =========================
if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()    