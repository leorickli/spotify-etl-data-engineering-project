# spotify-etl-data-engineering-project

### Introduction

This is an ETL project using the Spotify API to get the daily top 50 global songs in the app. This project will use the AWS cloud tools to extract the file from a Jupyter notebook using Python to process into an S3 bucket, separating data between artist, album and songs into another S3 bucket. Finally, it's going to load the data into AWS Athena for analysis using AWS Glue.

### Steps

- Use the Spotipy API to extract data from Spotify using a Jupyter Notebook to make the ETL (Extract, Transform, Load) in a local machine
- Use AWS CloudWatch to deploy the daily trigger that will activate the Python code
- Use AWS Lambda to extract data into a S3 bucket
- Add a trigger to run the transformation and loading into another S3 bucket automatically
- Use AWS CloudWatch again to write the transformation and loading fucntion
- Load the transformed file into another S3 bucket, dividing it into folders form "artist", "album" and "songs"
- Build Analytics Tables on data files using Glue and Athena
