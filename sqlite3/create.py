import sqlite3

conn=sqlite3.connect('test.db')
print("Opened database sucessfully");

conn.execute('''CREATE TABLE STUDENT1
		(ID INT PRIMARY KEY	NOT NULL,
		NAME			TEXT NOT NULL,
		AGE			INT	NOT NULL,
		ADDRESS		CHAR(50),
		SALARY		REAL);''')
print("Table created successfully");

conn.close()