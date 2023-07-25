# import os
# from flask import Flask, render_template, request,redirect, url_for, session
# from newsapi import NewsApiClient
# from flask_mail import Mail, Message
# import ibm_db
# import re
# # init flask app
# app = Flask(__name__)
# app.secret_key = 'a'
# conn= ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=nkk12877;PWD=UUGFBq21gm6EiMIz",'','')
  

# newsapi = NewsApiClient(api_key='70fdb9ba81ba40b6bda148e672898bd9')
  

# def get_sources_and_domains():
#     all_sources = newsapi.get_sources()['sources']
#     sources = []
#     domains = []
#     for e in all_sources:
#         id = e['id']
#         domain = e['url'].replace("http://", "")
#         domain = domain.replace("https://", "")
#         domain = domain.replace("www.", "")
#         slash = domain.find('/')
#         if slash != -1:
#             domain = domain[:slash]
#         sources.append(id)
#         domains.append(domain)
#     sources = ", ".join(sources)
#     domains = ", ".join(domains)
#     return sources, domains

# @app.route('/login',methods =['GET', 'POST'])
# def login():
#     global userid
#     msg = ''
   
  
#     if request.method == 'POST' :
#         username = request.form['username']
#         password = request.form['password']
#         sql = "SELECT * FROM users WHERE username =? AND password=?"
#         stmt = ibm_db.prepare(conn, sql)
#         ibm_db.bind_param(stmt,1,username)
#         ibm_db.bind_param(stmt,2,password)
#         ibm_db.execute(stmt)
#         account = ibm_db.fetch_assoc(stmt)
#         print (account)
#         if account:
#             session['loggedin'] = True
#             session['id'] = account['USERNAME']
#             userid=  account['USERNAME']
#             session['username'] = account['USERNAME']
#             msg = 'Logged in successfully !'
            
#             msg = 'Logged in successfully !'
#             return redirect(url_for('home'))  
#         else:
#             msg = 'Incorrect username / password !'
#     return render_template('login.html', msg = msg)

        

   
# @app.route('/register', methods =['GET', 'POST'])
# def register():
#     msg = ''
#     if request.method == 'POST' :
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         sql = "SELECT * FROM users WHERE username =?"
#         stmt = ibm_db.prepare(conn, sql)
#         ibm_db.bind_param(stmt,1,username)
#         ibm_db.execute(stmt)
#         account = ibm_db.fetch_assoc(stmt)
#         print(account)
#         if account:
#             msg = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address !'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             msg = 'name must contain only characters and numbers !'
#         else:
#             insert_sql = "INSERT INTO  users VALUES (?, ?, ?)"
#             prep_stmt = ibm_db.prepare(conn, insert_sql)
#             ibm_db.bind_param(prep_stmt, 1, username)
#             ibm_db.bind_param(prep_stmt, 2, email)
#             ibm_db.bind_param(prep_stmt, 3, password)
#             ibm_db.execute(prep_stmt)
#             msg = 'You have successfully registered !'
#             app.config['SECRET_KEY'] = 'top-secret!'
#             app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
#             app.config['MAIL_PORT'] = 587
#             app.config['MAIL_USE_TLS'] = True
#             app.config['MAIL_USERNAME'] = 'apikey'
#             app.config['MAIL_PASSWORD'] = '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'
#             app.config['MAIL_DEFAULT_SENDER'] = 'vigneshbit2019@citchennai.net'
#             mail = Mail(app)
#             recipient = request.form['email']
#             msg = Message('Successfully Registered', recipients=[recipient])
#             msg.body = ('Congratulations! You have successfully registered with '
#                     'NewsApp!')
#             msg.html = ('<h1>Successfully Registered</h1>'
#                     '<p>Congratulations! You have successfully registered with '
#                     '<b>NewsApp</b>!</p>')
#             mail.send(msg)
#             return redirect(url_for('login'))
#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     return render_template('login-register.html', msg = msg)


