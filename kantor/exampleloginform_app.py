import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

from flask import Flask, render_template, request

app = Flask(__name__)

import csv
with open('valuta.csv', newline="") as csvfile:
    rates = csv.reader(csvfile)


@app.route("/exchanger", methods=["GET", "POST"])
def exchanger():
  if request.method == "POST":
    data = request.form
    code = data.get('code')
    amount = data.get("amount")

    

  return render_template("kantor.html")


if __name__ == "__main__":
  app.run(debug=True)