# spotify-etl-data-engineering-project

### Introduction

This is an ETL project using the Spotify API to get the daily top 50 global songs in the app. This project will use the AWS cloud tools to extract the file from a Jupyter notebook using Python to process into an S3 bucket, separating data between artist, album and songs into another S3 bucket. Finally, it's going to load the data into AWS Athena for analysis using AWS Glue.

### About Datase/API

Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform. Wit this API, data will be extracted to get "artist", "album" and "song" data.
You can check the [Spotipy API](https://spotipy.readthedocs.io/) for more information and documentation regarding the API.

### AWS Services Used

- **S3 (Simple Storage Service):** Amazon S3 is a highly scalable object storage service that can store an retrieve any amount of data from anywhere on the web. It is commonly used to store and distribute large media files, data backups and static website files.
- **AWS Lambda:** Lambda is a serverless computing service that lets you run your code without managing servers. You can use Lambda to run code in response to events like changes in S3, DynamoDB or other AWS services.
- **CloudWatch:** Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.
- **Glue Crawler:** Glue Crawler is a fully managed service that automatically crawls your data sources, identifies data formats and infers schemas to create an AWS Glue Data Catalog.
- **Data Catalog:** AWS Glue Data Catalog is fully managed metadata repository that makes it easy to discover and manage data in AWS. You can use Glue Data Catalog with other AWS services such as Athena.
- **Athena:** Amazon Athena is an interactive query service that makes it easy to analyse data in Amazon S3 using standard SQL. You can use Athena to analyze data in your Glue Data Catalog or in other S3 buckets.

### Architecture

<img width="1163" alt="Screenshot 2023-03-16 at 15 17 22" src="https://user-images.githubusercontent.com/106999054/225715782-6e6165d1-8480-4a77-a0d1-e7fd693421d2.png">

### Steps

- Use the Spotipy API to extract data from Spotify using a Jupyter Notebook to make the ETL (Extract, Transform, Load) in a local machine
- Use AWS CloudWatch to deploy the daily trigger that will activate the Python code
- Use AWS Lambda to extract data into a S3 bucket
- Add a trigger to run the transformation and loading into another S3 bucket automatically
- Use AWS CloudWatch again to write the transformation and loading fucntion
- Load the transformed file into another S3 bucket, dividing it into folders form "artist", "album" and "songs"
- Build Analytics Tables on data files using Glue and Athena
