from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('encyclopedia.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topics')
def get_topics():
    conn = get_db_connection()
    topics = conn.execute('SELECT DISTINCT main_topic FROM topics').fetchall()
    conn.close()
    return jsonify([topic['main_topic'] for topic in topics])

@app.route('/subtopics/<topic>')
def get_subtopics(topic):
    conn = get_db_connection()
    subtopics = conn.execute('SELECT subtopic FROM topics WHERE main_topic = ?', (topic,)).fetchall()
    conn.close()
    return jsonify([subtopic['subtopic'] for subtopic in subtopics])

@app.route('/content/<topic>/<subtopic>')
def get_content(topic, subtopic):
    conn = get_db_connection()
    content = conn.execute('SELECT content FROM topics WHERE main_topic = ? AND subtopic = ?', (topic, subtopic)).fetchone()
    conn.close()
    return jsonify({"content": content['content'] if content else "Content not found."})

if __name__ == '__main__':
    app.run(debug=True)