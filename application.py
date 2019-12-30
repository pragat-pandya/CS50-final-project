import os

# cs50's SQL module to access database and manipulate in within application.py file
from cs50 import SQL

# importing various flask modules as needed
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

# importing WSGI library componetns to convert passwords to hashes and vice verca
from werkzeug.security import check_password_hash, generate_password_hash


# intializing Flask webapp
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///portal.db")


# The default route AKA home-page
@app.route("/")
def get_index():
    return render_template("index.html")


# Bloglist rendering controller code!
@app.route("/blogs")
def blogs():
    """
    This method will fetch the list of all the blogs from the Table-blogs in database
    and will render the view that consist of the list of all blogs

    """

    # Loads all the titles from blogs table into a python datatype
    bloglist = db.execute("SELECT * FROM Blogs")

    # Returns the blog.html template injecting the data-objects titles and intros
    return render_template("blog.html", bloglist=bloglist)



@app.route("/blogs/<parm>")
def blogloader(parm):

    """
    This method's purpose in life is to render template which will consist the blog-post as a whole!
    This method takes a parameter : "parm" which will always be the title of the blog on which the user has clicked!

    """

    # This line of code will select all the columns for the blog on which the user has clicked from /blogs
    blogdata = db.execute("SELECT * FROM Blogs WHERE blog_title=:title", title=parm)
    return render_template("blogcore.html", blogdata=blogdata)


@app.route("/login", methods=["GET","POST"])
def login():
    """
    login portal for admin to manage certain activities on the portal

    """

    return render_template("login.html")



#The following route was used in development to register admins
#@app.route("/register", methods=["POST"])
#def register():

    # if from submission is replicated using a GET request then redirect to the login page
 #   if request.method == "GET":
 #       return redirect("/login")

  #  if request.method == "POST":

        # checking if any required form field is left blank on the time of sumission!
   #     if not request.form.get("name") or not request.form.get("password") or not request.form.get("role"):
    #        return "Please Fill-Out all the required form fields!"

        # if that's not the case then move on to adding the user to the admin table
#        else:
 #           user= request.form.get("name")
  #          pwd = generate_password_hash(request.form.get("password"))
   #         role = request.form.get("role")
            # insert the admin data into the table ADMINS
    #        db.execute("INSERT into Admin(admin_name,admin_hash,admin_role) VALUES (:admin_name,:admin_hash,:admin_role)",
      #                  admin_name=user, admin_hash=pwd, admin_role=role)
     #       return "Registered Successfully"

@app.route("/blogadder", methods=["POST"])
def blogadder():

    # If form submission is replicated by a get request then the submission should not be accepted!
    if request.method == "GET":
        redirect("/login")

    # If the form submission is genuen then move on to verifing credentials!
    else:

        # Placeholders for the data which is collected from form submission
        user = request.form.get("name")
        pwd = request.form.get("password")
        role = request.form.get("role")

        # Selecting the row matching the username form the admin table
        admin = db.execute("SELECT * FROM Admin WHERE admin_name=:name", name=user)

        if user == admin[0]['admin_name'] and check_password_hash(admin[0]['admin_hash'], pwd):
            return render_template("blogadder.html")
        else:
            redirect("/login")

@app.route("/published", methods=["POST"])
def blog_publish():
    if request.method == "GET":
        redirect("/blogadder")

    else:
        # Place holder for the data collected from the form fields
        title = request.form.get("blog-title")
        intro = request.form.get("blog-intro")
        body = request.form.get("blog-body")

        # Inserting the data into the database table  : Blogs as this is the content for a new blog!
        db.execute("INSERT into Blogs(blog_title,brief_intro,blog_body) VALUES (:title,:intro,:body)"
                    ,title=title, intro=intro, body=body)

        return "NEW BLOG PUBLISHED SUCCESSFULLY!"

@app.route("/", methods=["POST"])
def contact():
    if request.method == "GET":
        redirect("/")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        db.execute("INSERT into Contact(cont_name,cont_email,cont_subject,cont_message) VALUES (:cont_name,:cont_email,:cont_subject,:cont_message)",
                    cont_name=name,cont_email=email,cont_subject=subject,cont_message=message)
        flash("You've successfully sent a message to Pragat!")
        return redirect(url_for('get_index'))


app.route("/tutorials")
def tutorial():
    return render_template("tuts.html")