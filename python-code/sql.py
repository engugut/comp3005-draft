import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        port="5432")

cursor = conn.cursor()

def getAllStudents():
    cursor.execute("SELECT * FROM students")

    print(cursor.fetchall())
    
    
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute('''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s,%s,%s,%s)''', (first_name,last_name,email,enrollment_date))
    conn.commit()
    #print(cursor.fetchall())

def updateStudentEmail(student_id, new_email):
    cursor.execute(""" UPDATE students SET email = %s WHERE student_id = %s""", (new_email,student_id))
    conn.commit()
    #print(cursor.fetchall())

def deleteStudent(student_id):
	cursor.execute('DELETE FROM students WHERE student_id = %s', (student_id))
	conn.commit()
	#print(cursor.fetchall())

if __name__ == '__main__':
	#getAllStudents()
	#updateStudentEmail("2", "jane.human@earth.com")
	#addStudent("Bob", "Morbly" , "bobbybob@bob.xyz", "2023-03-19")
	#deleteStudent("2")
	


