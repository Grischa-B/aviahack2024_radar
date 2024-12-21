# Django Project with InfluxDB Integration

This project is a Django-based application integrated with InfluxDB for storing and retrieving time-series data. The application provides a REST API for CRUD operations, including data creation, retrieval, updating, and deletion.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [API Endpoints](#api-endpoints)
7. [Environment Variables](#environment-variables)
8. [License](#license)

---

## Project Structure

```plaintext
.
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── myapp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── myproject
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── stats
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── influxdb_client.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── db.sqlite3
└── .env
```

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker and Docker Compose
- Python 3.10+
- Git

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Create a virtual environment and install dependencies (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

3. **Set up the `.env` file:**

   Create a `.env` file in the root directory and add the necessary environment variables (see [Environment Variables](#environment-variables)).

4. **Start the application using Docker Compose:**

   ```bash
   docker-compose up --build
   ```

---

## Configuration

The application uses environment variables stored in a `.env` file to configure the database connection and other settings. Make sure the `.env` file includes the following variables:

```plaintext
INFLUXDB_URL=http://db:8086
INFLUXDB_TOKEN=your_influxdb_token
INFLUXDB_ORG=your_organization
INFLUXDB_BUCKET=your_bucket_name
INFLUXDB_ADMIN_USER=admin
INFLUXDB_ADMIN_PASSWORD=admin_password
```

---

## Running the Application

1. **Start the application:**

   ```bash
   docker-compose up
   ```

2. **Access the application:**

   The Django application will be available at `http://localhost:8000`.

3. **Run database migrations (if necessary):**

   ```bash
   docker-compose exec web python manage.py migrate
   ```

---

## API Endpoints

The application provides the following REST API endpoints:

### POST `/stats/create`
- **Description:** Add a new record to the database.
- **Payload:**
  ```json
  {
    "dateCreate": "YYYY-MM-DD HH:MM:SS",
    "claim_count": 2,
    "suggestion_count": 1,
    "thank_count": 2,
    "average_rank": 3,
    "SLI": 7
  }
  ```
- **Response:** JSON with success or error message.

### GET `/stats/read?date=YYYY-MM-DD`
- **Description:** Retrieve records for a specific date.
- **Response:**
  ```json
  {
    "status": "success",
    "data": [ ... ]
  }
  ```

### PATCH `/stats/update`
- **Description:** Update a record for a specific date.
- **Payload:**
  ```json
  {
    "date": "YYYY-MM-DD",
    "fields": {
      "claim_count": 3,
      "average_rank": 4
    }
  }
  ```
- **Response:** JSON with success or error message.

### DELETE `/stats/delete`
- **Description:** Delete a record for a specific date.
- **Payload:**
  ```json
  {
    "date": "YYYY-MM-DD"
  }
  ```
- **Response:** JSON with success or error message.

---

## Environment Variables

| Variable              | Description                      |
|-----------------------|----------------------------------|
| `INFLUXDB_URL`        | URL for the InfluxDB instance    |
| `INFLUXDB_TOKEN`      | Authentication token for InfluxDB |
| `INFLUXDB_ORG`        | Organization name in InfluxDB    |
| `INFLUXDB_BUCKET`     | Bucket name in InfluxDB          |
| `INFLUXDB_ADMIN_USER` | Admin username for InfluxDB      |
| `INFLUXDB_ADMIN_PASSWORD` | Admin password for InfluxDB  |

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

