# Data orchestration with Airflow and AWS S3

## Overview
This is a project on orchestrating the flow of data from Google's API to an S3 bucket via Apache Airflow. 

## Components

#### Data Source: Youtube trending videos data
- The application emulates streaming data by sampling records from a CSV file in quick intervals.

#### Apache Airflow:
- Using Airflow, I orchestrated the data flow from an API to an S3 bucket, read data from the bucket and processed the data, and then redirected it to a new S3 bucket. This
  is a rudimentary approach of a complex ETL process.

#### AWS S3:
- Stores any form of data and provides easy and cheap access to it.

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
