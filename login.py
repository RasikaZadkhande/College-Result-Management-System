from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
#import pymysql #pip install pymysql
from tkinter import messagebox,ttk
import sqlite3
import os

class login():
    def __init__(self,root):
         self.root=root
         self.root.title("Login System")
         self.root.geometry("1350x700+0+0")
         self.root.config(bg="#021e2f")
         
         #==========BackgroundColours============
         left_lbl=Label(self.root,bg="#08A3D2",bd=0)
         left_lbl.place(x=0,y=0,relheight=1,width=600)

         right_lbl=Label(self.root,bg="#031F3C",bd=0)
         right_lbl.place(x=600,y=0,relheight=1,width=1)
         #=================Frames=========
         login_frame=Frame(self.root,bg="white")
         login_frame.place(x=250,y=100,height=500,width=800)

         title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

         email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
         self.text_email=Entry(login_frame,font=("times new roman",18),bg="lightgray")
         self.text_email.place(x=250,y=180,width=350,height=35)

         pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
         self.text_pass_=Entry(login_frame,font=("times new roman",18),bg="lightgray")
         self.text_pass_.place(x=250,y=280,width=350,height=35)



         btn_reg=Button(login_frame,text="Register new Account?",command=self.register_window,font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=245,y=320)
         btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_password_window,font=("times new roman",14),bg="white",bd=0,fg="red",cursor="hand2").place(x=450,y=320)

         btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=245,y=380,width=180,height=40)







         #===========Clock===============
         self.lbl=Label(self.root,text="Results change,Enduring Effort📊✨",font=("Book Antiqua",15,"bold"),compound=BOTTOM,fg="white",bg="#4F8394",bd=0)
         self.lbl.place(x=90,y=120,height=450,width=350)

         self.working()

    def reset(self):
         self.cmb_quest.current(0)
         self.text_pass_.delete(0,END)
         self.txt_answer.delete(0,END)
         self.text_pass_.delete(0,END)
         self.text_email.delete(0,END)

    def forget_password(self):
         if self.text_email.get() == "Select" or self.cmb_quest.get() == "" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":           
            messagebox.showerror("Errpr","All fields are required ",parent=self.root2)
         else:
              try:
                     con=sqlite3.connect(database="rms.db")
                     cur=con.cursor()
                     cur.execute("select * from employee2 where email=? and question=? and answer=?",(self.text_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                     row=cur.fetchone()
                     if row==None:
                        messagebox.showerror("Error","Please Select the correct Security Question / Enter Answer",parent=self.root2)
                     
                     else:
                        cur.execute("update employee2 set password=? where email=? and question=? and answer=? ",(self.txt_new_password.get(),self.text_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                        con.commit()
                        con.close()                      
                        messagebox.showinfo("Success","your passwoerd has been reset, Please login with new password",parent=self.root2)
                        self.reset()
                        self.root2.destroy()

                     

              except Exception as es: 
                     messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
             
    
              
    



    def forget_password_window(self):
         if self.text_email.get()=="":
              messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
         else:
               try:
                  
                  con=sqlite3.connect(database="rms.db")
                  cur=con.cursor()
                  cur.execute("select * from employee2 where email=? ",(self.text_email.get(),))
                  row=cur.fetchone()
                  if row==None:
                      messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                     
                  else:
                       
                       con.close()
                       self.root2=Toplevel()
                       self.root2.title("Forget Password")
                       self.root2.geometry("350x400+495+150")
                       self.root2.config(bg="white")
                       self.root2.focus_force()
                       self.root2.grab_set()

                       t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
         

         #======================Forget Password============
                       question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                       self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                       self.cmb_quest['value']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                       self.cmb_quest.place(x=50,y=130,width=250)
                       self.cmb_quest.current(0)

                       answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                       self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                       self.txt_answer.place(x=50,y=210,width=250)

                       new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                       self.txt_new_password=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                       self.txt_new_password.place(x=50,y=290,width=250)


                       btn_change_password=Button(self.root2,text="Rest Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
   
               except Exception as es:
                  messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
             
              
             
         
              


    def register_window(self):
         self.root.destroy()
         import register


    def login(self):
         if self.text_email.get()=="" or self.text_pass_.get()=="":
              messagebox.showerror("Error","All Fields are required",parent=self.root)
         else:
             try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee2 where email=? and password=?",(self.text_email.get(),self.text_pass_.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                     
                else:
                     messagebox.showinfo("Success",f"Welcome: {self.text_email.get()}",parent=self.root)
                     self.root.destroy()
                     os.system("python dashbord.py")
                con.close()
             except Exception as es:
                  messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
             
               





    def clock_image(self,hr,min_,sec_):
         clock=Image.new("RGB",(400,400),(8,25,35))
         draw=ImageDraw.Draw(clock)
         #====Clock Image========
         bg=Image.open("loginsystem/images/cb.png")
         bg=bg.resize((300,300),Image.Resampling.LANCZOS)
         clock.paste(bg,(50,50))
         origin=200,200
         
         draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
         draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
         draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
         draw.ellipse((195,195,210,210),fill="#1AD5D5")
         clock.save("loginsystem/images/clock_new.png")
    
    def working(self):
        try:
                           
              h=datetime.now().time().hour
              m=datetime.now().time().minute
              s=datetime.now().time().second
              hr=(h/12)*30+(m/2)
              min_=(m/60)*360
              sec_=(s/60)*360
              self.clock_image(hr,min_,sec_)
              self.img=ImageTk.PhotoImage(file="loginsystem/images/clock_new.png")
              self.lbl.config(image=self.img)
              self.lbl.after(1000, self.working)
          
        except:
              pass
         
         
root=Tk()
obj=login(root)
root.mainloop()