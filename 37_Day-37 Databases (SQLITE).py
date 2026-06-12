"""
Day 37: Intro to Databases (SQLite)
File: day37_database.py
"""
import sqlite3

def manage_database():
    # 1. Connect to a database file (creates it automatically if missing)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 2. Create a clean data table structure
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade TEXT NOT NULL
        )
    """)
    
    # 3. Insert a fresh record into the table
    cursor.execute("INSERT INTO students (name, grade) VALUES ('Alice', 'A')")
    conn.commit() # Save changes permanently to the file
    
    # 4. Read data from the table
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()
    
    print("-" * 40)
    print("DATABASE RECORDS:")
    print("-" * 40)
    for student in all_students:
        # student[0] is ID, student[1] is Name, student[2] is Grade
        print(f"ID: {student[0]} | Name: {student[1]} | Grade: {student[2]}")
    print("-" * 40)
    
    # 5. Close connection
    conn.close()

if __name__ == "__main__":
    manage_database()
    
    print("\nExecution finished.")
    input("Press the ENTER key to close this window...")
