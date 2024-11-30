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

# @public.route('/register',methods=['POST','GET'])
# def register():
#     if 'submit' in request.form:
#         name=request.form['name']
#         email=request.form['mail']
#         phno=request.form['phno']
#         username=request.form['username']
#         password=request.form['pass']


#         qry="insert into login values(null,'%s','%s','user')"%(username,password)
#         res=insert(qry)
#         qry1="insert into register values(null,'')"
#     return render_template("register.html")
