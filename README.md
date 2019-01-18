# Project Idea 
A dashboard to lookup the **look-alike** product by matching the input image with other product photos in the same category (using interest point).

What is the interest point? !https://www.kaggle.com/wesamelshamy/image-feature-extraction-and-matching-for-newbies

# Tech Stack
1. AWS S3
2. Spark
4. Cassandra
5. Flask

# Data Source
Amazon review data: !http://jmcauley.ucsd.edu/data/amazon/
1. Review data (18GB) 
2. Product metadata (3.1GB)
3. Visual data (181 GB)

![reviews_df](https://user-images.githubusercontent.com/11646036/51401319-4bab2200-1aff-11e9-8083-0c8741a102c3.png)
  

# Engineering Challenge
1. How to join different datasets
2. Build a scalable distributed training pipeline for image vectors, that can both train on very large images, and train as fast as possible

# Business Value
1. Customers can filter products based on the shape/appearance/color of the product
2. For customers who can not elaborate what style of product they want, they can check the look-alike products intead of searching with keywords

# MVP
A dashboard that user can enter the product name. It will show some basic information (e.g. item name, price, rating etc) and **look-alike** products. If the user is not satisfied with the current item, then click on the look-alike product, which will direct the user to that item in the same category.

# Stretch Goals
* Workflow automation: Schedulers like Airflow
* Optimize the performance: Join different data sources, caching
