import sqlite3

conn=sqlite3.connect('test.db')
print("Opened database sucessfully");

conn.execute("INSERT INTO STUDENT1 (ID,NAME,AGE,ADDRESS,SALARY) \
			 VALUES(11,'PAUL',32,'CALIFORNIA',20000.00)");

conn.execute("INSERT INTO STUDENT1 (ID,NAME,AGE,ADDRESS,SALARY) \
			 VALUES(12,'ALLEN',25,'TEXAS',15000.00)");

conn.commit()
print("Recordes Created Successfully");
conn.close()