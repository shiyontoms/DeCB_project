from flask import *
from database import*
public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template("home.html")

@public.route('/login',methods=['POST','GET'])
def login():
    if 'submit' in request.form:
        username=request.form['uname']
        password=request.form['passw']

        qry = "select * from login where username='%s' and password='%s'"%(username,password)
        res = select(qry)

        if res:
            session['log']= res[0]['login_id']

        if res[0]['usertype']=='admin':
            return redirect(url_for('admin.admin_home'))        
        
    return render_template("login.html")




@public.route('/user_register',methods=['POST','GET'])
def user_register():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['mail']
        phno=request.form['phno']
        username=request.form['uname']
        password=request.form['passw']


        qry="insert into login values(null,'%s','%s','user')"%(username,password)
        res=insert(qry)


        qry1="insert into user values(null,'%s','%s','%s','%s')"%(res,fname,lname,phno,email)
        insert(qry1)

    return render_template("registration.html")