# @app.route("/", methods=['GET', 'POST'])
# def home():
#     if request.method == "POST":
#         sources, domains = get_sources_and_domains()
#         keyword = request.form["keyword"]
#         related_news = newsapi.get_everything(q=keyword,
#                                       sources=sources,
#                                       domains=domains,
#                                       language='en',
#                                       sort_by='relevancy')
#         no_of_articles = related_news['totalResults']
#         if no_of_articles > 100:
#             no_of_articles = 100
#         all_articles = newsapi.get_everything(q=keyword,
#                                       sources=sources,
#                                       domains=domains,
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page_size = no_of_articles)['articles']
#         return render_template("home.html", all_articles = all_articles, 
#                                keyword=keyword)
#     else:
#         top_headlines = newsapi.get_top_headlines(country="in", language="en")
#         total_results = top_headlines['totalResults']
#         if total_results > 100:
#             total_results = 100
#         all_headlines = newsapi.get_top_headlines(country="in",
#                                                      language="en", 
#                                                      page_size=total_results)['articles']
#         return render_template("home.html", all_headlines = all_headlines)
#     return render_template("home.html")
  
# if __name__ == "__main__":
#     app.run(debug = True)

import os
from flask import Flask, render_template, request, redirect, url_for, session
from newsapi import NewsApiClient
from flask_mail import Mail, Message
import mysql.connector
import re

# init flask app
app = Flask(__name__)
app.secret_key = 'a'

# connect to mysql database
cnx = mysql.connector.connect(user='root',
                              password='Vkt@098',
                              host='127.0.0.1',
                              database='ibm')

newsapi = NewsApiClient(api_key='57c9c4d80d62479c8c13b744394e0374')

def get_sources_and_domains():
    all_sources = newsapi.get_sources()['sources']
    sources = []
    domains = []
    for e in all_sources:
        id = e['id']
        domain = e['url'].replace("http://", "")
        domain = domain.replace("https://", "")
        domain = domain.replace("www.", "")
        slash = domain.find('/')
        if slash != -1:
            domain = domain[:slash]
        sources.append(id)
        domains.append(domain)
    sources = ", ".join(sources)
    domains = ", ".join(domains)
    return sources, domains

@app.route('/login', methods=['GET', 'POST'])
def login():
    global userid
    msg = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM IbmUser WHERE uname=%s AND pswd=%s"
        cursor.execute(query, (username, password))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['uname']
            userid = account['uname']
            session['username'] = account['uname']
            msg = 'Logged in successfully !'
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM IbmUser WHERE uname=%s"
        cursor.execute(query, (username,))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Name must contain only characters and numbers !'
        else:
            insert_sql = "INSERT INTO IbmUser VALUES (%s, %s, %s)"
            cursor.execute(insert_sql, (username, email, password))
            cnx.commit()
            msg = 'You have successfully registered !'
            app.config['SECRET_KEY'] = 'top-secret!'
            app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
            app.config['MAIL_PORT'] = 587
            app.config['MAIL_USE_TLS'] = True
            app.config['MAIL_USERNAME'] = 'apikey'
            app.config['MAIL_PASSWORD'] = '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'
            app.config['MAIL_DEFAULT_SENDER'] = 'vigneshbit2019@citchennai.net'
            mail = Mail(app)
            recipient = request.form['email']
            msg = Message('Successfully Registered', recipients=[recipient])
            msg.body = ('Congratulations! You have successfully registered with '
                    'NewsApp!')
            msg.html = ('<h1>Successfully Registered</h1>'
                    '<p>Congratulations! You have successfully registered with '
                    '<b>NewsApp</b>!</p>')
            mail.send(msg)
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('login-register.html', msg = msg)


@app.route("/main", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        sources, domains = get_sources_and_domains()
        keyword = request.form["keyword"]
        related_news = newsapi.get_everything(q=keyword,
                                      sources=sources,
                                      domains=domains,
                                      language='en',
                                      sort_by='relevancy')
        no_of_articles = related_news['totalResults']
        if no_of_articles > 100:
            no_of_articles = 100
        all_articles = newsapi.get_everything(q=keyword,
                                      sources=sources,
                                      domains=domains,
                                      language='en',
                                      sort_by='relevancy',
                                      page_size = no_of_articles)['articles']
        return render_template("home.html", all_articles = all_articles, 
                               keyword=keyword)
    else:
        top_headlines = newsapi.get_top_headlines(country="in", language="en")
        total_results = top_headlines['totalResults']
        if total_results > 100:
            total_results = 100
        all_headlines = newsapi.get_top_headlines(country="in",
                                                     language="en", 
                                                     page_size=total_results)['articles']
        return render_template("home.html", all_headlines = all_headlines)
    return render_template("home.html")
  
if __name__ == "__main__":
    app.run(debug = True)
