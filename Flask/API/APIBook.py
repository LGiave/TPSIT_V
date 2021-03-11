from flask import Flask,url_for,jsonify,request
import flask

books = [
{'id': 0,
'title': 'Il nome della Rosa',
'author': 'Umberto Eco',
'year_published': '1980'},
{'id': 1,
'title': 'Il problema dei tre corpi',
'author': 'Liu Cixin',
'published': '2008'},
{'id': 2,
'title': 'Fondazione',
'author': 'Isaac Asimov',
'published': '1951'}
]

app= flask.Flask(__name__)
app.config["DEBUG"]= True

@app.route('/', methods=['GET'])
def home():
    return "<h1> Biblioteca online</><p>Prototipo web API</p>"


@app.route('/api',methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    
    for book in books:
        if book['id'] == id:
            results.append(book)
    
    return jsonify(results)

@app.route('/api/v1/title', methods=['GET'])
def api_title():
    if 'title' in request.args:
        title= str(request.args['title'])
    else:
        return "Error: No title field provided. Please specify an title."
    
    results=[]

    for book in books:
        if book['title'] == title:
            results.append(book)
    
    return jsonify(results)

app.run()