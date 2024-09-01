# Data orchestration with Airflow and AWS S3

## Overview
This project aims to develop a robust and scalable data pipeline that automates the process of extracting data from Google's API and storing it in an Amazon S3 bucket. Utilizing Apache Airflow as the orchestrator, the pipeline ensures efficient scheduling, monitoring, and management of data flows.

## Key Components

#### Data Source: Youtube trending videos data
- The application emulates streaming data by sampling records from a CSV file in quick intervals.

#### Apache Airflow:
- The orchestration tool used to automate and manage the workflow of data extraction, transformation, and loading (ETL).
  
#### AWS S3:
- The storage solution for holding processed data, providing durability and easy access for downstream applications.

## Workflow
### Data Ingestion:
- Use Airflow's PythonOperator to call Google's API and fetch data.
- Implement authentication and error handling to ensure reliable data retrieval.
### Data Transformation:
- Process the raw data using Python scripts within Airflow tasks.
- Clean and format the data to meet storage requirements.
### Data Storage:
- Use Airflow's S3Hook to upload the transformed data to an S3 bucket.

## Technologies used
- Python
- Pandas
- Apache Airflow
- AWS S3

## How to run
1) Create an AWS account
2) Download and install Apache Airflow
3) Clone and download the code in from repository and run it in a Python IDE (preferably VScode)
6) Create an S3 bucket to store the data
7) Launch the Airflow console with the following command
   ```bash
   airflow standalone
8) Navigate to youtube_dag and run it
