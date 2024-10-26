from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Main page route with support for both GET and HEAD requests
@app.route('/', methods=['GET', 'HEAD'])
def home():
    return render_template('index.html')

# Route to submit work logs
@app.route('/submit', methods=['POST'])
def submit_work_log():
    data = request.json
    # Save or process data (you may save it to a file or database here)
    return jsonify({"message": "Work log submitted successfully!"}), 201

# Route to retrieve logs for the administrator
@app.route('/get_logs', methods=['GET'])
def get_logs():
    # Return stored logs (fetch from file or database)
    logs = [
        # Example logs, replace with database or file data
        {"name": "Employee 1", "ticket": "123", "location": "Site A", "work_order": "WO-001"},
        {"name": "Employee 2", "ticket": "456", "location": "Site B", "work_order": "WO-002"}
    ]
    return j
