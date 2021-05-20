from flask import Flask,render_template,request,session
from DBConnection import Db
app = Flask(__name__)
app.secret_key="hi"

@app.route('/')
def hello_world():
    return render_template("LOGIN.html")
@app.route("/login_post",methods=['POST'])
def login():
    username=request.form["textfield"]
    password=request.form["textfield2"]
    db=Db()
    qry="select * from login where Login_Name='"+username+"' and Password='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session["lid"]=res["Login_id"]
        if res["Login_type"]=="admin":
            return render_template("admin_home.html")
        if res["Login_type"] == "doctor":
            return render_template("doctor/Dr_home.html")
        else:
            return '''<script>alert('Invalid username or Password');window.location="/"</script>'''
    else:
        return '''<script>alert('Invalid username or Password');window.location="/"</script>'''

@app.route('/adm_view_doctor_request')
def adm_approve_doctors():
    qry="select doctor.* from doctor inner join login on doctor.Doc_login_id=login.Login_id where login.Login_type ='pending'"
    db=Db()
    res=db.select(qry)
    return render_template("admin_approve_doctors.html",data=res)

@app.route('/admin_accept_reject_doctor/<lid>/<status>')
def admin_accept_reject_doctor(lid,status):
    qry="update login set Login_type ='"+status+"'where Login_id ='"+lid+"'"
    db=Db()
    db.update(qry)
    return '''<script>alert('Succesfully Updated');window.location="/adm_view_doctor_request"</script>'''


@app.route('/admin_reply/<cid>')
def admin_reply(cid):
    return render_template("admin_reply.html",cid=cid)

@app.route("/Admin_reply_post",methods=['POST'])
def Admin_reply_post():
    cid=request.form["cid"]
    reply=request.form ["textarea"]
    db=Db()
    qry="update complaint set C_reply='"+reply+"' where C_id='"+cid+"'"
    res = db.update(qry)
    return admin_view_complaint()

@app.route('/admin_view_complaint')
def admin_view_complaint():
    qry="Select * from complaint"
    db=Db()
    res=db.select(qry)
    return render_template("admin_view_complaint.html",data=res)

@app.route('/admin_View_User')
def View_User():
    qry = "select * from user"
    db = Db()
    res = db.select(qry)
    return render_template("View_User.html",data=res)

@app.route('/admin_search_user',methods=["post"])
def admin_search_user():
    name=request.form["textfield"]
    qry = "select * from user where U_name like '%"+name+"%'"
    db = Db()
    res = db.select(qry)
    return render_template("View_User.html",data=res)


@app.route('/Change_password')
def Change_password():
    return render_template("doctor/Change_password.html")

@app.route('/change_password_post',methods=['post'])
def change_password_post():
    current_password =request.form["textfield"]
    password= request.form["textfield2"]
    confirm_password=request.form["textfield3"]
    db=Db()
    lid=session["lid"]
    qry2="select Password from login where Login_id ='"+str(lid)+"'"
    res =db.selectOne(qry2)
    if res["Password"] == current_password :
        if password == confirm_password :
            qry ="update login set Password = '"+confirm_password+"'WHERE Login_id = '"+str(lid)+"'"
            res = db.update(qry)
            return '''<script>alert('Password changed');window.location ='/'</script> '''
        else:
            return '''<script>alert('Password not equal to current password');window.location ='/Change_password'</script> '''
    else :
        return '''<script>alert('Password incorrect');window.location ='/Change_password'</script> '''



@app.route('/Dr_register')
def Dr_register():
    return render_template("Dr_register.html")

@app.route("/dr_register_post",methods=['POST'])
def dr_register():
    name=request.form["textfield"]
    Dob=request.form["textfield2"]
    gender=request.form["Gender"]
    email=request.form["textfield3"]
    experince=request.form["textfield4"]
    image=request.files["fileField"]
    phone=request.form["textfield5"]
    area_of_spec=request.form["textfield6"]
    state=request.form["state"]
    district=request.form["select2"]
    place=request.form["textfield7"]
    pin=request.form["textfield8"]
    password=request.form["password"]
    latitude=request.form["lat"]
    longitude=request.form["lon"]

    db=Db()
    image.save("C:\\Users\\Hridhin\\PycharmProjects\\smpl\\static\\doctor\\"+image.filename)
    path='/static/doctor/'+image.filename
    QRY="insert into login (Login_type,Login_Name,Password) values ('pending','"+email+"','"+password+"')"
    lid=str(db.insert(QRY))
    qry2="insert into doctor(Doc_name,Doc_dob,Doc_gender,Doc_email,Doc_phone,Doc_area_of_spec,Doc_state,Doc_district,Doc_place,Doc_pin,Doc_lat,Doc_log,Doc_Experince,Doc_login_id,Doc_img)values('"+name+"','"+Dob+"','"+gender+"','"+email+"','"+phone+"','"+area_of_spec+"','"+state+"','"+district+"','"+place+"','"+pin+"','"+latitude+"','"+longitude+"','"+experince+"','"+lid+"','"+str(path)+"')"
    print(qry2)
    res=db.insert(qry2)
    return render_template('/LOGIN.html')

