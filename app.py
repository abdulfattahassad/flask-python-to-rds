import os
import boto3
import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# --- 1️⃣ Fetch secrets from AWS Secrets Manager ---
client = boto3.client('secretsmanager')   
response = client.get_secret_value(SecretId='dbsecret')
dbsecret = json.loads(response['SecretString'])

DB_username = dbsecret['username']
DB_password = dbsecret['password']
DB_host = dbsecret['host']
DB_name = dbsecret['dbname']

# --- 2️⃣ Flask app ---
app = Flask(__name__)

# --- 3️⃣ Configure SQLAlchemy using secrets ---
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_username}:{DB_password}@{DB_host}/{DB_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- 4️⃣ Define models ---
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(120), nullable=False)

# --- 5️⃣ Routes ---
@app.route('/', methods=['GET', 'POST'])
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

# --- 6️⃣ Create tables and run app ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
