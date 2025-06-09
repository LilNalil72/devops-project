from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from prometheus_client import start_http_server, Counter, Summary

app = Flask(__name__)
DATABASE_URL = "postgresql://admin:secret@postgres:5432/clinic"
engine = create_engine(DATABASE_URL)

# Метрики Prometheus
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Запускаем сервер метрик на порту 8000
start_http_server(8000)

@app.route('/')
def home():
    return "Registry Service"

@app.route('/patients', methods=['POST'])
@REQUEST_TIME.time()
def create_patient():
    data = request.json
    try:
        with engine.begin() as conn:
            conn.execute(text("""
                INSERT INTO patients (full_name, birth_date, phone)
                VALUES (:full_name, :birth_date, :phone)
            """), data)
        REQUEST_COUNT.labels('POST', '/patients', '201').inc()
        return jsonify({"status": "success"}), 201
        
    except IntegrityError as e:
        REQUEST_COUNT.labels('POST', '/patients', '400').inc()
        return jsonify({
            "status": "error",
            "message": "Phone number already exists"
        }), 400