@app.route('/dr_view_profile')
def dr_view_profile():
    lid = session["lid"]
    qry ="select * from doctor where Doc_login_id = '"+str(lid)+"'"
    db=Db()
    res =db.selectOne(qry)
    return render_template('doctor/View_profile.html',data=res)


@app.route('/Dr_register_update')
def Dr_register_update():
    return render_template("doctor/Dr_register_update.html")



@app.route('/Dr_schedule')
def Dr_schedule():
    qry = "select * FROM schedule WHERE Doc_id ='"+str (session["lid"])+"' "
    db = Db()
    res = db.select(qry)
    return render_template("doctor/Dr_schedule.html", data=res)

@app.route('/Dr_schedule_Delete/<sid>')
def Dr_schedule_Delete(sid):
    qry ="delete from schedule where S_id ='"+sid+"' "
    db=Db()
    res=db.delete(qry)
    return Dr_schedule()

@app.route('/LOGIN')
def LOGIN():
    return render_template("LOGIN.html")

@app.route('/Schedule_manage')
def Schedule_manage():
    return render_template("doctor/Schedule_manage.html")

@app.route('/Schedule_manage_post',methods=["post"])
def Schedule_manage_post():
    date = request.form["textfield"]
    from_time =request.form["textfield2"]
    to_time =request.form["textfield3"]
    lid = session["lid"]
    qry ="insert into schedule(D_from_time,D_to_time,Day,Doc_id)values ('"+from_time+"','"+to_time+"','"+date+"','"+str(lid)+"')"
    db=Db()
    db.insert(qry)
    return Schedule_manage()



@app.route('/User_prediction')
def User_prediction():
    return render_template("User_prediction.html")

@app.route('/user_reg')
def user_reg():
    return render_template("user_reg.html")

@app.route('/View_Booking')
def View_Booking():
    db=Db()
    qry ="select user.U_name,booking.B_date,schedule.D_from_time,schedule.D_to_time,schedule.Day,booking.B_id,user.U_Login_id from booking inner join schedule on booking.S_id =schedule.S_id inner join user on user.U_Login_id = booking.U_id"
    res = db.select(qry)
    return render_template("doctor/View_Booking.html",data = res)

@app.route('/View_feedback')
def View_feedback():
    db=Db()
    qry ="select user.U_name,feedback.* from user inner join feedback on user.U_Login_id = feedback.U_id"
    res=db.select(qry)
    return render_template("doctor/View_feedback.html",data=res)


#@app.route('/View_prediction_history')
#def View_prediction_history():

@app.route('/View_prescription')
def View_prescription():


    return render_template("View_prediction_history.html")


@app.route('/doctor_add_presciption/<u_lid>')
def doctor_add_presciption(u_lid):
    db=Db()
    qry ="select prescription.prescription,prescription.pres_id,doctor.Doc_name,prescription.pres_date,prescription.pres_time from prescription inner join prescription.Doc_id =doctor.Doc_id where prediction.U_id='"+u_lid+"'"
    res = db.select(qry)
    return render_template("doctor/View_prescription.html",data=res,ulid=u_lid)

@app.route('/doctor_add_presciption_post ',methods=["post"])
def doctor_add_presciption_post():
    db=Db()
    ulid=request.form["ulid"]
    pres=request.form["view_prescription"]
    dr_lid =session["lid"]
    qry ="insert into prescription(U_id,prescription,Doc_id,pres_date,pres_time) values ('"+ulid+"','"+pres+"','"+dr_lid+"',curdate(),curtime())"
    res = db.insert(qry)
    return render_template("doctor/View_prescription.html")



@app.route('/View_report')
def View_report():
    return render_template("View_report.html")









if __name__ == '__main__':
    app.run()
