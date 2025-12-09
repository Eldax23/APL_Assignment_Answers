# problem 1
import pymysql
connect = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="school"
)
cursor = connect.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    Student_id INT AUTO_INCREMENT PRIMARY KEY,
    grade FLOAT,
    name VARCHAR(250)
)
""")
students = [("Hamza", 20.0),("Osama", 15.0),("Khaled", 13.0)]
cursor.executemany("INSERT INTO students (name, grade) VALUES (%s, %s)", students)
connect.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
connect.close()



# --------------------------------------------------------------
# problem 2

grade = int(input("enter grade: "))
name = input("enter name: ")
cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",(name, grade))
connect.commit()
cursor.execute("SELECT * FROM students")


for row in cursor.fetchall():
    print(row)


# --------------------------------------------------------------
# problem 3

try:
    connect.start_transaction()
    cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",("Abdo", 20))
    cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",("Adel", 33))
    connect.commit()

except Exception as e:
    print("error:", e)
    connect.rollback()
    print("transaction failed")

cursor.execute("SELECT * FROM students")


for row in cursor.fetchall():
    print(row)

cursor.close()
connect.close()


#------------------------------------------------
# problem 4
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    grade = Column(Float)
    def __repr__(self):
        return f"<student_id: (id={self.id}, with name='{self.name}', and grade={self.grade})>"
engine = create_engine("mysql+mysqlconnector://root:your_password@localhost/school")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
student1 = Student(name="ALI", grade=30.5)
student2 = Student(name="Sama", grade=12.2)
session.add_all([student1, student2])
session.commit()
students = session.query(Student).all()
for s in students:
    print(s)
