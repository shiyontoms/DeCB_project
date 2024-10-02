from flask import *
public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template("home.html")

@public.route('/login',methods=['POST','GET'])
def login():
    if 'login' in request.form:
        loginid=request.form['loginid']
        username=request.form['uname']
        usertype=request.form['usertype']
        password=request.form['psw']
        print(loginid,username,usertype,password)
    return render_template("login.html")

@public.route('/register',methods=['POST','GET'])
def register():
    if 'submit' in request.form:
        name=request.form['name']
        email=request.form['mail']
        phno=request.form['phno']
        username=request.form['username']
        password=request.form['pass']


        qry="insert into login values(null,'%s','%s','user')"%(username,password)
        res=insert(qry)
        qry1="insert into register values(null,'')"
    return render_template("register.html")
