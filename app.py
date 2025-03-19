import streamlit as st
import mysql.connector
from mysql.connector import Error

# Database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="dbms"
    )

# CRUD Functions for Student
def add_student_via_procedure(student_id, email, dob, fname, lname, enrollment_date):
    conn = create_connection()
    cursor = conn.cursor()
    query = "CALL add_student_procedure(%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (student_id, email, dob, fname, lname, enrollment_date))
    conn.commit()
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_student(student_id, email, dob, fname, lname, enrollment_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE student SET Email=%s, DOB=%s, Fname=%s, Lname=%s, EnrollmentDate=%s WHERE StudentID=%s",
                   (email, dob, fname, lname, enrollment_date, student_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE StudentID = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Instructor
def add_instructor(instructor_id, phone, email, name, specialization):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO instructor (InstructorID, Phone, Email, Name, Specialisation) VALUES (%s, %s, %s, %s, %s)",
                   (instructor_id, phone, email, name, specialization))
    conn.commit()
    cursor.close()
    conn.close()

def view_instructors():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM instructor")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_instructor(instructor_id, phone, email, name, specialization):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE instructor SET Phone=%s, Email=%s, Name=%s, Specialisation=%s WHERE InstructorID=%s",
                   (phone, email, name, specialization, instructor_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_instructor(instructor_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM instructor WHERE InstructorID = %s", (instructor_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Course
def add_course(course_id, instructor_id, duration, title, beginner, intermediate, advanced, description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO course (CourseID, InstructorID, Duration, Title, Beginner, Intermediate, Advanced, Description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (course_id, instructor_id, duration, title, beginner, intermediate, advanced, description))
    conn.commit()
    cursor.close()
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_course(course_id, instructor_id, duration, title, beginner, intermediate, advanced, description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE course SET InstructorID=%s, Duration=%s, Title=%s, Beginner=%s, Intermediate=%s, Advanced=%s, Description=%s WHERE CourseID=%s",
                   (instructor_id, duration, title, beginner, intermediate, advanced, description, course_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course WHERE CourseID = %s", (course_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Assignment
def add_assignment(assignment_id, course_id, title, description, due_date, total_marks):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO assignment (AssignmentID, CourseID, Title, Description, DueDate, TotalMarks) VALUES (%s, %s, %s, %s, %s, %s)",
                   (assignment_id, course_id, title, description, due_date, total_marks))
    conn.commit()
    cursor.close()
    conn.close()

def view_assignments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assignment")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_assignment(assignment_id, course_id, title, description, due_date, total_marks):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE assignment SET CourseID=%s, Title=%s, Description=%s, DueDate=%s, TotalMarks=%s WHERE AssignmentID=%s",
                   (course_id, title, description, due_date, total_marks, assignment_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_assignment(assignment_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assignment WHERE AssignmentID = %s", (assignment_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Complaint
def add_complaint(complaint_id, student_id, description, submission_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO complaint (ComplaintID, StudentID, Description, SubmissionDate, Open, InProgress, Resolved) VALUES (%s, %s, %s, %s, 1, 0, 0)",
                   (complaint_id, student_id, description, submission_date))
    conn.commit()
    cursor.close()
    conn.close()

def view_complaints():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM complaint")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_complaint(complaint_id, student_id, description, submission_date, open_status, in_progress, resolved):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE complaint SET StudentID=%s, Description=%s, SubmissionDate=%s, Open=%s, InProgress=%s, Resolved=%s WHERE ComplaintID=%s",
                   (student_id, description, submission_date, open_status, in_progress, resolved, complaint_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_complaint(complaint_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM complaint WHERE ComplaintID = %s", (complaint_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Enrollment
def add_enrollment(enrollment_id, course_id, student_id, progress, enrollment_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollment (EnrollmentID, CourseID, StudentID, Progress, EnrollmentDate) VALUES (%s, %s, %s, %s, %s)",
                   (enrollment_id, course_id, student_id, progress, enrollment_date))
    conn.commit()
    cursor.close()
    conn.close()

def view_enrollments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM enrollment")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_enrollment(enrollment_id, course_id, student_id, progress, enrollment_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE enrollment SET CourseID=%s, StudentID=%s, Progress=%s, EnrollmentDate=%s WHERE EnrollmentID=%s",
                   (course_id, student_id, progress, enrollment_date, enrollment_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_enrollment(enrollment_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM enrollment WHERE EnrollmentID = %s", (enrollment_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Quiz
def add_quiz(quiz_id, course_id, title, total_marks):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quiz (QuizID, CourseID, Title, TotalMarks) VALUES (%s, %s, %s, %s)",
                   (quiz_id, course_id, title, total_marks))
    conn.commit()
    cursor.close()
    conn.close()

def view_quizzes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quiz")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_quiz(quiz_id, course_id, title, total_marks):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE quiz SET CourseID=%s, Title=%s, TotalMarks=%s WHERE QuizID=%s",
                   (course_id, title, total_marks, quiz_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_quiz(quiz_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quiz WHERE QuizID = %s", (quiz_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Submission
def add_submission(submission_id, assignment_id, student_id, marks_obtained, submission_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO submission (SubmissionID, AssignmentID, StudentID, MarksObtained, SubmissionDate) VALUES (%s, %s, %s, %s, %s)",
                   (submission_id, assignment_id, student_id, marks_obtained, submission_date))
    conn.commit()
    cursor.close()
    conn.close()

def view_submissions():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM submission")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_submission(submission_id, assignment_id, student_id, marks_obtained, submission_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE submission SET AssignmentID=%s, StudentID=%s, MarksObtained=%s, SubmissionDate=%s WHERE SubmissionID=%s",
                   (assignment_id, student_id, marks_obtained, submission_date, submission_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_submission(submission_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM submission WHERE SubmissionID = %s", (submission_id,))
    conn.commit()
    cursor.close()
    conn.close()

# CRUD Functions for Phone
def add_phone(student_id, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO phone (StudentID, Phone) VALUES (%s, %s)",
                   (student_id, phone))
    conn.commit()
    cursor.close()
    conn.close()

def view_phones():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phone")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_phone(student_id, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE phone SET Phone=%s WHERE StudentID=%s",
                   (phone, student_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_phone(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM phone WHERE StudentID = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Function to display student details with their enrolled courses (Join Query)
def show_student_enrollments():
    conn = create_connection()
    cursor = conn.cursor()
    query = """
    SELECT student.StudentID, student.Fname, student.Lname, course.Title 
    FROM student 
    JOIN enrollment ON student.StudentID = enrollment.StudentID 
    JOIN course ON enrollment.CourseID = course.CourseID;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Function to get the highest marks using SQL function
def highest_marks_in_assignment_via_function(assignment_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT get_highest_marks(%s);"
    cursor.execute(query, (assignment_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Function to get the average marks using SQL function
def average_marks_in_course_via_function(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT get_average_marks(%s);"
    cursor.execute(query, (course_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None



# Streamlit UI
st.title("DBMS Project Management System")

menu = st.sidebar.selectbox("Select Table", ("Student", "Instructor", "Course", "Assignment", "Complaint", "Enrollment", "Quiz", "Submission", "Phone"))

if menu == "Student":
    st.subheader("Manage Students")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        student_id = st.number_input("Student ID", min_value=1)
        email = st.text_input("Email")
        dob = st.date_input("Date of Birth")
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        enrollment_date = st.date_input("Enrollment Date")
        if st.button("Add Student"):
            add_student_via_procedure(student_id, email, dob, fname, lname, enrollment_date)
            st.success("Student added successfully!")

    elif action == "View":
        st.write(view_students())

    elif action == "Update":
        student_id = st.number_input("Student ID to Update", min_value=1)
        email = st.text_input("New Email")
        dob = st.date_input("New Date of Birth")
        fname = st.text_input("New First Name")
        lname = st.text_input("New Last Name")
        enrollment_date = st.date_input("New Enrollment Date")
        if st.button("Update Student"):
            update_student(student_id, email, dob, fname, lname, enrollment_date)
            st.success("Student updated successfully!")

    elif action == "Delete":
        student_id = st.number_input("Student ID to Delete", min_value=1)
        if st.button("Delete Student"):
            delete_student(student_id)
            st.success("Student deleted successfully!")

elif menu == "Instructor":
    st.subheader("Manage Instructors")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        instructor_id = st.number_input("Instructor ID", min_value=1)
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        name = st.text_input("Name")
        specialization = st.text_input("Specialization")
        if st.button("Add Instructor"):
            add_instructor(instructor_id, phone, email, name, specialization)
            st.success("Instructor added successfully!")

    elif action == "View":
        st.write(view_instructors())

    elif action == "Update":
        instructor_id = st.number_input("Instructor ID to Update", min_value=1)
        phone = st.text_input("New Phone")
        email = st.text_input("New Email")
        name = st.text_input("New Name")
        specialization = st.text_input("New Specialization")
        if st.button("Update Instructor"):
            update_instructor(instructor_id, phone, email, name, specialization)
            st.success("Instructor updated successfully!")

    elif action == "Delete":
        instructor_id = st.number_input("Instructor ID to Delete", min_value=1)
        if st.button("Delete Instructor"):
            delete_instructor(instructor_id)
            st.success("Instructor deleted successfully!")

elif menu == "Course":
    st.subheader("Manage Courses")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        course_id = st.number_input("Course ID", min_value=1)
        instructor_id = st.number_input("Instructor ID", min_value=1)
        duration = st.number_input("Duration (in weeks)", min_value=1)
        title = st.text_input("Title")
        beginner = st.checkbox("Beginner")
        intermediate = st.checkbox("Intermediate")
        advanced = st.checkbox("Advanced")
        description = st.text_area("Description")
        if st.button("Add Course"):
            add_course(course_id, instructor_id, duration, title, beginner, intermediate, advanced, description)
            st.success("Course added successfully!")

    elif action == "View":
        st.write(view_courses())

    elif action == "Update":
        course_id = st.number_input("Course ID to Update", min_value=1)
        instructor_id = st.number_input("New Instructor ID", min_value=1)
        duration = st.number_input("New Duration (in weeks)", min_value=1)
        title = st.text_input("New Title")
        beginner = st.checkbox("Beginner")
        intermediate = st.checkbox("Intermediate")
        advanced = st.checkbox("Advanced")
        description = st.text_area("New Description")
        if st.button("Update Course"):
            update_course(course_id, instructor_id, duration, title, beginner, intermediate, advanced, description)
            st.success("Course updated successfully!")

    elif action == "Delete":
        course_id = st.number_input("Course ID to Delete", min_value=1)
        if st.button("Delete Course"):
            delete_course(course_id)
            st.success("Course deleted successfully!")

elif menu == "Assignment":
    st.subheader("Manage Assignments")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        assignment_id = st.number_input("Assignment ID", min_value=1)
        course_id = st.number_input("Course ID", min_value=1)
        title = st.text_input("Title")
        description = st.text_area("Description")
        due_date = st.date_input("Due Date")
        total_marks = st.number_input("Total Marks", min_value=1)
        if st.button("Add Assignment"):
            add_assignment(assignment_id, course_id, title, description, due_date, total_marks)
            st.success("Assignment added successfully!")

    elif action == "View":
        st.write(view_assignments())

    elif action == "Update":
        assignment_id = st.number_input("Assignment ID to Update", min_value=1)
        course_id = st.number_input("New Course ID", min_value=1)
        title = st.text_input("New Title")
        description = st.text_area("New Description")
        due_date = st.date_input("New Due Date")
        total_marks = st.number_input("New Total Marks", min_value=1)
        if st.button("Update Assignment"):
            update_assignment(assignment_id, course_id, title, description, due_date, total_marks)
            st.success("Assignment updated successfully!")

    elif action == "Delete":
        assignment_id = st.number_input("Assignment ID to Delete", min_value=1)
        if st.button("Delete Assignment"):
            delete_assignment(assignment_id)
            st.success("Assignment deleted successfully!")

elif menu == "Complaint":
    st.subheader("Manage Complaints")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        complaint_id = st.number_input("Complaint ID", min_value=1)
        student_id = st.number_input("Student ID", min_value=1)
        description = st.text_area("Description")
        submission_date = st.date_input("Submission Date")
        if st.button("Add Complaint"):
            add_complaint(complaint_id, student_id, description, submission_date)
            st.success("Complaint added successfully!")

    elif action == "View":
        st.write(view_complaints())

    elif action == "Update":
        complaint_id = st.number_input("Complaint ID to Update", min_value=1)
        student_id = st.number_input("New Student ID", min_value=1)
        description = st.text_area("New Description")
        submission_date = st.date_input("New Submission Date")
        open_status = st.checkbox("Open")
        in_progress = st.checkbox("In Progress")
        resolved = st.checkbox("Resolved")
        if st.button("Update Complaint"):
            update_complaint(complaint_id, student_id, description, submission_date, open_status, in_progress, resolved)
            st.success("Complaint updated successfully!")

    elif action == "Delete":
        complaint_id = st.number_input("Complaint ID to Delete", min_value=1)
        if st.button("Delete Complaint"):
            delete_complaint(complaint_id)
            st.success("Complaint deleted successfully!")

elif menu == "Enrollment":
    st.subheader("Manage Enrollments")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        enrollment_id = st.number_input("Enrollment ID", min_value=1)
        course_id = st.number_input("Course ID", min_value=1)
        student_id = st.number_input("Student ID", min_value=1)
        progress = st.number_input("Progress (in %)", min_value=0, max_value=100)
        enrollment_date = st.date_input("Enrollment Date")
        if st.button("Add Enrollment"):
            add_enrollment(enrollment_id, course_id, student_id, progress, enrollment_date)
            st.success("Enrollment added successfully!")

    elif action == "View":
        # Show student enrollments with join query
        st.subheader("Enrolled Students with Courses")
        enrollments = show_student_enrollments()
        if enrollments:
            # Display the result in a table
            for enrollment in enrollments:
                st.write(f"Student ID: {enrollment[0]}, Name: {enrollment[1]} {enrollment[2]}, Course: {enrollment[3]}")
        else:
            st.write("No enrollments found.")

    elif action == "Update":
        enrollment_id = st.number_input("Enrollment ID to Update", min_value=1)
        course_id = st.number_input("New Course ID", min_value=1)
        student_id = st.number_input("New Student ID", min_value=1)
        progress = st.number_input("New Progress (in %)", min_value=0, max_value=100)
        enrollment_date = st.date_input("New Enrollment Date")
        if st.button("Update Enrollment"):
            update_enrollment(enrollment_id, course_id, student_id, progress, enrollment_date)
            st.success("Enrollment updated successfully!")

    elif action == "Delete":
        enrollment_id = st.number_input("Enrollment ID to Delete", min_value=1)
        if st.button("Delete Enrollment"):
            delete_enrollment(enrollment_id)
            st.success("Enrollment deleted successfully!")

elif menu == "Quiz":
    st.subheader("Manage Quizzes")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        quiz_id = st.number_input("Quiz ID", min_value=1)
        course_id = st.number_input("Course ID", min_value=1)
        title = st.text_input("Title")
        total_marks = st.number_input("Total Marks", min_value=1)
        if st.button("Add Quiz"):
            add_quiz(quiz_id, course_id, title, total_marks)
            st.success("Quiz added successfully!")

    elif action == "View":
        st.write(view_quizzes())

    elif action == "Update":
        quiz_id = st.number_input("Quiz ID to Update", min_value=1)
        course_id = st.number_input("New Course ID", min_value=1)
        title = st.text_input("New Title")
        total_marks = st.number_input("New Total Marks", min_value=1)
        if st.button("Update Quiz"):
            update_quiz(quiz_id, course_id, title, total_marks)
            st.success("Quiz updated successfully!")

    elif action == "Delete":
        quiz_id = st.number_input("Quiz ID to Delete", min_value=1)
        if st.button("Delete Quiz"):
            delete_quiz(quiz_id)
            st.success("Quiz deleted successfully!")

elif menu == "Submission":
    st.subheader("Manage Submissions")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        submission_id = st.number_input("Submission ID", min_value=1)
        assignment_id = st.number_input("Assignment ID", min_value=1)
        student_id = st.number_input("Student ID", min_value=1)
        marks_obtained = st.number_input("Marks Obtained", min_value=0)
        submission_date = st.date_input("Submission Date")
        if st.button("Add Submission"):
            add_submission(submission_id, assignment_id, student_id, marks_obtained, submission_date)
            st.success("Submission added successfully!")

    elif action == "View":
        st.write(view_submissions())
        st.subheader("Highest and Average Marks")

        # Highest Marks Functionality
        assignment_id = st.number_input("Enter Assignment ID for Highest Marks", min_value=1, step=1)
        if st.button("Get Highest Marks"):
            highest_marks = highest_marks_in_assignment_via_function(assignment_id)
            if highest_marks is not None:
                st.write(f"Highest Marks in Assignment {assignment_id}: {highest_marks}")
            else:
                st.write("No data found for this assignment.")

        # Average Marks Functionality
        course_id = st.number_input("Enter Course ID for Average Marks", min_value=1, step=1)
        if st.button("Get Average Marks"):
            avg_marks = average_marks_in_course_via_function(course_id)
            if avg_marks is not None:
                st.write(f"Average Marks in Course {course_id}: {avg_marks}")
            else:
                st.write("No data found for this course.")
    
    elif action == "Update":
        submission_id = st.number_input("Submission ID to Update", min_value=1)
        assignment_id = st.number_input("New Assignment ID", min_value=1)
        student_id = st.number_input("New Student ID", min_value=1)
        marks_obtained = st.number_input("New Marks Obtained", min_value=0)
        submission_date = st.date_input("New Submission Date")
        
        if st.button("Update Submission"):
            try:
                conn = create_connection()
                cursor = conn.cursor()

                # Update the submission in the database
                cursor.execute("""
                    UPDATE submission 
                    SET AssignmentID = %s, StudentID = %s, MarksObtained = %s, SubmissionDate = %s 
                    WHERE SubmissionID = %s
                """, (assignment_id, student_id, marks_obtained, submission_date, submission_id))

                conn.commit()
                cursor.close()
                conn.close()
                
                st.success("Submission updated successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")

    elif action == "Delete":
        submission_id = st.number_input("Submission ID to Delete", min_value=1)
        if st.button("Delete Submission"):
            delete_submission(submission_id)
            st.success("Submission deleted successfully!")


elif menu == "Phone":
    st.subheader("Manage Phones")
    action = st.selectbox("Choose Action", ("Add", "View", "Update", "Delete"))

    if action == "Add":
        student_id = st.number_input("Student ID", min_value=1)
        phone = st.text_input("Phone")
        if st.button("Add Phone"):
            add_phone(student_id, phone)
            st.success("Phone added successfully!")

    elif action == "View":
        st.write(view_phones())

    elif action == "Update":
        student_id = st.number_input("Student ID to Update", min_value=1)
        phone = st.text_input("New Phone")
        if st.button("Update Phone"):
            update_phone(student_id, phone)
            st.success("Phone updated successfully!")

    elif action == "Delete":
        student_id = st.number_input("Student ID to Delete", min_value=1)
        if st.button("Delete Phone"):
            delete_phone(student_id)
            st.success("Phone deleted successfully!")
        
