import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
        id Integer Primary Key,
        name text,
        age text, 
        doj text,
        gender text,
        contact text,
        address text
        )
        """
        self.con.execute(sql)
        self.con.commit()

    def insert(self, name, age, doj, gender, contact, address, get):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?)",
                         (name, age, doj, gender, contact, address))
        self.con.commit()
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows
    def delete(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()
    def update(self,id, name, age, doj, gender, contact, address):
        self.cur.execute("update employees set name=?, age=?, doj=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, gender, contact, address,id))
        self.con.commit()



o=Database("employees.db")
#o.insert("anupriya", "21", "14-07-2023", "female", "5679804123", "main road,Salem")
o.fetch()
#o.delete("3")
o.update("2","samkannan","30","10-6-2022","male", "1234567897", "madurai")

