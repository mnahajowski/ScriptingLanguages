import threading
import json
import socket
import shutil
import sqlite3

from flask import render_template, request, Flask
from werkzeug.utils import redirect

conn = sqlite3.connect('db/mainDatabase.db')
s = socket.socket()
host = "127.0.0.1"
port = 5409
s.bind((host, port))
s.listen(1)
app = Flask(__name__)


@app.route("/")
def index():
    with sqlite3.connect("db/mainDatabase.db") as con:
        c = con.cursor()
        c.execute("""SELECT * FROM customers""")
        result = c.fetchall()
        return render_template('serverDashboard.html', data=result)


@app.route('/copyDatabase', methods=['POST'])
def copyDatabase():
    if request.method == 'POST':
        shutil.copy2('db/mainDatabase.db', 'mainDatabaseCopy.db')
        return redirect('/')


@app.route('/delete/<string:tab>', methods=['GET'])
def deleteTableContent(tab):
    with sqlite3.connect("db/mainDatabase.db") as con:
        c = con.cursor()
        c.execute("""DELETE * FROM %s""" % tab)
        c.fetchall()
        con.commit()
        return redirect('/')


def chooseStrategy(a, msg: bytes, con) -> str:
    if msg.decode("utf-8") == "GetClientList":
        a.execute("""SELECT * FROM customers""")
    elif msg.decode("utf-8") == "GetFactoriesList":
        a.execute("""SELECT * FROM factories""")
    elif msg.decode("utf-8") == "GetOrdersList":
        a.execute("""SELECT * FROM orders""")
    elif msg.decode("utf-8") == "GetProductsList":
        a.execute("""SELECT p.id, p.name, factories.name
                FROM products p
                JOIN factories ON factories.id = p.factory""")
    else:
        try:
            a.execute(msg.decode("utf-8"))
            result = a.fetchall()
            con.commit()
            return result
        except Exception as e:
            con.rollback()
        finally:
            if result is []:
                return "Other operation"

    result = a.fetchall()
    return result


def listen():
    while True:
        c, addr = s.accept()
        while True:
            try:
                msg = c.recv(1024)
                with sqlite3.connect("db/mainDatabase.db") as con:
                    a = con.cursor()
                    result = chooseStrategy(a, msg, con)
                    data = json.dumps(result)
                    c.send(bytes(data, "utf-8"))
            except:
                pass


def runApp():
    app.run(host='0.0.0.0', port=12345)


if __name__ == '__main__':
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=runApp)
    t1.start()
    t2.start()
