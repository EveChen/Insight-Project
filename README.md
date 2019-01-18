# Project Idea 
Aggregate ratings in each product by regions. Compare the average ratings, sentiments within five countries (US, UK, DE, FR, JP).

# Tech Stack
1. AWS S3: Has data in S3 bucket
2. Kafka: Import data to do partition, replication to make the pipeline more fault-tolerance
3. Spark: Batch streaming, doing aggregation, data manipulation (NLTK)
4. MySQL: Queries
5. Flask: Web application

# Data Source
Amazon open data: !https://registry.opendata.aws/amazon-reviews/

# Engineering Challenge
1. How to aggregate ratings efficiently? e.g. Use key-pair?
2. How to query a large scale of data efficiently? e.g. Presto?

# Business Value
Sellers on Amazon can identify customer preferences in different regions

# MVP
A web application that user can enter the product name. It will compare the ratings and different adjectives that different regions users used.

# Stretch Goals
Version1: Just compare ratings
Version2: Add sentiments analysis
Version3: Do it efficiently
