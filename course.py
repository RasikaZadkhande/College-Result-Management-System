from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======title======
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=40)
        #=======variables====
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_courseid = StringVar()
    


        #======widgets=====
        
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg='white').place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg='white').place(x=10,y=100)        
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg='white').place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg='white').place(x=10,y=180)
        lbl_courseid = Label(self.root, text="Course ID", font=("goudy old style", 15, "bold"), bg='white')
        lbl_courseid.place(x=10, y=350)


        #=========Entry Fields =====
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg='lightyellow')
        self.txt_courseName.place(x=150,y=60,width=200)

        self.txt_courseid = Entry(self.root, textvariable=self.var_courseid, font=("goudy old style", 15, "bold"),
                          bg='lightgray')
        self.txt_courseid.place(x=150, y=350, width=200)

        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=150,y=100,width=200)        
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg='lightyellow')
        self.txt_description.place(x=150,y=180,width=500,height=130)
        
        #====buttons======
        self.btn_add=Button(self.root,text='Save',font=("goudy old style ",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40) 
        self.btn_update=Button(self.root,text='Update',font=("goudy old style ",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40) 
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style ",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)            
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style ",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40) 
    
        #====search pannel  =========
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg='white').place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style ",15,"bold"),bg="#03A9F4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28) 

        #=====content==============
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)



        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Descriptrion")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#=============================data function====================================================================
    def clear(self):
        self.show() 
        self.var_course.set("")
        self.var_courseid.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)
    
    
    #====delete function=====
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root) 
            else:
                cur.execute("delete from course where cid=?", (self.var_courseid.get(),))
                con.commit()
                messagebox.showinfo("Delete", "Course deleted Successfully", parent=self.root)
                self.show()
                self.clear()
                row=con.commit()
                if row==None:
                     messagebox.showerror("Error","please select course from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully",parent=self.root)
                        self.clear()
                        

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
        finally:
           con.close()


    
    
    
    
    def get_data(self,ev):
     
     self.txt_courseName.config(state='readonly')
     self.txt_courseid.config(state=NORMAL)
     self.txt_courseName 
     r=self.CourseTable.focus() 
     content=self.CourseTable.item(r)
     row=content["values"]
      #print(row) 
     if row:
        
        self.var_courseid.set(row[0])      # Course ID
        self.var_course.set(row[1])        # Name
        self.var_duration.set(row[2])      # Duration
        self.var_charges.set(row[3])       # Charges

        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])

    
     
   #=========add function========


    def add(self):
        con= con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root) 
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","Course Name should be exists",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description)values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ) ) 
                    con.commit()   
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
        finally:
          con.close()

       #==============update===========
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where cid=?", (self.var_courseid.get(),))
                row = cur.fetchone()

                if row is None:
                    op = messagebox.askyesno("Not Found", "This Course ID not found. Do you want to add as new?", parent=self.root)
                    if op:
                       cur.execute("insert into course (cid, name, duration, charges, description) values(?,?,?,?,?)", (
                           self.var_courseid.get(),
                           self.var_course.get(),
                           self.var_duration.get(),
                           self.var_charges.get(),
                           self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Added", "New Course Added Successfully", parent=self.root)
                    self.show()
                else:
                    cur.execute("""update course set 
                        name=?, duration=?, charges=?, description=? 
                        where cid=?""", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_courseid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
                    self.show()
                    self.clear()
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()




      
       
       
       
       
       
       
       
       
       
       
       
        #===========show function ===========
    def show(self):
        con= con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
           
            cur.execute("select * from course" )
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:  
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
        finally:
         con.close()

       
    #===========search function ======
    def search(self):
        con= con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            # chat gpt
            search_text = self.var_search.get()   # <-- हे बरोबर आहे, वर define केलेले पाहिजे
        
            if search_text == "":
                 messagebox.showerror("Error", "Please enter course name to search", parent=self.root)
            #=====chatgpt
            else:
                cur.execute("select * from course where name LIKE ?",('%' + search_text + '%',),) 
                rows=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)

        except Exception as ex:  
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        finally:
         con.close()
 
       
       
       
       
       
       
        








# ========================= RUN APP =========================
if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()