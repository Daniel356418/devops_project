from flask import Flask, render_template
import datetime
import socket
import os

app = Flask(__name__)
visit_count = 0

@app.route('/')
def home():
    global visit_count
    visit_count += 1
    
    server_info = {
        'hostname': socket.gethostname(),
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'visits': visit_count,
        'environment': os.getenv('ENVIRONMENT', 'Development')
    }
    
    return render_template('index.html', **server_info)

@app.route('/health')
def health():
    return {'status': 'healthy', 'timestamp': datetime.datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)