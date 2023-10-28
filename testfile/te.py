import sqlite3

class student:
    age=17
    grade=11
    school="A"

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"student(name='{self.name}')"
    
    def __repr__(self):
        return f"student(name='{self.name}' , age='{self.age}')"

    def introduction(self):
        return f"name:{self.name} age:{self.age} grade:{self.grade}"

    def save(self):
        conn = sqlite3.connect('testfile/db.sqlite3')
        conn.execute(f"INSERT INTO student(name,age,grade,school) \
        VALUES ('{self.name}','{self.age}', '{self.grade}' , '{self.school}' )")

        conn.commit()
        conn.close()

    @classmethod
    def filter(cls,**kwargs):
        where_clause = [f"{key}='{value}' " for key, value in kwargs.items()]
        where = " and ".join(where_clause)
        print(where)
        conn = sqlite3.connect('testfile/db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(
            f"select id,name , age from student where {where};"
        )
        results = cursor.fetchall()
        output = []
        for result in results:
            p = cls(result[1])#,results[2])
            p.id = result[0]
            output.append(p)

        conn.commit()
        conn.close()
        return output

s1 = student("ali")
s2 =student("ali2")
# s2.save()
# print(s1.introduction())
# s1.save()

p2 = s2.filter(age=17)

print(p2)


