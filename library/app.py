from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response
from forms import HomelibraryForm                   
from models import homelib                          

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"



@app.route("/homelib/", methods=["GET", "POST"])   
def homelib_list():                                  
    form = HomelibraryForm()                        
    error = ""
    if request.method == "POST":  
        if form.validate_on_submit():
            homelib.create(form.data)                 
            homelib.save_all()                        
        return redirect(url_for("homelib_list"))       
    return render_template("homelib.html", form=form, homelib=homelib.all(), error=error)    
    

@app.route("/homelib/<int:homelibrary_id>/", methods=["GET", "POST"])  
def homelibrary_details(homelibrary_id):                            
    homelibrary = homelib.get(homelibrary_id - 1)
    form = HomelibraryForm(data=homelibrary)         
    if request.method == "POST":   
        if form.validate_on_submit():
            homelib.update(homelibrary_id - 1, form.data)       
        return redirect(url_for("homelib_list"))        
    return render_template("homelibrary_id.html", form=form, homelibrary_id=homelibrary_id)  

 

#1: ф-ція збору данних
@app.route("/api/v1/homelib/", methods=["GET"]) 
def homelib_list_api_v1(): 
    return jsonify(homelib.all())

#2:збір данних ID - GET
@app.route("/api/v1/homelib/<int:homelibrary_id>", methods=["GET"]) 
def get_homelibrary(homelibrary_id):
    homelibrary = homelib.get(homelibrary_id)
    if not homelibrary:    
        abort(404)   
    return jsonify({"homelibrary": homelibrary})


@app.errorhandler(404)  
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

#3: додавання елементу  - POST
@app.route("/api/v1/homelib/", methods=["POST"]) 
def create_homelibrary():
    if not request.json or not 'title' in request.json:
        abort(400)
    homelibrary = {
        'id': homelib.all()[-1]['id'] + 1,  
        'title': request.json['title'], 
        'description': request.json.get('description', ""),  
        'done': False
    }
    homelib.create(homelibrary)
    return jsonify({'homelibrary': homelibrary}), 201 



@app.errorhandler(400)    
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


#4: видалення - DELETE
@app.route("/api/v1/homelib/<int:homelibrary_id>", methods=['DELETE'])  
def delete_homelibrary(homelibrary_id):
    result = homelib.delete(homelibrary_id)
    if not result:
        abort(404)
    return jsonify({'result': result})



@app.route("/api/v1/homelib/<int:homelibrary_id>", methods=["PUT"])
def update_homelibrary(homelibrary_id): 
    homelibrary = homelib.get(homelibrary_id)   
    if not homelibrary:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json  
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)   
    homelibrary = {
        'title': data.get('title', homelibrary['title']),
        'description': data.get('description', homelibrary['description']),
        'done': data.get('done', homelibrary['done'])
    }
    homelib.update(homelibrary_id, homelibrary)
    return jsonify({'homelibrary': homelibrary})


if __name__ == "__main__":
    app.run(debug=True)