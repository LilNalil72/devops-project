CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    phone VARCHAR(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(id),
    doctor_name VARCHAR(255) NOT NULL,
    appointment_time TIMESTAMP NOT NULL,
    status VARCHAR(50) DEFAULT 'Scheduled'
);

CREATE TABLE IF NOT EXISTS schedules (
    id SERIAL PRIMARY KEY,
    doctor_name VARCHAR(255) NOT NULL,
    work_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    room_number VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    schedule_id INTEGER REFERENCES schedules(id),
    patient_id INTEGER NOT NULL,
    booked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
