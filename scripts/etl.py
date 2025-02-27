import logging
import os
from typing import Any, Dict, List

import psycopg2
import requests
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
DB_CONFIG = {
    "dbname": "testfligoo",
    "user": "admin",
    "password": "password",
    "host": "postgres",
    "port": 5432,
}

API_URL = "http://api.aviationstack.com/v1/flights"


def fetch_flight_data() -> List[Dict[str, Any]]:
    """Fetch real-time flight data from the AviationStack API."""
    params = {"access_key": API_KEY, "flight_status": "active", "limit": 100}
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json().get("data", [])


def transform_data(raw_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Clean and transform flight data."""
    transformed = []
    for flight in raw_data:
        transformed.append(
            {
                "flight_date": flight.get("flight_date"),
                "flight_status": flight.get("flight_status"),
                "departure_airport": flight.get("departure", {}).get("airport"),
                "departure_timezone": (
                    flight.get("departure", {}).get("timezone") or ""
                ).replace("/", " - "),
                "arrival_airport": flight.get("arrival", {}).get("airport"),
                "arrival_timezone": (
                    flight.get("arrival", {}).get("timezone") or ""
                ).replace("/", " - "),
                "arrival_terminal": (
                    flight.get("arrival", {}).get("terminal") or ""
                ).replace("/", " - "),
                "airline_name": flight.get("airline", {}).get("name"),
                "flight_number": flight.get("flight", {}).get("number"),
            }
        )
    return transformed


def insert_data_to_db(data: List[Dict[str, Any]]):
    """Insert cleaned data into PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        insert_query = """
        INSERT INTO testdata (flight_date, flight_status, departure_airport, departure_timezone,
                              arrival_airport, arrival_timezone, arrival_terminal,
                              airline_name, flight_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        for flight in data:
            cur.execute(
                insert_query,
                (
                    flight["flight_date"],
                    flight["flight_status"],
                    flight["departure_airport"],
                    flight["departure_timezone"],
                    flight["arrival_airport"],
                    flight["arrival_timezone"],
                    flight["arrival_terminal"],
                    flight["airline_name"],
                    flight["flight_number"],
                ),
            )

        conn.commit()
        cur.close()
        conn.close()
        logger.info("Data successfully inserted into the database.")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")


if __name__ == "__main__":
    logger.info("Running ETL process...")
    raw_data = fetch_flight_data()
    transformed_data = transform_data(raw_data)
    insert_data_to_db(transformed_data)
    logger.info("✅ ETL process completed.")
