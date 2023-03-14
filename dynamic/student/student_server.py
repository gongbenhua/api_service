from dynamic.student import student_dao

def select_stud_count():
    '''
            Query the number of students
            :return: number of lines in student list
    '''
    count = student_dao.select_stud_count()
    return count

def select_student_by_name(student_name:str):
    '''
        Query student information by name
          :param student_name
          :return:Dictionary list of student information
    '''
    stud_mes = student_dao.select_student_by_name(student_name)
    return stud_mes

def update_stud_name(student_id:str ,student_name:str):
    '''
         Modify student name according to student number
          :param    student_id
                    student_name
          :return:Number of code lines affected
    '''


    row = student_dao.update_stud_name(student_id, student_name)
    row_dict ={"Number of code lines affected": row}
    return row_dict

def insert_stud(student_id, student_name,subject ,phone):
    '''
         add new student information
          :param    student_id
                    student_name
                    subject
                    phone
          :return:Number of code lines affected
    '''
    row = student_dao.insert_stud(student_id, student_name,subject ,phone)
    row_dict = {"Number of code lines affected": row}
    return row_dict

def delete_stud_by_name(student_name):
    '''
         Delete student information by name
          :param student_name:student name
          :return:Number of code lines affected
    '''
    row = student_dao.delete_stud_by_name(student_name)
    row_dict = {"Number of code lines affected": row}
    return row_dict