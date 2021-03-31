from math import isnan
from flask import Flask, json, render_template, request, redirect, session, jsonify
from flask_session import Session
from numpy.core.numeric import NaN
from werkzeug.wrappers import AuthorizationMixin
import yahoo_fin.stock_info as si
from datetime import datetime, timedelta

# Proceso para ejecutar la web app
# Lo mejor es que el fichero se llame app.py
# Indicarle a flask en el terminal de VSCODE que el fichero app.py es una app de flask. En este caso --> $env:FLASK_APP = "app"
# Abrir la ventana de comandos de MS-DOS, ir a la ubicación del fichero py en cuestión (D:\LocalUsers\ERojo\PROTOTIPOS\Python\froshims0) y ejecutar --> flask run

# turn this file into a web app
app = Flask(__name__)

tickers = si.tickers_sp500(False)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/search")
def search():
    q = request.args.get('q', default="")

    # print(q)
    ticker_list = []
    
    # for ticker in tickers:
    #     # Cuidado porque startswith es case sensitive: z no es Z
    #     if ticker.upper().startswith(q.upper()):
    #         ticker_list.append(ticker)

    # list comprehension. Esta línea equivale a las 4 anteriores
    ticker_list = [ticker for ticker in tickers if ticker.upper().startswith(q.upper())]

    return jsonify(ticker_list)

@app.route("/getStockData")
def getStockData():
    t = request.args.get('t', default="")
    return render_template("ticker.html", ticker=t)

@app.route("/getLivePrice")
def getLivePrice():
    t = request.args.get('t', default="")
    return str(si.get_live_price(t))

@app.route("/get_market_status")
def get_market_status():
    return str(si.get_market_status())

@app.route("/getShortName")
def getShortName():
    t = request.args.get('t', default="")
    return si.get_quote_data(t)["shortName"]

@app.route("/getDividends")
def getDividends():
    t = request.args.get('t', default="")

    try:
        dividends = si.get_dividends(t)
        return render_template("dividends.html", ticker=t, dividends=dividends)
    except:
        return render_template("error.html")

@app.route("/getQuoteTable")
def getQuoteTable():
    t = request.args.get('t', default="")
    my_dict = si.get_quote_table(t)

    for x in my_dict:
        # print(my_dict[x])
        # print(type(my_dict[x]))
        if type(my_dict[x]) is float and isnan(my_dict[x]):
            my_dict[x] = ""
            # print("Encontrado NaN")

    # Hace falta hacer un replace del valor NaN por el texto "NaN", ya que de lo contrario el JSON se queda con un formato incorrecto
    return json.dumps(my_dict)

@app.route("/dayMostActive")
def dayMostActive():
    try:
        most_active = si.get_day_most_active()
        print("OK")
        return render_template("daymostactive.html", data=most_active)
    except:
        print("Error")
        return render_template("error.html")    

@app.route("/getEarningsForDate")
def getEarningsForDate():
    return render_template("earningsForDate.html")

@app.route("/searchEarningsForDate")
def searchEarningsForDate():

    earnings = []
    
    from_date = request.args.get("from", default="")
    to_date = request.args.get("to", default="")
    # Check strings
    if from_date == "" or to_date == "":
        # print("Nos vamos")
        # print(earnings)
        return ""
    
    from_date = datetime.strptime(from_date, "%Y-%m-%d")
    to_date = datetime.strptime(to_date, "%Y-%m-%d")

    # Check dates
    if from_date > to_date:
        # print("Nos vamos")
        # print(earnings)
        return ""

    # print(from_date)
    # print(to_date)

    # Check number of days
    numdays = abs((to_date - from_date).days) + 1
    if numdays > 100:
        # print("Nos vamos")
        # print(earnings)
        return ""

    date_list = [from_date + timedelta(days=x) for x in range(numdays)]
    for fecha in date_list:
        # print(fecha)
        earnings.append(si.get_earnings_for_date(fecha))

    # print(earnings)
    # print(type(earnings))
    
    return jsonify(earnings)

def isNaN(num):
    return num != num