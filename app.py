from flask import Flask, render_template, request, redirect, url_for, session,abort
from mysqlconn import mydb
import os

app = Flask (__name__)

app.secret_key = 'abcde'


@app.route ('/')
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

        if result:
            session['loggedin'] = True
            session['id'] = result[0]
            session['username'] = result[1]
            return redirect(url_for('dashboard',id = session['id'] ))
        else:
            msg = 'Incorrect username / password !'

    return render_template ("login.html", msg=msg)


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


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login' ))


@app.route('/page-not-found')
def page_not_found():
    return render_template ("404.html")


@app.route ('/dashboard/<id>', methods=['GET', 'POST'])
def dashboard(id):

    if session.get('loggedin') is None:
        #redirect(url_for('login'))
        abort(401)

    if int(id) != session['id']:
        print(id,session['id'])

        abort (404)
        #redirect(url_for('page_not_found' ))

    if request.method == 'POST':
        file = request.files['pdf']
        name = file.filename
        file.save(os.path.join('static/pdf', name))
        cur = mydb.cursor()
        sql = "INSERT INTO documents (name,owner_id) VALUES (%s, %s)"
        val = (name,  id)
        cur.execute (sql, val)
        mydb.commit ()
        redirect (url_for('dashboard', id = session['id'] ) )

    cur = mydb.cursor ()
    sql = "select * from documents join user where owner_id =uid and owner_id = "+ str(id)
    cur.execute (sql)
    result = cur.fetchall()

    return render_template ("index.html", id=id, result = result)


@app.route ('/company/<id>', methods=['GET', 'POST'])
def company(id):

    if session.get('loggedin') is None:
        #redirect(url_for('login'))
        abort(401)

    if int(id) != session['id']:
        print(id,session['id'])

        abort (404)
        #redirect(url_for('page_not_found' ))

    cur = mydb.cursor ()
    sql = "SELECT * FROM `documents` join user where `owner_id`= uid and company = (select company from user where " \
          "uid =" + id + ') '
    cur.execute(sql)
    result = cur.fetchall()

    return render_template ("company.html", id=id, result = result)


@app.route ('/dashboard/<id>/<did>', methods=['GET', 'POST'])
def viewer(id, did):
    if session.get ('loggedin') is None:
        # redirect(url_for('login'))
        abort (401)

    if int (id) != session['id']:
        print (id, session['id'])

        abort (404)
        # redirect(url_for('page_not_found' ))

    cur = mydb.cursor ()
    sql = "select name from documents where did = " + str(did)
    cur.execute (sql)
    result = cur.fetchone ()

    if request.method == 'POST':
        comment = request.form['message']
        cur = mydb.cursor()
        sql = "INSERT INTO comments (doc_id,user_id,comment) VALUES (%s, %s,%s)"
        val = (did, id,  comment)
        cur.execute (sql, val)
        mydb.commit ()
        redirect(url_for('dashboard',id = session['id'] ,did =did))

    cur = mydb.cursor ()
    sql = "select * from comments join user where user_id = uid and doc_id = " + str(did)
    cur.execute (sql)
    result2 = cur.fetchall ()
    print (result2)

    return render_template ("viewer.html", id=id, pname=result[0], did=did,result2=result2,length = len(result2))


if __name__ == "__main__":
    app.run (debug=True)
