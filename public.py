from flask import *
from database import DB,CR

public = Blueprint("pulic",__name__)

@public.route("/",methods =["post",'get'] )
def Signin():
        if 'submit' in request.form:
         username = request.form["username"]
         password = request.form["password"]

         sql = "SELECT * FROM user WHERE username=%s AND password=%s"
         val = (username,password)
         CR.execute(sql,val)
         result = CR.fetchall()
         if result:
              if result:
                 if result[0]['Usertype'] == 'patient':
                     return redirect(url_for('patient.Patienthome'))

                 if result[0]['Usertype'] == 'doctor':
                     return redirect(url_for('doctor.Doctorhome'))  
                 return render_template('patienthome.html')
        else:
             flash("Username or password incorrect")    

        return render_template('login.html')

@public.route("/register",methods =["post",'get'])
def SignUp():
    if 'submit' in request.form:
             username = request.form['username']
             email = request.form['email']
             usertype = request.form["usertype"]
             password = request.form['password']

             sql ="SELECT * FROM user WHERE username=%s OR email=%s"
             val =(username,email)
             CR.execute(sql,val)
             result = CR.fetchall()

             if result:
                 flash("username or Emailid  exists")
             else:
                 sql = 'INSERT INTO user (username,email,password,usertype) VALUES (%s,%s,%s,%s)'
                 val = (username,email,password,usertype)
                 CR.execute(sql,val)
                 DB.commit()
                 return render_template('login.html')
        
    return render_template('register.html') 
@public.route("/logout")
def logout():
    return redirect(url_for("pulic.Signin"))
