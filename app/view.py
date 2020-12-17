#####################################################################################
########################  THIS FILE(view.py) CONTAINS THE USER INTERFACE  ################################################
#######################################################################################

from app import app, mongo #this means from the app folder(which calls on the __init__.py file in the app folder) import the flask init(i.e app = Flask(__name__)) 
import re, time, datetime, uuid, os
from flask import request, render_template, flash, redirect, url_for, session,logging 
from passlib.hash import sha256_crypt
from functools import wraps


app.secret_key = os.urandom(24)

# #CHECK IF USER IS LOGGED IN (DECORATOR)
# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         # if "email" in session == "emeka@gmail.com":
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized, Please login','danger')
#             return redirect(url_for("login"))
#     return wrap

#####################################################################################
########################   FUNCTION  ################################################
#######################################################################################
#displays year
year = datetime.date.today().year

#function that displays Nigerian time.
def nigerian_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    today = datetime.date.today()
    d2 = today.strftime("%B %d, %Y")
    tm = now.strftime("%H:%M:%S")
    return (d2 +' '+'at'+' '+tm)


#####################################################################################
########################   ENDPOINTS  ################################################
#######################################################################################
#homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=='POST':
        #get form fields
        reg_id=request.form['registration_id']
        print(reg_id)
        frequency=request.form['frequency']
        print(frequency)
        fees_to_pay=request.form.getlist('fees_to_pay')
        print(fees_to_pay)
        
        #call an api to save the data
        

        flash("Payment details recorded sucessfully.")
        return render_template("index.html", title="Home | Pay School Fees", home="active", year=year)

    #if the method is GET
    else:
        return render_template("index.html", title="Home | Pay School Fees", home="active", year=year)

