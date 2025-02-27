FROM apache/airflow:2.7.0-python3.8

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

USER airflow
WORKDIR /opt/airflow

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the scripts directory
COPY scripts /opt/airflow/scripts
COPY dags /opt/airflow/dags


# Set the default command for Airflow containers
CMD ["airflow", "standalone"]