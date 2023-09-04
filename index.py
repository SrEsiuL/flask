from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import models as dbase  
from goleador import Goleador

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    goleadores = db['goleadores']
    goleadoresReceived = goleadores.find()
    return render_template('index.html', goleadores = goleadoresReceived)

#Method Post
@app.route('/goleadores', methods=['POST'])
def addProduct():
    goleadores = db['goleadores']
    name = request.form['name']
    goals = request.form['goals']
    pg = request.form['pg']

    if name and goals and pg:
        goleador = Goleador(name, goals, pg)
        goleadores.insert_one(goleador.toDBCollection())
        response = jsonify({
            'name' : name,
            'goals' : goals,
            'pg' : pg
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:goleador_name>')
def delete(goleador_name):
    goleadores = db['goleadores']
    goleadores.delete_one({'id2' : goleador_name})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:goleador_name>', methods=['POST'])
def edit(goleador_name):
    goleadores = db['goleadores']
    name = request.form['name']
    goals = request.form['goals']
    pg = request.form['pg']

    if name and goals and pg:
        goleadores.update_one({'id2' : goleador_name}, {'$set' : {'name' : name, 'goals' : goals, 'pg' : pg}})
        response = jsonify({'message' : 'Goleador ' + goleador_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.run(debug=True, port=1212)
