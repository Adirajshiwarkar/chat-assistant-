from flask import Flask, request, jsonify
import sqlite3
from waitress import serve
import os

app = Flask(__name__)

# Initialize SQLite Database
DATABASE = 'demodb.db'

# Helper Function to Execute Queries
def execute_query(query, params=()):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.commit()  # Ensure changes are saved if needed
    except sqlite3.Error as e:
        return str(e)
    finally:
        conn.close()
    return result

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Server is running"})

@app.route('/chat', methods=['POST'])
def chat_assistant():
    user_query = request.json.get('query', '')

    if not user_query:
        return jsonify({"error": "Query cannot be empty."}), 400

    # Query Processing
    if "show me all employees in" in user_query.lower():
        department = user_query.split("in")[-1].strip().capitalize()
        result = execute_query("SELECT * FROM Employees WHERE Department = ?", (department,))
        if isinstance(result, str):
            return jsonify({"error": result}), 500
        if result:
            return jsonify([{ "ID": row[0], "Name": row[1], "Department": row[2], "Salary": row[3], "Hire_Date": row[4] } for row in result])
        else:
            return jsonify({"message": "No employees found in the specified department."})

    elif "who is the manager of" in user_query.lower():
        department = user_query.split("of")[-1].strip().capitalize()
        result = execute_query("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        if isinstance(result, str):
            return jsonify({"error": result}), 500
        if result:
            return jsonify({"Manager": result[0][0]})
        else:
            return jsonify({"message": "No department found with that name."})

    elif "list all employees hired after" in user_query.lower():
        date = user_query.split("after")[-1].strip()
        result = execute_query("SELECT * FROM Employees WHERE Hire_Date > ?", (date,))
        if isinstance(result, str):
            return jsonify({"error": result}), 500
        if result:
            return jsonify([{ "ID": row[0], "Name": row[1], "Department": row[2], "Salary": row[3], "Hire_Date": row[4] } for row in result])
        else:
            return jsonify({"message": "No employees hired after the specified date."})

    elif "what is the total salary expense for" in user_query.lower():
        department = user_query.split("for")[-1].strip().capitalize()
        result = execute_query("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,))
        if isinstance(result, str):
            return jsonify({"error": result}), 500
        if result and result[0][0]:
            return jsonify({"Total Salary Expense": result[0][0]})
        else:
            return jsonify({"message": "No salary data found for the specified department."})

    else:
        return jsonify({"message": "Sorry, I didn't understand that query."})

if __name__ == '__main__':
    # Ensure database file exists
    if not os.path.exists(DATABASE):
        print(f"Database '{DATABASE}' not found. Please ensure it exists and contains required tables.")
        exit(1)
    
    # Use Waitress for Production Deployment
    host = os.environ.get('HOST', '127.0.0.1')  # Default host set to 127.0.0.1
    port = int(os.environ.get('PORT', 8080))  # Default to 8080 if no environment variable is set
    print(f"Starting server at http://{host}:{port}")
    serve(app, host=host, port=port)
