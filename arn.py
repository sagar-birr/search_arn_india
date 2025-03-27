from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    conn.close()
    return (rows[0] if rows else None) if one else rows

def construct_query(name, email, arn, pin):
    query = "SELECT * FROM users WHERE 1=1"
    args = []

    if name:
        query += " AND name LIKE ?"
        args.append(f"%{name}%")

    if email:
        query += " AND email LIKE ?"
        args.append(f"%{email}%")
    
    if arn:
        query += " AND arn LIKE ?"
        args.append(f"%{arn}%")

    if pin:
        query += " AND pin LIKE ?"
        args.append(f"%{pin}%")

    results = query_db(query, args)
    
    return jsonify([dict(row) for row in results])


@app.route('/search', methods=['GET'])
def search():
    name = request.args.get("name")
    email = request.args.get("email")
    arn = request.args.get("arn")
    pin = request.args.get("pin")
   
    data = construct_query(name, email, arn, pin)
    
    return data


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
