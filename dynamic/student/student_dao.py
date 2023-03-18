from utils.MysqlDb import db


def select_stud_count():
    '''
        Query the number of students
        :return:dictionary：{count(1)：2}
    '''
    sql = 'select count(1) from student'
    count = db.select_one(sql)
    return count

def select_student_by_name(student_name:str):
    '''
        Query student information by name
          :param: student_name
          :return: Number of code lines affected
    '''
    sql = 'select * from student where student_name = %s'
    value = (student_name)
    # Call driver to execute sql statements
    stud_mes = db.select_all_value(sql, value)
    return stud_mes

def update_stud_name(student_id:str ,student_name:str):
    '''
         Modify student name according to student number
          :param: student_id:
                  student_name:
          :return: Number of code lines affected
    '''

    sql = 'update student set student_name = %s where student_id = %s'
    value = (student_name, student_id)
    # Call driver to execute sql statements
    rowcount = db.execute_value(sql, value)
    return rowcount

def insert_stud(student_id, student_name,subject ,phone):
    '''
         add new student information
          :param: student_id, student_name,subject ,phone
          :return:Number of code lines affected
    '''
    sql = 'insert into student (student_id, student_name, subject, phone)' \
          'values(%s,%s,%s,%s)'
    value = (student_id,student_name,  subject ,phone)
    rowcount = db.execute_value(sql, value)
    return rowcount

def delete_stud_by_name(student_name):
    '''
         Delete student information by name
          :param: student_name
          :return:Number of code lines affected
    '''
    sql = 'delete from student where student_name=%s'
    value = (student_name)
    rowcount = db.execute_value(sql, value)
    return rowcount

def select_score_by_name(student_name:str, course_name:str, teacher_name:str ):
    '''
        Query student information by name
          :param: student_name
                  course_name
                  teacher_name
          :return: Number of code lines affected
    '''
    score_sql = 'select s.student_name, scs.score from ' \
                'student s  INNER JOIN student_course_select scs on s.student_id= scs.student_id ' \
                'INNER JOIN course c ON scs.course_id = c.course_id  ' \
                'INNER JOIN teacher t ON c.teacher_id = t.teacher_id ' \
                'where s.student_name=%s and c.course_name=%s and t.teacher_name=%s'
    value = (student_name,course_name,teacher_name)
    stud_score = db.select_all_value(score_sql,value)
    return stud_score

def insert_score(student_name:str, course_name:str, teacher_name:str, score):
    '''
        Query student information by name
          :param: student_name
                  course_name
          :return: Number of code lines affected
    '''
    student_id_sql = 'select student_id from student where student_name = %s'
    student_name_value = (student_name)
    stud_msg = db.select_all_value(student_id_sql, student_name_value)[0]
    stud_id = stud_msg['student_id']
    ## get student_id
    teacher_id_sql = 'select teacher_id from teacher where teacher_name=%s'
    teacher_name_value = (teacher_name)
    teacher_msg = db.select_all_value(teacher_id_sql, teacher_name_value)[0]
    teacher_id = teacher_msg['teacher_id']
    ## get teacher_id
    course_id_sql = 'select course_id from course where course_name=%s and teacher_id=%s'
    course_name_value = (course_name,teacher_id)
    course_msg = db.select_all_value(course_id_sql, course_name_value)[0]
    course_id = course_msg['course_id']
    ##get course_id
    insert_score_sql = 'insert into student_course_select (student_id, course_id, score)' \
    'values(%s,%s,%s)'
    value = (stud_id,course_id,score)
    rowcount = db.execute_value(insert_score_sql,value)
    return rowcount

if __name__ == '__main__':

#     x = update_stud_name("std_2019015", "jack")
#     x = select_student_by_name("jack")
#     x = insert_stud("std_2022045","snow", "english", "77777777777")
#     x = delete_stud_by_name("snow")
    x = select_score_by_name("snow","Politics","york")
    print(x)


