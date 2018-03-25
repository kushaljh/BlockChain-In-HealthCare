from flask import Flask, render_template, request
import addRecord

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

if __name__ == '__main__':
    app.run(debug=True)