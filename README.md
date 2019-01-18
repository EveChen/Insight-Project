# Project Idea 
A dashboard to see the product features that the users may care about and inversely find other similar products based on the features listed

# Tech Stack
1. AWS S3
2. Spark
4. Cassandra: 
5. Flask

# Data Source
Amazon review data: !http://jmcauley.ucsd.edu/data/amazon/
1. Review data (18GB) 
2. Product metadata (3.1GB)
3. Visual data (181 GB)

# Engineering Challenge
1. How to join different datasets, especially text joins image data
2. How to lookup the product features inversely? e.g. product -> features; feature -> products

# Business Value
Customers can filter products based on their prefered features

# MVP
A web application that user can enter the product name. It will show some basic information (e.g. item name, price, rating etc) and bunch of product features. If the user is not satisfied with the current item, then click on the specific feature tag, which will direct the user to similar items with the same feature tag.

# Stretch Goals
* Workflow automation: Schedulers like Airflow?
* Optimize the performance: Join different data sources, caching
