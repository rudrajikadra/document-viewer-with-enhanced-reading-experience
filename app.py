from flask import Flask, render_template, request, redirect, url_for, session, abort, jsonify
from mysqlconn import mydb
from datetime import date
from pdfToSummary import pdfToSummary as ps
from pdfToURLS import pdfToUrls as pu
from urlToPDF import urlToPDF as up
from highlight import highlightOnPDF as hi
import os, json


app = Flask (__name__)

app.secret_key = 'secret'

# Deault Redirect to Home page of the website that is index.html
@app.route ('/')
@app.route ('/index')
def index():
    return render_template ("index.html")

# Redirect of services link to service.html page
@app.route ('/services')
def services():
    return render_template ("service.html")


# Redirect of pricing link to pricing.html page
@app.route ('/pricing')
def pricing():
    return render_template ("pricing.html")


# Redirect of Contact Us link to contact.html page
@app.route ('/contact')
def contact():
    return render_template ("contact.html")


# Implementing login route for Get and Post request to login the customer with their id and password
@app.route ('/login', methods=['GET', 'POST'])
def login():

    msg = ""
    if request.method == 'POST' and 'uname' in request.form and 'pass' in request.form:
        uname = request.form['uname']
        password = request.form['pass']

        cur = mydb.cursor ()
        sql = "select * from user where uname = %s and pass = %s"
        val = (uname, password)
        cur.execute (sql, val)
        result = cur.fetchone ()

        # print(result)
        
        # When the user is successfully loggedin, create a sessions  variable with the user contents \
        # that will be used throughout the user session interacting with the website.
        if result:
            session['loggedin'] = True
            session['id'] = result[0]
            session['highlight'] = False
            session['username'] = result[1]
            session['premium'] = result[4]
            return redirect(url_for('company',id = session['id'] ))
        else:
            msg = 'Incorrect username / password !'

    return render_template ("login.html", msg=msg)

# Implementing the register route for flask with Get and post request to register a new user with a valid company code.
@app.route ('/register', methods=['GET', 'POST'])
def signup():
    msg = ""
    if request.method == 'POST' and 'uname' in request.form and 'pass' in request.form:
        uname = request.form['uname']
        password = request.form['pass']
        password2 = request.form['pass2']
        company = request.form['comp']
        if password != password2:
            msg = "Passwords don't match"
            return render_template ("signup.html", msg=msg)
        else:
            cur = mydb.cursor ()
            sql = "INSERT INTO user (uname, pass,company) VALUES (%s, %s, %s)"
            val = (uname, password, company)
            cur.execute (sql, val)

            mydb.commit ()
            return redirect(url_for('login'))
    else:
        return render_template ("signup.html", msg=msg)


# Creating a logout route that clears out the session variables and redirects to the login page
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('highlight', None)
    session.pop('premium', None)
    return redirect(url_for('login' ))


# Redirect to page not found page upon bad url request
@app.route('/page-not-found')
def page_not_found():
    return render_template ("404.html")



# Implementing Dashboard (My Uploads) route that displays user uploads and let's user upload a pdf or submit a link that will be converted to pdf
@app.route ('/dashboard/<id>', methods=['GET', 'POST'])
def dashboard(id):

    if session.get('loggedin') is None:
        return redirect(url_for('login'))
        #abort(401)

    if int(id) != session['id']:
        #abort (404)
        return redirect(url_for('page_not_found' ))

    if request.method == 'POST':
        
        # If a pdf file is submitted then it will save the pdf to pdfs folder
        if request.files:
            file = request.files['pdf']
            name = file.filename
            if not os.path.exists ('static/pdf/'+name):
                file.save(os.path.join('static/pdf', name))

        # If a url is submitted then it will get the context of the url body convert into pdf then store that pdf to the pdfs folder
        elif request.form['urlfile']:
            urlfile = request.form['urlfile']
            name = up(str(urlfile))

        highLit = hi(name)
        
        summary = ps(name)
        url = json.dumps(pu(name))
        cur = mydb.cursor()

        # Insert the newly uploaded pdf to the database
        sql = "INSERT INTO documents (name,owner_id,summary,urls) VALUES (%s, %s,%s,%s)"
        val = (name,  id, summary, url)
        cur.execute (sql, val)
        mydb.commit ()

    cur = mydb.cursor ()
    sql = "select did,name,uname,summary from documents join user where owner_id =uid and owner_id = "+ str(id)
    cur.execute (sql)
    result = cur.fetchall()
    #print(result)

    return render_template ("dashboard.html", id=id, result = result)


