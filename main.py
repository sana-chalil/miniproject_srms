# import base64

from flask import Flask, render_template, request, session, jsonify
# import time
# import datetime
from DBConnection import Db

# import tensorflow as tf, sys
app = Flask(__name__)
app.secret_key = "ppppfdkmdfd"
static_path = "C:\\Users\\HP\\Downloads\\srms\\pythonProject1\\static\\"


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route("/login_post", methods=['post'])
def login_post():
    username = request.form['textfield']
    password = request.form['textfield2']
    db = Db()
    qry = "select * from login where username='" + username + "' and password='" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        session["lid"] = res["login_id"]
        if res["type"] == "admin":
            return render_template("/admin/admin_home.html")
        elif res["type"] == "student":
            return render_template("/student/student_home.html")
        elif res["type"] == "parent":
            return render_template("/parent/parent_home.html")

        else:
            return '''<script>alert('Invalid Username or password');window.location='/'</script>'''
    else:
        return '''<script>alert('Invalid Username or password');window.location='/'</script>'''




@app.route('/register')
def register():
    return render_template("register.html")


@app.route("/admin_add_course")
def admin_add():
    return render_template("/admin/add_course.html")


@app.route("/admin_add_course_post", methods=['post'])
def admin_add_post():
    name = request.form["textfield"]
    duration = request.form["textfield2"]
    chapters = request.form["textfield3"]
    description = request.form["textfield4"]
    qry = "INSERT INTO course(course_name,duration,chapters,description) VALUES ('" + name + "','" + duration + "','" + chapters + "','" + description + "')"
    db = Db()
    res = db.insert(qry)
    return '''<script>alert('Inserted course');window.location='/admin_view_course'</script>'''


@app.route("/admin_view_course")
def admin_view():
    db = Db()
    qry = "select * from course"
    print(qry)
    res = db.select(qry)
    return render_template("admin/view_course.html", data=res)


@app.route("/admin_add_student")
def add_student():
    return render_template("/admin/add_student.html")


@app.route("/admin_add_student_post", methods=['post'])
def add_student_post():
    roll_number = request.form["textfield"]
    student_name = request.form["textfield2"]
    email = request.form["textfield3"]
    dob = request.form["textfield4"]
    contact = request.form["textfield5"]
    course_name = request.form["textfield6"]
    qry = "INSERT INTO student(roll_no,student_name,date_of_birth,contact_no,course_name,email) VALUES ('" + roll_number + "','" + student_name + "','" + dob + "','" + contact + "','" + course_name + "','" + email + "')"
    db = Db()
    res = db.insert(qry)
    return '''<script>alert('Inserted student');window.location='/admin_view_student'</script>'''


@app.route("/admin_view_student")
def view_student():
    db = Db()
    qry = "select * from student"
    print(qry)
    res = db.select(qry)
    return render_template("admin/view_student.html", data=res)


@app.route("/add_result")
def add_result():
    return render_template("/admin/add_result.html")


@app.route("/add_result_post", methods=['post'])
def add_result_post():
    roll_no = request.form["textfield"]
    student = request.form["textfield2"]
    course_name = request.form["textfield3"]
    mark_obt = request.form["textfield4"]
    total_mark = request.form["textfield5"]
    percentage = float(mark_obt)/float(total_mark) * 100
    qry = "INSERT INTO result(roll_no,student_name,course_name,mark_obtained,total_mark,percentage) VALUES('" + roll_no + "','" + student + "','" + course_name + "','" + mark_obt + "','" + total_mark + "','" + str(percentage) + "')"
    db = Db()
    res = db.insert(qry)
    return '''<script>alert('Inserted result');window.location='/view_result'</script>'''



# @app.route("/view_result")
# def view_result():
#     qry = "select * from result"
#     return render_template("/admin/view_result.html")
#



@app.route("/view_result")
def view_result():
    db = Db()
    qry = "select * from result"
    print(qry)
    res = db.select(qry)
    return render_template("/admin/view_result.html", data=res)



@app.route("/analysis")
def analysis():
    return render_template("/admin/analysis.html")


@app.route("/home_admin")
def home():
    return render_template("/admin/admin_home.html")


@app.route('/change_password')
def change_password():
    return render_template('admin/change_password.html')


