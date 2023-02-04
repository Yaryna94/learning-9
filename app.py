
from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def mypage():
   if request.method == 'GET':
       print("Вітаю на моїй сторінці")
       return render_template("templates/form.html")
       
@app.route('/mypage/contact', method=['GET', 'POST'])
def contact():
 if request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/me")
 

