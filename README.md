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

## Setup
1. **Install Dependencies**: Use `pip` to install the required packages.
   ```bash
   pip install apache-airflow google-api-python-client pandas s3fs python-dotenv
   ```

2. **Environment Variables**: Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Run Airflow**: Start the Airflow web server and scheduler to manage the DAGs.
   ```bash
   airflow webserver --port 8080
   airflow scheduler
   ```

4. **Access the Airflow UI**: Open your browser and navigate to `http://localhost:8080` to trigger the DAG.

## Usage
- The DAG `youtube_videos_analytics_dag` can be triggered manually from the Airflow UI. It will fetch the most popular videos, process the data, and store the results in the specified S3 bucket.

## Output
- The ingested data is saved as `raw_youtube_comments.csv` in the S3 bucket.
- The processed data is saved as `processed_youtube_comments.csv` in the same S3 bucket.
