CREATE TABLE IF NOT EXISTS testdata (
    id SERIAL PRIMARY KEY,
    flight_date DATE,
    flight_status VARCHAR(50),
    departure_airport VARCHAR(255),
    departure_timezone VARCHAR(100),
    arrival_airport VARCHAR(255),
    arrival_timezone VARCHAR(100),
    arrival_terminal VARCHAR(50),
    airline_name VARCHAR(255),
    flight_number VARCHAR(50)
);
