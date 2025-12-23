from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(120), nullable=False)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        msg = request.form['msg']

        new_customer = Customer(name=name, email=email, msg=msg)
        db.session.add(new_customer)
        db.session.commit()

        return 'Customer added successfully'

    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # create tables
    app.run(debug=True)


