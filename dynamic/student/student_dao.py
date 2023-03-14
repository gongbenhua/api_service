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

if __name__ == '__main__':

#     x=update_stud_name("std_2019015", "吴六")
    x = select_student_by_name("张三")
    #x = insert_stud("std_2078556","老何", "英语", "77777777777")
    #x=delete_stud_by_name("std_2078556")
    print(x)


