from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/api/user')
def user_data():
    data = {
        'name': 'Harshitha Kumari',
        'referral_code': 'harshitha2025',
        'total_donations': 12500
    }
    return jsonify(data)

@app.route('/api/leaderboard')
def leaderboard_data():
    data = [
        {'name': 'Harshitha', 'donations': 12500},
        {'name': 'Anjali', 'donations': 11000},
        {'name': 'Sai', 'donations': 9500},
        {'name': 'Rahul', 'donations': 8000},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