@app.route('/change_pass_post', methods=['post'])
def change_pass_post():
    current_pass = request.form['current_password']
    new_pass = request.form['new_password']
    confirm_pass = request.form['confirm_password']
    d = Db()
    qry = "select * from login where password='" + current_pass + "'"
    res = d.selectOne(qry)
    if res != None:
        if new_pass == confirm_pass:
            qry = "update login set password='" + confirm_pass + "' where login_id='" + str(session['lid']) + "'"
            res = d.update(qry)
            return '''<script>alert('Password Changed');window.location='/'</script>'''
        else:
            return '''<script>alert('Password Mismatch');window.location='/change_password'</script>'''
    else:
        return '''<script>alert('Current Password must be valid');window.location='/change_password'</script>'''

# --------------------------------------STUDENT-SECOND MODULE-----------------------------------------------------------


@app.route('/view_results_student')
def view_results():
    # roll_no = request.form['textfield']
    # db = Db()
    # qry = "select * from result where roll_no='"+roll_no+"'"
    # print(qry)
    # res = db.select(qry)
    return render_template("/student/view_result.html")



@app.route('/view_results_student_post', methods=['post'])
def view_results_post():
    roll_no = request.form['textfield']
    db = Db()
    qry = "select * from result where roll_no='"+roll_no+"'"
    print(qry)
    res = db.select(qry)
    return render_template("/student/view_result.html", data=res)




@app.route('/change_password_student')
def change_password_student():
    return render_template('student/change_password_student.html')


@app.route('/change_pass_student_post', methods=['post'])
def change_pass_student_post():
    current_pass = request.form['current_password']
    new_pass = request.form['new_password']
    confirm_pass = request.form['confirm_password']
    d = Db()
    qry = "select * from login where password='" + current_pass + "'"
    res = d.selectOne(qry)
    if res != None:
        if new_pass == confirm_pass:
            qry = "update login set password='" + confirm_pass + "' where login_id='" + str(session['lid']) + "'"
            res = d.update(qry)
            return '''<script>alert('Password Changed');window.location='/'</script>'''
        else:
            return '''<script>alert('Password Mismatch');window.location='/change_password_student'</script>'''
    else:
        return '''<script>alert('Current Password must be valid');window.location='/change_password_student'</script>'''


@app.route("/home_student")
def student_home():
    return render_template("/student/student_home.html")


# ---------------------------------------PARENT-THIRD MODULE------------------------------------------------------------


@app.route('/view_results_parent')
def view_results_parent():
    return render_template("/parent/view_results_parent.html")



@app.route('/view_results_parent_post', methods=['post'])
def view_results_parent_post():
    roll_no = request.form['textfield']
    db = Db()
    qry = "select * from result where roll_no='"+roll_no+"'"
    print(qry)
    res = db.select(qry)
    return render_template("/parent/view_results_parent.html", data=res)



@app.route('/change_password_parent')
def change_password_parent():
    return render_template('parent/change_password_parent.html')


@app.route('/change_pass_parent_post', methods=['post'])
def change_pass_parent_post():
    current_pass = request.form['current_password']
    new_pass = request.form['new_password']
    confirm_pass = request.form['confirm_password']
    d = Db()
    qry = "select * from login where password='" + current_pass + "'"
    res = d.selectOne(qry)
    if res != None:
        if new_pass == confirm_pass:
            qry = "update login set password='" + confirm_pass + "' where login_id='" + str(session['lid']) + "'"
            res = d.update(qry)
            return '''<script>alert('Password Changed');window.location='/'</script>'''
        else:
            return '''<script>alert('Password Mismatch');window.location='/change_password_parent'</script>'''
    else:
        return '''<script>alert('Current Password must be valid');window.location='/change_password_parent'</script>'''


@app.route("/home_parent")
def parent_home():
    return render_template("/parent/parent_home.html")



@app.route('/register')
def reg():
    return render_template("register.html")


@app.route('/register_post', methods=['post'])
def reg_post():
    name = request.form['textfield']
    u_type = request.form['select']
    # email = request.form['textfield2']
    # contact = request.form['textfield3']
    password = request.form['textfield4']
    qry = "INSERT INTO login(username,password,type) VALUES('" + name + "','" + password + "','" + u_type + "')"
    db = Db()
    res = db.insert(qry)
    return '''<script>alert('Successfully Registered');window.location='/'</script>'''






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
