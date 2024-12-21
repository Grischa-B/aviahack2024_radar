# Django & React Application

This repository contains a full-stack application built using Django as the backend and React as the frontend. The application is containerized with Docker for easy deployment and development.

## Features

### Backend (Django)
- REST API for CRUD operations using Django REST framework.
- Integration with InfluxDB for storing and querying time-series data.
- Configuration through environment variables.

### Frontend (React)
- A single-page application (SPA) built with React.
- Dynamic components for visualizing and interacting with backend data.
- Proxy setup for seamless API calls to the Django backend.

### Docker
- Separate containers for backend and frontend.
- Docker Compose for managing services.

## Requirements

- Docker
- Docker Compose

## Project Structure

```
.
├── Dockerfile.backend       # Dockerfile for the Django backend
├── Dockerfile.frontend      # Dockerfile for the React frontend
├── docker-compose.yml       # Docker Compose configuration
├── frontend/                # React frontend code
│   ├── public/              # Static files for the React app
│   ├── src/                 # Source files for React components
├── myapp/                   # Django app for core functionality
├── myproject/               # Django project settings and configuration
├── stats/                   # Django app for stats and InfluxDB integration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Grischa-B/aviahack2024_radar
cd aviahack2024_radar
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory and configure the following variables:

#### For Backend
```env
INFLUXDB_URL=http://influxdb:8086
INFLUXDB_TOKEN=your_influxdb_token
INFLUXDB_ORG=your_org
INFLUXDB_BUCKET=your_bucket
DJANGO_SECRET_KEY=your_django_secret_key
```

#### For Frontend
In `frontend/.env`, add:
```env
REACT_APP_API_URL=http://backend:8000
```

### 3. Build and Run the Containers

Start the application using Docker Compose:

```bash
docker-compose up --build
```

### 4. Access the Application

- Backend API: `http://localhost:8000`
- Frontend: `http://localhost:3000`

## Docker Configuration

### Docker Compose Services

#### Backend
- **Service Name**: `backend`
- **Dockerfile**: `Dockerfile.backend`
- **Ports**: `8000:8000`

#### Frontend
- **Service Name**: `frontend`
- **Dockerfile**: `Dockerfile.frontend`
- **Ports**: `3000:3000`

#### InfluxDB
- **Service Name**: `influxdb`
- **Image**: `influxdb:latest`
- **Ports**: `8086:8086`

### Proxy Setup for Frontend
The React app uses `http://backend:8000` as the API endpoint when running inside Docker. This is configured in the `.env` file.

## Development Notes

### Running Frontend Locally
If you want to run the React app locally without Docker:

```bash
cd frontend
npm install
npm start
```

Make sure the backend is running and update the `REACT_APP_API_URL` in `frontend/.env` to `http://localhost:8000`.

### Running Backend Locally
To run the Django backend without Docker:

```bash
pip install -r requirements.txt
python manage.py runserver
```

## Deployment
For production, make sure to configure environment variables securely and use a production-grade WSGI server like Gunicorn for Django.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

