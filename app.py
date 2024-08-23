from flask import Flask, request, jsonify, render_template
from backend import chatbot_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_response = chatbot_response(user_message)
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)




