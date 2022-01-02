from flask import Flask, render_template,request,redirect
import helper_fxns

app = Flask(__name__)

#Declare Globals
input_list = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check_user",methods = ["POST"])
def check_user():
    
    username = request.form.get('Username_')
    password = request.form.get('Password_')
    condition = helper_fxns.check_user(username,password)

    if(condition):

        return redirect("/workspace")
    else:
        return redirect("/failure")



@app.route("/workspace")
def workspace():
    return render_template("workspace.html")

@app.route("/failure")
def failure():
    return render_template("failure.html")



@app.route("/work_in_progress")
def work_in_progress():
    return render_template("work_in_progress.html")

@app.route("/project")
def project():
    return render_template("project.html")