# Implementing Company (My Team) route that displays all the pdfs that are uploaded by all team members of that particular team
@app.route ('/company/<id>', methods=['GET', 'POST'])
def company(id):

    if session.get('loggedin') is None:
        return redirect(url_for('login'))
        #abort(401)

    if int(id) != session['id']:
        #print(id,session['id'])

        #abort (404)
        return redirect(url_for('page_not_found' ))

    cur = mydb.cursor ()
    sql = "SELECT did,name,uname,summary FROM `documents` join user where `owner_id`= uid and company = (select " \
          "company from user where uid =" + id + ') '
    cur.execute(sql)
    result = cur.fetchall()

    return render_template("company.html", id=id, result = result)


# Redirect from documents when a user clicks on a particular pdf, get all the required data from the databse and pass it to the html file for diaply in viewer.html
@app.route ('/dashboard/<id>/<did>', methods=['GET', 'POST'])
def viewer(id, did):
    if session.get ('loggedin') is None:
        return redirect(url_for('login'))
        #abort (401)

    if int (id) != session['id']:
        #abort (404)
        return redirect(url_for('page_not_found' ))

    cur = mydb.cursor ()
    sql = "select * from documents where did = " + str(did)
    cur.execute(sql)
    result = cur.fetchone ()
    x = json.loads(result[4])

    # Insert a new discussion thread when a user posts a new comment
    if request.method == 'POST':

        comment = request.form['message']
        cur = mydb.cursor()
        sql = "INSERT INTO comments (doc_id,user_id,comment,date) VALUES (%s, %s,%s,%s)"
        val = (did, id,  comment,date.today())
        cur.execute (sql, val)
        mydb.commit ()
        #redirect(url_for('dashboard',id = session['id'] ,did =did))


    # Get all the necessary data to pass to the pdf viewer
    cur = mydb.cursor ()
    sql = "select cid,date,doc_id,user_id,comment,votes,uname from comments join user where user_id = uid and doc_id = " + str(did) + " ORDER BY votes Desc,date Asc;"
    cur.execute (sql)
    result2 = cur.fetchall ()
    #print (result2)

    cur = mydb.cursor ()
    sql = "select rid,cid,msg,date,uname from reply join user where usid = uid"
    cur.execute (sql)
    result3 = cur.fetchall ()
    #print(result3)

    cur = mydb.cursor ()
    sql = "select cidv,uidv,val,votes from vote join comments where cidv = cid and doc_id =" + did
    cur.execute (sql)
    result4 = cur.fetchall ()
    #print(result4)

    return render_template ("viewer.html", id=id, did=did,result = result,result2=result2,length = len(result2), result3=result3, result4=result4, urllist=x)


# Nested reply to discussion thread is stored in reply table in the database
@app.route ('/reply/<id>/<did>/<cid>', methods=['GET', 'POST'])
def reply(id, did,cid):

    if request.method == 'POST':
        rep= request.form['message2']
        cur = mydb.cursor()
        sql = "INSERT INTO reply (cid,usid,msg,date) VALUES (%s, %s,%s,%s)"
        val = (cid, id,  rep, date.today())
        cur.execute (sql, val)
        mydb.commit ()

    return redirect (url_for ('viewer', id=id, did=did))


# Voting system route for each discussion threads that will happen dynamically in the backgroynd using ajax in the html file
@app.route ('/vote', methods=['GET', 'POST'])
def vote():

    data = request.json
    uid = int(data['uid'])
    cid = int(data['cid'])
    value = data['val']
    cur = mydb.cursor ()
    sql = "INSERT INTO vote (uidv,cidv,val) VALUES (%s, %s,%s) ON DUPLICATE KEY UPDATE val = %s "
    val = (uid, cid, value, value)
    cur.execute(sql, val)
    mydb.commit()

    cur = mydb.cursor ()
    sql = "select count(*) from vote where val = -1 and cidv = "+str(cid)
    cur.execute (sql)
    result1 = cur.fetchone ()

    cur = mydb.cursor ()
    sql = "select count(*) from vote where val = 1 and cidv = "+str(cid)
    cur.execute (sql)
    result2 = cur.fetchone ()

    votes = result2[0] - result1[0]
    cur = mydb.cursor ()
    sql = "UPDATE comments set votes = %s where cid = %s"
    val = (votes, cid)
    cur.execute(sql, val)
    mydb.commit()

    return jsonify (data)


# Route for displaying Highlighted keywords in the pdf when the user clicks on show keywords highlights
@app.route ('/highlight/<id>/<did>', methods=['GET', 'POST'])
def highlight(id, did):
    print(session)
    if session['highlight']:
        session['highlight'] = False
    else:
        session['highlight'] = True

    return redirect (url_for ('viewer', id=id, did=did))


# This is where the magic happens
# Running the entire Flask Application
if __name__ == "__main__":
    app.run (debug=True)

