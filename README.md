# 🇺🇸 USPowerPlant: Annual Net Generation Visualizer

A cloud-ready, Dockerized, full-stack application to ingest, transform, store, and visualize annual net generation data of U.S. power plants based on the EPA’s eGRID 2023 dataset.

---

## 🔧 Features

* Ingests EPA-formatted CSV files from S3-compatible storage (AWS S3).
* Cleans, normalizes, and stores data in PostgreSQL
* Exposes RESTful APIs via FastAPI
* Interactive React frontend to explore top N power plants by net generation per U.S. state
* Fully containerized with Docker Compose
* Optional: Cloud-ready Terraform deployment on AWS

---

## 🏗️ Architecture Overview

### 🔹 Logical View

* **Ingestor**: Extracts & loads CSVs to PostgreSQL with relevant fields. Also checks if the bucket is not present, creates the bucket and upload the file GEN23.csv
* **Backend API**: FastAPI-based service to query the database
* **Frontend**: React app that visualizes top N power plants by state
* **Database**: PostgreSQL
* **Storage**: Object Storage (S3)

### 🔹 Deployment View

```plaintext
User --> Frontend (React)
         |
         v
     Backend API (FastAPI) <---> PostgreSQL
         |
         v
     Object Storage (S3/MinIO) --> Ingestor
```

### 🔹 Infrastructure

* Docker + Docker Compose
* Environment variables managed centrally via `.env`
* Optional: AWS deployment via Terraform

---

## 🚀 Getting Started (Local Setup)

### Prerequisites

* Docker + Docker Compose
* Git
* .env file: Need to update this, with correct details like AWS & db credits.
* S3 Bucket : 
  + Bucket Created + File Uploaded with GEN23.csv schema file. NOTE, if no bucket found, ingestor on run, will create it and put the file in it so that S3 resource is ready to read the file.
  + This file is in the ingestor module, and was extracted from the parent excel file GEN23 sheet, which was downloaded from the assignment given link, and was used for the development.

### Clone the Repository

```bash
git clone https://github.com/heybirendra/uspowerplant.git
cd uspowerplant
```

### Environment Setup

Copy and update `.env.example`:

```bash
cp .env.example .env : 
```
Above, to create the .env file at the project root based upon the sample file .env.example. Once created, update the file with the required values. Please, ensure your AWS given credentials and DB values are correct. Please also ensure AWS credential user has accessible roles and policies with respect to AWS S3 Service.

### Run All Services

```bash
docker-compose up --build
```

Access: Once all services are up, use the below URLs. 

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)
* pgAdmin (if enabled): [http://localhost:8081](http://localhost:8081) : This is a service defined in the docker-compose file and in disabled state. I used this to verify the ingested data.
* Optional : You may use pgAdmin to see the data and tables. 
         pgAdmin on Docker : You can enable the commented service "pgadmin" in docker-compose.yml file if wanna use the dockerized pgAdmin. In this case, host = postgres (docker service), need to be given. 
         pgAdmin on Local : If pgAdmin running on local machine, then while registering the server, please provide host = localhost

---

## 🥚 API Usage

FastAPI automatically generates documentation:

* Swagger UI: `/docs`

Main Endpoints:

* `GET /pp/powerplants?limit=10&state=CA` : Main API to get the data filtered by state and limited in number.
* `GET /pp/states` : Populating the list of states dynamically from the data in table

---

## 🖼️ UI Usage

* Select U.S. State
* Choose number of top plants
* View table of results
* Visualization Chart can be added as well (coming soon)

---

## ⚙️ Docker & Volumes

Clean everything: This script can be used to cleanslate the environment by cleaning all unused containers, images and volumes and was helpful while testing.

```bash
./clean_uspowerplant.sh
./clean_test.sh
```

---

## ☁️ Cloud Deployment (AWS)

Terraform deployment coming soon! Can be done, but need More time

Features:

* VPC + ECS
* RDS (PostgreSQL)
* S3 bucket
* Outputs DNS for frontend + backend

---

## 🔐 Authentication (Optional)

* Token-based auth for API endpoints
* Protect ingestion and analytics routes

---

## 📊 Monitoring (Optional Coming Soon)

* Integrate with Prometheus + Grafana
* Log collection with Loki or CloudWatch (for AWS)

---

## 📁 Project Structure

```plaintext
USPowerPlant/
│
├── app/                  # FastAPI Backend
├── ingestor/             # Data ingestion logic
├── powerplant-frontend/  # React frontend
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🧠 Non-functional Considerations

* **Scalability**: Decoupled services via Docker
* **DataIntegrity** : Defined unique constraint on state+plan_id+gen_id
* **Resilience**: Health checks + retry logic
* **Security**: Env-based secrets + role-based auth (future)
* **Automation** : Defined the upload functionality to create the bucket and upload the sample file GEN23.csv, if not already presnet.

---

## ✅ Tech Stack

| Layer       | Technology     |
| ----------- | -------------- |
| UI          | React          |
| API         | FastAPI        |
| DB          | PostgreSQL     |
| Storage     | S3             |
| Container   | Docker Compose |
| Infra (Opt) | Terraform (Pending)     |

---

## 🤠 GenAI Usage

Used OpenAI's ChatGPT to:

* Suggest healthcheck logic
* Structure documentation
* Debug Docker-related issues
* Debug Env Related Issues
* React useState related stuff
* Others

