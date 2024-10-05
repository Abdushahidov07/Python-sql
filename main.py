from typing import Any
from conection import conn

cur = conn.cursor()

cur.execute("""
            create table if not exists Students(
            id serial primary key,
            f_name varchar(100),
            l_name varchar(100),
            age int,
            phone varchar(100),
            email varchar(100)
            )
""")


class Students:
    def __init__(self, f_name, l_name, age, phone, email):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.phone = phone   
        self.email = email

    def __str__(self) -> str:
        return self.f_name, self.l_name, self.age

class StudentManeger:
    def add_students(self):
        add_st = Students(
            input("f name: "),
            input("l name: "),
            int(input("Age: ")),
            input("Phone: "),
            input("Email: ")
        )
        st = (add_st.f_name, add_st.l_name, add_st.age, add_st.phone, add_st.email)
        cur.execute("insert into Students(f_name, l_name, age, phone, email) values(%s,%s,%s,%s,%s)",st)
        conn.commit()
        cur.close()
    def show_st_by_id(self, id):
        cur = conn.cursor()
        cur.execute("select * from Students where id = %s",(id,))
        print(cur.fetchall())
        conn.commit()
        cur.close()
    def show_st(self):
        cur = conn.cursor()
        cur.execute("select * from Students")
        print(cur.fetchall())
        conn.commit()
        cur.close()
    def update(self, id, nf_name, nl_name, nage, nphone, nemail):
        cur = conn.cursor()
        cur.execute("update Students set f_name = %s, l_name=%s, age = %s, phone=%s, email=%s where id = %s", (nf_name, nl_name, nage, nphone, nemail, id,))
        conn.commit()
        cur.close()
    def delete(self, id):
        cur = conn.cursor()
        cur.execute("delete from Students where id = %s",(id, ))
        conn.commit()
        cur.close()

st_mng = StudentManeger()

while True:
    user_input = int(input("1.add 2.show 3.show all 4.update 5.delete 6.exit"))
    if user_input == 1:
        st_mng.add_students()
    elif user_input == 2:
        st_mng.show_st_by_id(int(input("ID:")))
    elif user_input == 3:
        st_mng.show_st()
    elif user_input == 4:
        st_mng.update(int(input("ID:")), input("new fname: "),input("new lname: "),int(input("new age: ")), input("new phone: "),input("new email: "))
    elif user_input == 5:
        st_mng.delete(int(input("ID:")))
    elif user_input == 6:
        print("Exit")
        break
conn.commit()
cur.close()
conn.close()