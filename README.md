# Smart E-Learning Platform  

## Overview  
The **Smart E-Learning Platform** is a database-driven educational platform designed to manage essential academic and administrative data in a structured and efficient manner. It uses **MySQL** for backend data management, **Python** for logic and data processing, and **Streamlit** for an interactive frontend interface. The platform supports comprehensive **CRUD (Create, Read, Update, Delete)** operations and advanced features like complex queries, aggregate functions, stored procedures, and triggers.  

---

## Features  
✅ Centralized data management for academic records  
✅ User-friendly interface using Streamlit  
✅ Supports complex relational queries and aggregate functions  
✅ Automated data handling with stored procedures and triggers  
✅ Real-time tracking of student progress and course enrolments  

---

## Table of Contents  
- [Abstract](#abstract)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Database Schema](#database-schema)  
- [CRUD Operations](#crud-operations)  
- [Queries](#queries)  
- [Stored Procedures, Functions, and Triggers](#stored-procedures-functions-and-triggers)  
- [Technologies Used](#technologies-used)  
- [Screenshots](#screenshots)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Abstract  
This project presents the development of a **Smart E-Learning Platform** designed to manage essential academic and administrative data for a digital learning environment. The system includes nine core entities:  
- `student`  
- `instructor`  
- `course`  
- `enrolment`  
- `assignment`  
- `quiz`  
- `submission`  
- `complaint`  
- `phone`  

The platform supports seamless **CRUD** operations through a user-friendly **Streamlit** interface, facilitating efficient data storage, retrieval, and manipulation. The system is scalable, reliable, and capable of handling complex queries and automated triggers, enhancing the overall learning experience for students and instructors.  

---

## Installation  
### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/smart-e-learning-platform.git
cd smart-e-learning-platform
```
2. Set Up Virtual Environment (Optional)
```bash
python -m venv env
source env/bin/activate      # Linux/macOS
# .\env\Scripts\activate      # Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Set Up MySQL Database
Create a MySQL database using the provided schema.sql file:
```sql
source schema.sql;
```
5. Start Streamlit Application
```bash
streamlit run app.py

