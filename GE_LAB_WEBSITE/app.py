from flask import Flask, render_template,request,redirect
from usermanagement import user_management

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

## User Management
@app.route("/create_user",methods = ["POST"])
def create_user():
    username = request.form.get('Username_')
    role = request.form.get('Role_')
    email = request.form.get('Email_')
    password = request.form.get('Password_')

    condition = user_management.add_user(username,role,email,password)

    return redirect("/returnhome")


@app.route("/check_user",methods = ["POST"])
def check_user():
    
    email = request.form.get('Email_')
    password = request.form.get('Password_')
    condition = user_management.check_user(email,password)

    if(condition):

        return redirect("/workspace")
    else:
        return redirect("/failure")


## Change Page
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

@app.route("/loginpage")
def loginpage():
    return render_template("loginpage.html")

@app.route("/signuppage")
def signuppage():
    return render_template("signuppage.html")

@app.route("/returnhome")
def returnhome():
    return render_template("index.html")