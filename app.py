from flask import Flask, render_template, request 
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('estructura.html')

@app.route('/agendar/cita', methods=['POST'])
def AgregarDatos():
    baseDB = sqlite3.connect('citas.db', check_same_thread=False)
    cursorDataBase = baseDB.cursor()
    
    nombre = request.form['name']
    correo = request.form['email']
    numero = request.form['number']
    fecha = request.form['date']
    
    datosUsuarios = nombre, correo, numero, fecha
    
    cursorDataBase.execute('INSERT into usuarios(nombre, correo, numero, fecha) VALUES(?, ?, ?, ?)', datosUsuarios)
    baseDB.commit()
    
    return render_template('estructura.html')
if __name__=='__main__':
    app.run(debug=True)