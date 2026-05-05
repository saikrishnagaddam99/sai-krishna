from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config

# ✅ CREATE APP FIRST
app = Flask(__name__)
app.config.from_object(Config)

# ✅ THEN DB
db = SQLAlchemy(app)

# Model
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    blood_group = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(50), nullable=False)

# Create table
with app.app_context():
    db.create_all()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Register donor
@app.route('/register', methods=['POST'])
def register():
    donor = Donor(
        name=request.form['name'],
        blood_group=request.form['blood_group'],
        phone=request.form['phone'],
        city=request.form['city']
    )
    db.session.add(donor)
    db.session.commit()
    return redirect('/')

# ✅ Search donor (correct place)
@app.route('/search', methods=['GET'])
def search():
    blood_group = request.args.get('blood_group')

    print("Searching for:", blood_group)

    donors = Donor.query.filter_by(blood_group=blood_group).all()

    print("Found:", donors)

    return render_template('results.html', donors=donors)
# Run app
if __name__ == '__main__':
    print("Server running...")
    app.run(debug=True)