from flask import Flask, jsonify
from flask import request , make_response
from flask import render_template
from Slang import Slang
app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/agregar/')
def agregar():
    return render_template('agregar.html')

@app.route('/agregado/', methods=['POST'])
def agregado() :
    if request.method == 'POST':
        Slang_request ={
            "palabra_" : request.form['palabra'],
            "definicion_" : request.form['definicion']
        }
        Slang.update(Slang_request)
        return jsonify({"message":"Palabra actualizada!","palabra":Slang})

@app.route('/ver/')
def ver_listado():
    return jsonify(Slang)
if __name__ == "__main__":
    app.run()

