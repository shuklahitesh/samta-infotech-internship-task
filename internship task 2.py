# -*- coding: utf-8 -*-
"""
 TASK 2 : MySQL Database Operations with Python 

Your task is to write a Python program that accomplishes the following:
First create a database , table and add these column ‘student_id’, ‘first_name’, ‘last_name’,
‘age’, ‘grade’.
Connects to your MySQL database with python.
Inserts a new student record into the "students" table with the following details:
First Name: "Alice"
Last Name: "Smith"
Age: 18
Grade: 95.5
Updates the grade of the student with the first name "Alice" to 97.0.
Deletes the student with the last name "Smith."
Fetches and displays all student records from the "students" table.
@author: hitess=h shukla
"""

import mysql.connector

# Function to create a new database and connect to it
def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="user",
        password="user"
    )

    cursor = connection.cursor()

    # Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    cursor.execute("USE school")

    # Create the "students" table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            grade FLOAT
        )
    """)

    connection.commit()
    connection.close()

# Function to connect to the MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="user",
        password="user",
        database="school"
    )

# Function to insert a new student record
def insert_student_record(connection, first_name, last_name, age, grade):
    cursor = connection.cursor()

    # Insert new student record
    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, age, grade))

    connection.commit()

# Function to update the grade of a student
def update_student_grade(connection, first_name, new_grade):
    cursor = connection.cursor()

    # Update student grade
    cursor.execute("""
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
    """, (new_grade, first_name))

    connection.commit()

# Function to delete a student by last name
def delete_student_by_last_name(connection, last_name):
    cursor = connection.cursor()

    # Delete student by last name
    cursor.execute("""
        DELETE FROM students
        WHERE last_name = %s
    """, (last_name,))

    connection.commit()

# Function to fetch and display all student records
def fetch_and_display_students(connection):
    cursor = connection.cursor()

    # Fetch all student records
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # Display student records
    for student in students:
        print(student)

    connection.close()

# Main program
create_database()

# Connect to the database
db_connection = connect_to_database()

# Insert a new student record
insert_student_record(db_connection, "Alice", "Smith", 18, 95.5)

# Update the grade of the student with the first name "Alice"
update_student_grade(db_connection, "Alice", 97.0)

# Delete the student with the last name "Smith"
delete_student_by_last_name(db_connection, "Smith")

# Fetch and display all student records
fetch_and_display_students(db_connection)