from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.exceptions import abort
from utils.MysqlDb import db
from auth import login_required
stud = Blueprint('stud', __name__)


@stud.route('/<string:id>/detail')
def detail(id):
    posts = db.select_one_value('SELECT * FROM student where student_id =%s',id)
    return render_template('system/detail.html',detail=posts)

def get_post(id, check_author=True):
    sql = 'SELECT * FROM student_system.student WHERE student_id = %s'
    post = db.select_all_value(sql,id)
    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    return post

@stud.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        subject = request.form["subject"]
        phone = request.form["phone"]
        age = request.form["age"]
        sclass = request.form["class"]
        dormitory = request.form["dormitory"]
        value = (student_id,student_name, subject ,phone, age, sclass, dormitory)
        sql = 'insert into student (student_id, student_name, subject, phone, age, class, dormitory) values(%s,%s,%s,%s,%s,%s,%s)'


        if not student_id:
            error = 'Title is required.'
            flash(error)

        db.execute_value(sql,value)
        return redirect(url_for('index'))

    return render_template('system/create.html')

@stud.route('/delete', methods=('GET', 'POST'))
@login_required
def delete():
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    if request.method == 'POST':
        student_id = request.form['student_id']
        sql='DELETE FROM student_system.student WHERE student_id = %s'
        db.execute_value(sql,student_id)
    return render_template('system/delete.html')

@stud.route('/<string:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        subject = request.form["subject"]
        phone = request.form["phone"]
        age = request.form["age"]
        sclass = request.form["class"]
        dormitory = request.form["dormitory"]
        error = None
        value = (student_name, subject, phone, age, sclass, dormitory, student_id)

        if not student_id:
            error = 'student_id is required.'

        if error is not None:
            flash(error)
        else:
            sql = 'UPDATE student_system.student SET student_name = %s, subject = %s , phone = %s, age = %s, class = %s, dormitory = %s WHERE student_id = %s'
            db.execute_value(sql, value)
            return redirect(url_for('index'))

    return render_template('system/update.html', post=post)

