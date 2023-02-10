from flask import Flask, render_template, request
import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()


with open("currency.csv", "w", encoding="UTF8", newline="") as csvfile:
    header = ["currency", "code", "bid", "ask"]
    writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=header)
    writer.writeheader()
    for i in data[0]["rates"]:
        writer.writerow(i)

Currency = []
Bid = []

with open("currency.csv", "r", encoding="UTF8", newline="") as csvfile:
    header = ["currency", "code", "bid", "ask"]
    reader = csv.DictReader(csvfile, delimiter=";", fieldnames=header)
    x = 0
    for i in reader:
        Currency.append([x, i["currency"].title()])
        Bid.append(i["bid"])
        x += 1

app = Flask(__name__)


@app.route("/cyrrency", methods=["GET", "POST"])
def action():

    if request.method == "POST":
        option = int(request.form["option"][1:2])
        quantity = int(request.form.get("quantity"))
        bid = float(Bid[option])
        result = bid * quantity
        return render_template("index.html", items=Currency, result=result)

    return render_template("index.html", x=x,  items=Currency)


if __name__ == "__main__":
    app.run(debug=True)