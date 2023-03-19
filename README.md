# api_service_system
(Due to my joining Fidelity and recent urgent work, the final front-end UI presentation system is not yet mature, and instead of changing the style, I use the original format)

simple api_service_system

* Before running this code, please use software such as navicat to import the **student_system.sql** into MySQL and change config in **setting.py** to your local configuration(host;post;user;password)

This project provides a simple API to Curd the database of the student system. The student database is mainly divided into four tables

1. student: store basic student information such as student ID, name, major, and phone number

2. teacher: store basic teacher information such as teacher number, name, and phone number

3. course: store the course number, course name, and teacher

4. student_course_select: store course numbers, student numbers, and scores



The following APIs are mainly provided:

1. ```
   '/select_stud_count'：Query the number of students
   ```

2. ```
   '/select_student_by_name'：Query student information by name; required parameters:"student_name"
   ```

3. ```
   '/select_score_by_name': Get student score by student_name, course_name and teacher_name, required parameters:"student_name","course_name","teacher_name"
   ```

4. ```
   '/update_stud_name': Modify student name according to student number; required parameters:"student_id", "student_name"
   ```

5. ```
   '/delete_stud_name': Delete student according to student name; required parameters:"student_name"
   ```

6. ```
   '/insert_stud': Add new student information; required parameters:"student_id", "student_name", "subject", "phone", "age", "sclass", "dormitory"
   ```

7. ```
   '/insert_score': Add new student score information;required parameters:"student_name", "course_name", "teacher_name", "score"
   ```

In order to facilitate display and use, a front-end system was written to operate the database on the web page using APIs

Main functions provided:

* Registration and login (after login, you can unlock the add, modify, and delete functions)

* The main page displays all student IDs. Click on ID to view basic student information

* Add new student information
* Modify student name according to student number
* Delete student according to student name



Instructions:

requirement: utils; flask; pymysql

After changing **setting.py** and importing **student_system.sql** in MySQL，run main.py

default: http://127.0.0.1:5001/ , database operations can be performed in the visual interface

Access http://127.0.0.1:5001/a will return "Hello world"



example for api using:

```
curl -d "student_name=jack&course_name=Politics&teacher_name=frank" http://127.0.0.1:5001/backend/student/select_score_by_name
```

Get student score by student_name, course_name and teacher_name

