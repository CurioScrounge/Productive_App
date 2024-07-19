from flask import Flask, request, jsonify
import threading

app = Flask(__name__)
current_url = ""

@app.route('/current_url', methods=['POST'])
def update_current_url():
    global current_url
    data = request.get_json()
    current_url = data['url']
    print(f"Received URL: {current_url}")  # Debug logging
    return jsonify({"status": "success"})

def run_flask():
    app.run(port=5000, debug=False)

def start_flask_server():
    threading.Thread(target=run_flask).start()

if __name__ == "__main__":
    start_flask_server()