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


## 🧪 Testing

The USPowerPlant solution has been successfully tested on two different macOS machines. This helped verify consistent behavior across different hardware and system configurations.

Testing covered:

- Docker Compose setup and orchestration of all services
- Data ingestion and API responses
- Frontend UI functionality and responsiveness

This ensures the solution is stable and reliable for similar environments.

---

## ☁️ Cloud Deployment (AWS) - Coming soon. Need some more time.

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

* **Scalability**: Decoupled entire solution in 3 seperate services via Docker
* **DataIntegrity** : Defined unique constraint on state+plan_id+gen_id to ensure data deduplicity.
* **Resilience**: Health checks + retry logic to ensure the health of postres is up before depenedent services can start using it.
* **Security**: Env-based secrets + role-based auth (future) : Kept a single place to keep the vars used by the services to maintain single source of truth
* **Automation** : Also, Defined the file upload functionality to create the bucket and upload the sample file GEN23.csv, if the bucket and/or file not already presnet.

---

## ✅ Tech Stack

| Layer       | Technology     | Justification                                          |
| ----------- | -------------- | ---------------------------------------------------- |
| UI          | React          | Popular, component-based, fast rendering, large community support. Have some previous knowledge | Could have used Streamlist provided the time
| API         | FastAPI        | Conidering the data ingestion project, Python was the choie for data transformation, thefore thouugh to keep the same tech for api as well. High-performance Python framework, easy to build RESTful APIs with async support. Plus consideration of existing usage in Org  |
| DB          | PostgreSQL     | Reliable, scalable relational DB with strong SQL support and extensibility. Good for fixed schmea data solution storage and reads |
| Storage     | S3             | Industry standard object storage. Part of AWS ecosystem. Fairly aware of this.
| Container   | Docker Compose | Simplifies multi-container orchestration locally and in production | Easy to test and run on any system without any critical configuraiton needs.


---

## 🤠 GenAI Usage

Used OpenAI's ChatGPT to:

* Suggest healthcheck logic
* Structure documentation
* Debug Docker-related issues
* Debug Env Related Issues
* React useState related stuff
* Others

