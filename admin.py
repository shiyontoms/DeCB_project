from flask import *
from database import *
admin=Blueprint('admin',__name__)


@admin.route('/admin_home')
def admin_home():
    return render_template("admin_home.html")


@admin.route('/viewuser')
def viewuser():
    data={}
    qry="select * from user"
    res = select(qry)
    if res:
        data['view']=res
    return render_template("viewuser.html",data=data)


@admin.route('/complaints')
def complaints():
    data={}
    qry="SELECT * FROM `complaints` INNER JOIN `user` USING(user_id)"
    res = select(qry)
    if res:
        data['view'] = res
    return render_template("viewcomp.html",data=data)

@admin.route('/admin_send_reply' ,methods=['POST','GET'])
def admin_send_reply():
    id=request.args['id']
    if 'submit' in request.form:
        reply=request.form['reply']
        a="update complaints set reply='%s' where complaint_id='%s'"%(reply,id)
        b=update(a)
        if b:
            return '''<script>alert("Reply Send Successfully");window.location='/complaints'</script>'''

    return render_template('admin_send_reply.html')


@admin.route('/notification',methods=['POST','GET'])
def notification():
    if 'submit' in request.form:
        title=request.form['title']
        description=request.form['desc']
        qry="insert into notification values(null,'%s','%s',curdate())"%(title,description)
        res=insert(qry)
        if res:
            return '''<script>alert("Notification Send Successfully");window.location='/notification'</script>'''
        
    return render_template("notification.html")


