from threading import Thread
import json
import socket

from flask import request, render_template, make_response, jsonify, Flask
from werkzeug.utils import redirect

from helpers_sql.SqlRequest import SqlRequest

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
s = socket.socket()
host = "127.0.0.1"
port = 5409
connected = False


def getFromDatabase(sqlRequest: SqlRequest):
    msg = sqlRequest.getInstance().content
    global connected
    message = bytes(msg, "utf-8")
    if connected is False:
        s.connect((host, port))
        connected = True
    s.send(message)
    msgRcvd = ""
    results = []
    while msgRcvd == "":
        try:
            msgRcvd = s.recv(1024)
            results = json.loads(msgRcvd)
        except:
            pass

    return results


@app.route('/addcli', methods=['POST', 'GET'])
def addcli():
    if request.method == 'POST':
        name = request.form['nm']
        iden = request.form['id']
        city = request.form['city']
        postcode = request.form['postcode']
        nip = int(request.form['nip'])
        SqlRequest.getInstance().content = "INSERT INTO customers VALUES (%s, '%s', '%s', '%s', %d)" % (
            iden, name, city, postcode, nip)
        results = getFromDatabase(SqlRequest.getInstance())

        return redirect('/ClientList')


@app.route('/confirmOrder', methods=['POST', 'GET'])
def confirmOrder():
    if request.method == 'POST':
        productSelected = request.form['prodSel']
        value = request.form['count']
        factorySelected = request.form['factSel']
        client = request.form['cli']
        SqlRequest.getInstance().content = "GetOrdersList"
        results = getFromDatabase(SqlRequest.getInstance())

        iden = max(element[0] for element in results) + 1
        SqlRequest.getInstance().content = "INSERT INTO orders VALUES (%s, '%s', '%s', '%s', '%s')" % (iden, client,
                                                                                                       productSelected,
                                                                                                       value,
                                                                                                       factorySelected)
        results = getFromDatabase(SqlRequest.getInstance())
        return redirect('/OrdersList')


@app.route('/makeOrder', methods=['POST'])
def makeOrder():
    if request.method == 'POST':
        productSelected = request.form['prodSel']
        value = request.form['count']
        client = request.form['cli']
        SqlRequest.getInstance().content = \
            "SELECT DISTINCT factories.name FROM factories JOIN products ON factories.id =" \
            " products.factory WHERE products.name = '%s'" % productSelected
        results = getFromDatabase(SqlRequest.getInstance())
        return render_template('selectFactory.html', data=[results, value, productSelected, client])


@app.route('/delete/<string:tab>/<int:id>', methods=['GET'])
def delete(tab, id):
    SqlRequest.getInstance().content = \
        "DELETE FROM %s WHERE id = '%s'" % (tab, id)
    getFromDatabase(SqlRequest.getInstance())

    return redirect('/')


@app.route('/TemplateForm', methods=['POST', 'GET'])
def templateForm():
    template = request.form['fab']
    results = []
    if str(template).__contains__("towar"):
        SqlRequest.getInstance().content = "SELECT orders.productName FROM orders GROUP BY orders.productName " \
                                           "ORDER BY Count(orders.productName) ASC LIMIT 1"
        resultsTop = getFromDatabase(SqlRequest.getInstance())
        SqlRequest.getInstance().content = "SELECT * FROM products GROUP BY name"
        results = getFromDatabase(SqlRequest.getInstance())
        SqlRequest.getInstance().content = "GetClientList"
        resultsClient = getFromDatabase(SqlRequest.getInstance())
        items = []

        for item in resultsClient:
            items.append(item[1])

        return render_template('addOrderTopProduct.html', data=[results, items, resultsTop])

    elif str(template).__contains__("klient"):
        SqlRequest.getInstance().content = "SELECT orders.clientName FROM orders GROUP BY orders.clientName " \
                                           "ORDER BY Count(orders.clientName) DESC LIMIT 1"
        resultsTop = getFromDatabase(SqlRequest.getInstance())
        SqlRequest.getInstance().content = "SELECT * FROM products GROUP BY name"
        results = getFromDatabase(SqlRequest.getInstance())
        SqlRequest.getInstance().content = "GetClientList"
        resultsClient = getFromDatabase(SqlRequest.getInstance())
        items = []

        for item in resultsClient:
            items.append(item[1])
        return render_template('addOrderTopClient.html', data=[results, items, resultsTop])

    return render_template('Index.html')


@app.route('/addFact', methods=['POST', 'GET'])
def addFact():
    if request.method == 'POST':
        name = request.form['nm']
        iden = request.form['id']

        SqlRequest.getInstance().content = "INSERT INTO factories VALUES (%s, '%s')" % (iden, name)
        results = getFromDatabase(SqlRequest.getInstance())

        return redirect('/FactoriesList')


