from flask import Flask, render_template, request
import json
import addRecord
import deleteScript
import getRecord

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('gui.html')
    
    name = request.form['fullname']
    email = request.form['email']
    number = request.form['phone']
    drug = request.form['prescription']
    dose = request.form['dosage']
    
    addRecord.newUser(name, email, number, drug, dose)

    return render_template('gui.html')

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('check.html')
    
    id = request.form['ID']
    #data_json = json.dumps(getRecord.getRecord(id))

    return render_template('check.html')#, data=data_json)

@app.route('/issue', methods=['GET', 'POST'])
def issue():
    if request.method == 'GET':
        return render_template('Output.html')
    
    id = request.form['ID']
    deleteScript.deleteRecord(id)

    return render_template('Output.html')

if __name__ == '__main__':
    app.run(debug=True)