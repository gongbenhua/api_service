from flask import Blueprint, request

from dynamic.student import student_server
from utils.response.json_fun import to_json_data

student_controller = Blueprint('student_controller', __name__)


@student_controller.route('/select_stud_count', methods=['GET','POST'])
def select_stud_count():
    '''
        Query the number of students
    '''
    row = student_server.select_stud_count()
    return to_json_data(code=200, msg='Request succeeded', data=row)

@student_controller.route('/select_student_by_name', methods=['GET','POST'])
def select_student_by_name():
    '''
        Query student information by name
          :param student_name：
          :return:student information
    '''

    #student_name = request.get_json()["student_name"]
    student_name=request.form["student_name"]
    stud_mes = student_server.select_student_by_name(student_name)
    return to_json_data(code=200, msg='Request succeeded', data=stud_mes)

@student_controller.route('/update_stud_name', methods=['GET','POST'])
def update_stud_name():
    '''
         Modify student name according to student number
          :param    student_id
                    student_name
          :return: Number of code lines affected
    '''
    student_id = request.form["student_id"]
    student_name = request.form["student_name"]
    row = student_server.update_stud_name(student_name)
    return to_json_data(code=200, msg='Request succeeded', data=row)