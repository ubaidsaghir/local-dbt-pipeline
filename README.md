# 🔄 Local dbt Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-red)
![dbt](https://img.shields.io/badge/dbt-Transformation-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 🚀 Overview

The **Local dbt Pipeline Project** demonstrates how to build a complete **local data engineering pipeline** using:

- Apache Airflow (orchestration)  
- dbt (data transformation)  
- Docker (environment setup)  

The project focuses on creating a **modular, automated pipeline** that ingests, transforms, and prepares data for analytics.

---

## 🎯 Problem Statement

Data pipelines are often:

- Manually executed  
- Difficult to maintain  
- Lacking automation  
- Not structured for scalability  

There is a need for a **local, production-style pipeline** that:

- Automates workflows  
- Applies transformations systematically  
- Ensures data reliability  

---

## ✅ Solution

This project provides:

- A **Dockerized Airflow setup**
- Automated DAG for pipeline execution
- A **dbt project** for transformation
- Modular pipeline structure
- End-to-end local data workflow

---

## 🏗️ Architecture
Raw Data → Airflow DAG → dbt Models → Transformed Data


---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python | Core programming |
| Apache Airflow | Workflow orchestration |
| dbt | Data transformation & modeling |
| Docker | Environment management |
| SQL | Data transformation logic |
| GitHub | Version control |

---


---

## 🔄 Data Pipeline

### 1️⃣ Orchestration (Airflow)

- Defines DAG workflow  
- Automates pipeline execution  
- Runs dbt commands  

---

### 2️⃣ Transformation (dbt)

- Cleans raw data  
- Applies transformations  
- Creates analytical models  
- Ensures data quality  

---

## 🧮 Data Processing

The pipeline performs:

- Data ingestion  
- Data transformation  
- Data validation  
- Model creation  

---

## 🧪 Data Validation

dbt ensures data quality through:

- Not null tests  
- Unique tests  
- Schema validation  

---

## ⚙️ Environment Setup

### Requirements

- Python 3.10+  
- Docker Desktop  
- Apache Airflow  
- dbt Core  

---

## 🐍 Setup

```bash
python -m venv .venv
```
Activate Environment:
```bash
.venv\Scripts\activate
```

---

## ▶️ Running the Project

### Start Airflow
```bash
docker compose -f airflow/docker-compose.yaml up -d
```
### Open Airflow UI
```bash
http://localhost:8080
```
### Run Pipeline
- Trigger DAG from Airflow UI
- Monitor execution logs
### Run dbt (Manual)
```bash
cd dbt_project
dbt run
dbt test
```

---

## 📈 Outputs
* Transformed datasets
* dbt models
* DAG execution logs
* Data validation results

---

## 📌 Conclusion
The Local dbt Pipeline Project demonstrates how to build a structured, automated data pipeline using Airflow and dbt in a local environment.

---

## 🌐 Author
[![GitHub](https://img.shields.io/badge/GitHub-ubaidsaghir-181717?logo=github&logoColor=white)](https://github.com/ubaidsaghir)

---
