from flask import Flask, render_template,request, Response, jsonify, redirect, url_for
import models as dbase
from product import Product

db = dbase.dbConnection()
app = Flask(__name__)


@app.route('/')
def inicio():
    product = db['product']
    productReceived = product.find()
    return render_template('/index.html', products = productReceived)

#Método Post
@app.route('/product', methods=['POST'])
def addProduct():
    product = db['product']
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']

    if name and age and email:
        product = Product(name,age,email)
        product.insert_one(product.toDBCollection())
        response = jsonify({'name':name, 'age':age, 'email':email})
        return redirect(url_for('home'))
    else:
        return notFound()
    
#Método error
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message':'No encontrado'+request.url,
        'status':'404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

#

if __name__ == "__main__":
	app.run("127.0.0.1", 5000, debug = True)