@app.route('/addpro', methods=['POST', 'GET'])
def addpro():
    if request.method == 'POST':
        name = request.form['nm']
        iden = request.form['id']
        facName = request.form['fab']

        SqlRequest.getInstance().content = "SELECT * FROM factories WHERE name='%s'" % facName
        results = getFromDatabase(SqlRequest.getInstance())

        SqlRequest.getInstance().content = "INSERT INTO products VALUES (%s, '%s', %s)" % (iden, name, results[0][0])
        results = getFromDatabase(SqlRequest.getInstance())

        return redirect('/ProductsList')


@app.route("/AddClient")
def addClient():
    SqlRequest.getInstance().content = "GetClientList"
    results = getFromDatabase(SqlRequest.getInstance())
    maxim = max(element[0] for element in results) + 1
    return render_template('addClient.html', data=maxim)


@app.route("/AddFactory")
def addFactory():
    SqlRequest.getInstance().content = "GetFactoriesList"
    results = getFromDatabase(SqlRequest.getInstance())
    maxim = max(element[0] for element in results) + 1
    return render_template('addFactory.html', data=maxim)


@app.route("/AddProduct")
def addProduct():
    SqlRequest.getInstance().content = "GetProductsList"
    results = getFromDatabase(SqlRequest.getInstance())
    maxim = max(element[0] for element in results) + 1

    SqlRequest.getInstance().content = "GetFactoriesList"
    results = getFromDatabase(SqlRequest.getInstance())

    return render_template('addProduct.html', data=[maxim, results])


@app.route("/AddOrder")
def AddOrder():
    SqlRequest.getInstance().content = "SELECT * FROM products GROUP BY name"
    results = getFromDatabase(SqlRequest.getInstance())
    SqlRequest.getInstance().content = "GetClientList"
    resultsClient = getFromDatabase(SqlRequest.getInstance())
    items = []
    for item in resultsClient:
        items.append(item[1])

    return render_template('addOrder.html', data=[results, items])


@app.route("/Statistics")
def statistics():
    SqlRequest.getInstance().content = "SELECT Count(orders.clientName), orders.clientName FROM orders GROUP BY orders.clientName"
    orders = getFromDatabase(SqlRequest.getInstance())
    xs = [order[1] for order in orders]
    ys = [order[0] for order in orders]

    return render_template('statistics.html', data=[xs, ys, "Liczba zamówień"])


@app.route("/")
def index():
    return render_template('welcome.html')


def passToChart(text):
    orders = getFromDatabase(SqlRequest.getInstance())
    xs = [order[1] for order in orders]
    ys = [order[0] for order in orders]
    return make_response(jsonify([xs, ys, text]))


@app.route("/data/clientsCount", methods=['POST'])
def clientsCount():
    SqlRequest.getInstance().content = "SELECT Count(orders.clientName), orders.clientName FROM orders GROUP BY orders.clientName"
    return passToChart('Liczba zamówień przez klientów')


@app.route("/data/productsCount", methods=['POST'])
def productsCount():
    SqlRequest.getInstance().content = "SELECT Count(orders.id), orders.productName FROM orders GROUP BY orders.productName"
    return passToChart('Liczba zamówień produktów')


@app.route("/data/productsSum", methods=['POST'])
def productsSum():
    SqlRequest.getInstance().content = "SELECT Sum(orders.value), orders.productName FROM orders GROUP BY orders.productName"
    return passToChart('Suma zamówionych produktów')


@app.route("/data/factoryCount", methods=['POST'])
def factoryCount():
    SqlRequest.getInstance().content = "SELECT Count(orders.id), orders.factoryName FROM orders GROUP BY orders.factoryName"
    return passToChart('Liczba zamówień w fabrykach')


@app.route("/data/factorySum", methods=['POST'])
def factorySum():
    SqlRequest.getInstance().content = "SELECT Sum(orders.value), orders.factoryName FROM orders GROUP BY orders.factoryName"
    return passToChart('Suma zamówień w fabrykach')


@app.route("/Orders")
def ordersSection():
    return render_template('ordersSection.html')


@app.route("/ProductsList")
def productsList():
    SqlRequest.getInstance().content = "GetProductsList"
    results = getFromDatabase(SqlRequest.getInstance())
    return render_template('productsList.html', data=results)


@app.route("/FactoriesList")
def factoriesList():
    SqlRequest.getInstance().content = "GetFactoriesList"
    results = getFromDatabase(SqlRequest.getInstance())
    return render_template('factoriesList.html', data=results)


@app.route("/OrdersList")
def ordersList():
    SqlRequest.getInstance().content = "GetOrdersList"
    results = getFromDatabase(SqlRequest.getInstance())
    return render_template('ordersList.html', data=results)


@app.route("/ClientList")
def clientList():
    SqlRequest.getInstance().content = "GetClientList"
    results = getFromDatabase(SqlRequest.getInstance())
    return render_template('clientList.html', data=results)


def runApp():
    app.run(host='0.0.0.0', port=8888)


if __name__ == '__main__':
    Thread(target=runApp()).start()
