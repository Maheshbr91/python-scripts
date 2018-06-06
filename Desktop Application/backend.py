import sqlite3

def connect():
    d1=sqlite3.connect("sample.db")
    cur=d1.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS samplebook(ID Integer Primary Key,Title text,Author text,Year integer,ISBN text)")
    d1.commit()
    d1.close()

def insert(title,author,year,isbn):
    d1=sqlite3.connect("sample.db")
    cur=d1.cursor()
    cur.execute("INSERT INTO samplebook VALUES(Null,?,?,?,?)",(title,author,year,isbn))
    d1.commit()
    d1.close()

def view():
    d1=sqlite3.connect("sample.db")
    cur=d1.cursor()
    cur.execute("SELECT * FROM samplebook")
    row=cur.fetchall()
    d1.commit()
    d1.close()
    return row

def search(title="",author="",year="",isbn=""):
    d1=sqlite3.connect("sample.db")
    cur=d1.cursor()
    cur.execute("SELECT * FROM samplebook WHERE Title=? OR Author=? OR Year=? OR Isbn=?",(title,author,year,isbn))
    row=cur.fetchall()
    d1.commit()
    d1.close()
    return row

def delete(id):
    d1=sqlite3.connect("sample.db")	
    cur=d1.cursor()
    cur.exetute("DELETE FROM samplebook WHERE ID=?",(id,))
    d1.commit()
    d1.close()

def update(id,title,author,year,isbn):
    d1=sqlite3.connect("sample.db")
    cur=d1.cursor()
    cur.execute("UPDATE samplebook SET Title=?,Author=?,year=?,Isbn=? WHERE id=?",(title,author,year,isbn,id))
    d1.commit()
    d1.close()


connect()
insert("sample","mahesh",1991,"11344dsa")
print(view())
print(search(author="mahesh"))
    
