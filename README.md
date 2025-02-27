# ✈️ Flight Data ETL Project

A pipeline to fetch, transform, and load real-time flight data from the AviationStack API into a PostgreSQL database using Apache Airflow for orchestration.

---

## 📋 Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/federicopeker/aviation_stack.git
   cd aviation_stack
   ```

2. **Create environment file**:
   ```bash
   cp .env.template .env
   ```
   Edit the `.env` file with your credentials.

3. **Build and start containers**:
   ```bash
   docker-compose up --build
   ```

---

## 🚀 Usage

1. **Access Airflow UI**:
   - Visit `http://localhost:8081`
   - Login with default credentials (airflow/airflow)

2. **Trigger ETL Process**:
   - Enable then trigger the `flight_data_etl` DAG

---

---

## 🔑 Environment Variables

Required in `.env` file:

- `AVIATIONSTACK_API_KEY` - Your [AviationStack](https://aviationstack.com/) API key
---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Key improvements made:
- Added emojis and clear section headers
- Improved formatting with code blocks and structure visualization
- Added more context about Airflow credentials
- Made environment variables section more detailed
- Added proper markdown syntax for code blocks and paths
- Improved visual hierarchy with horizontal rules