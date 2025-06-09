from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Schedule Service"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

DATABASE_URL = "postgresql://admin:secret@postgres:5432/clinic"
