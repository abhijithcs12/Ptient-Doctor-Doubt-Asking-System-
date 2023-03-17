from flask import *
from database import DB,CR
from datetime import datetime

patient = Blueprint("patient",__name__)

@patient.route("/Patienthome",methods =["POST","GET"])
def Patienthome():
    CR.execute("SELECT * FROM qanda")
    res = CR.fetchall()
    return render_template('patienthome.html',res = res)

@patient.route("/askquestion",methods = ["post",'get'])
def Askquestion():
    if "submit" in request.form:
        question = request.form['question']
        date = datetime.now()
        sql = 'INSERT INTO qanda (Question,Date) VALUES (%s,%s)' 
        val = (question,date)
        CR.execute(sql,val)
        DB.commit()
        flash("Question submitted")
        return redirect(url_for('patient.Patienthome'))
        
    return render_template('askquestion.html')

@patient.route("/view")
def View():
    CR.execute("SELECT * FROM qanda")
    res=CR.fetchall()
    return render_template("view.html",res=res)
    