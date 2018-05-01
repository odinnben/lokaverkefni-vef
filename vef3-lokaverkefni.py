from bottle import *
#from pymysql import *

@route("/")
def index():
    return template("index")

@route('/css/<filename>')
def static_server(filename):
    return static_file(filename, root=('./css'))
run()