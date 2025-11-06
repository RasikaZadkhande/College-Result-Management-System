import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS course( cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT UNIQUE,duration TEXT,charges TEXT,description TEXT) """)
    con.commit() 


    cur.execute("""CREATE TABLE IF NOT EXISTS student( roll INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,dob TEXT,contact TEXT,admission TEXT,course TEXT,state TEXT,city TEXT,pin TEXT,address TEXT) """)
    con.commit()  

    cur.execute("""CREATE TABLE IF NOT EXISTS result( rid INTEGER PRIMARY KEY AUTOINCREMENT,roll TEXT UNIQUE,name TEXT,course TEXT,marks_ob TEXT,full_marks TEXT,per TEXT) """)
    con.commit() 

    cur.execute("ALTER TABLE employee2 ADD COLUMN email TEXT;")
    cur.execute("""CREATE TABLE IF NOT EXISTS employee2( eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name TEXT,l_name TEXT,contact TEXT,email TEXT,question TEXT,answer TEXT,password TEXT) """)
    con.commit() 


    

    con.close()
    print("✅ Database and table created successfully!")





create_db()
