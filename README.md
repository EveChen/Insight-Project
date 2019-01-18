# Project Idea 
A dashboard to see the product features that the users may care about and inversely find other similar products based on the features listed

# Tech Stack
1. AWS S3: Has data in S3 bucket
2. Spark: Batch streaming, doing aggregation
4. Cassandra
5. Flask: Web application

# Data Source
Amazon review data: !http://jmcauley.ucsd.edu/data/amazon/
1. Review data (18GB): 
2. Product metadata (3.1GB)
3. Visual data (181 GB)

# Engineering Challenge
1. How to join different datasets, especially text joins image data
2. How to lookup the product features

# Business Value
Sellers on Amazon can identify customer preferences in different regions

# MVP
A web application that user can enter the product name. It will compare the ratings and different adjectives that different regions users used.

# Stretch Goals
* Version1: Just compare ratings
* Version2: Add sentiments analysis
* Version3: Do it efficiently
